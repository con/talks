// The DOM-free half of pdfdeck.html: how PDF pages become reveal.js slides.
// Unit tested by tests/pdfdeck_model.test.mjs.

const NAME = "[A-Za-z0-9][A-Za-z0-9._-]*";
const TALK_ID = new RegExp(`^${NAME}(/${NAME})?$`);
const LINK_SCHEMES = /^(https?:|mailto:)/i;
const HAS_DOMAIN = /^(?:https?:\/\/)?[^/]+\.[a-z]/i;
const WEB_ADDRESS = /\b(?:https?:\/\/|www\.)[^\s<>"'()[\]{}]+/gi;

// The talk named in a location.search string, or null.  Only a file stem, or
// one folder and a stem, is accepted, so ?talk= cannot point the viewer at
// another site or outside this directory.
export function talkId(search) {
  const id = new URLSearchParams(search).get("talk");
  return id && TALK_ID.test(id) && !id.includes("..") ? id : null;
}

// An event is a folder of PDFs: its lectures are the sections.yaml entries
// named <event>/<lecture>, in file order.  Returns [{id, title}].
export function lecturesOf(sections, event) {
  return Object.entries(sections || {})
    .filter(([id]) => id.startsWith(`${event}/`))
    .map(([id, entry]) => ({ id, title: String(entry.title ?? id) }));
}

// What a requested id shows: the PDF `id`, its `event` (the talks.yaml entry)
// and the event's `lectures`.  An event alone opens on its first lecture.
export function resolveTalk(sections, requested) {
  const event = requested.split("/")[0];
  const lectures = lecturesOf(sections, event);
  const id = requested === event && lectures.length ? lectures[0].id : requested;
  return { id, event, lectures };
}

// {page: title} (a parsed sections.yaml entry) as [{page, title}] in page
// order, always starting at page 1, without pages the PDF does not have.
export function sectionList(entry, numPages, fallbackTitle = "") {
  const list = Object.entries(entry || {})
    .map(([page, title]) => ({ page: Number(page), title: String(title) }))
    .filter((s) => Number.isInteger(s.page) && s.page >= 1 && s.page <= numPages)
    .sort((a, b) => a.page - b.page);
  if (!list.length || list[0].page !== 1) list.unshift({ page: 1, title: fallbackTitle });
  return list;
}

// Beamer gives every overlay of a frame the same page label, so consecutive
// equal labels are one frame.  With no usable labels (none, or one for the
// whole file) every page is a frame of its own.  A section start always opens
// a new frame.  Returns [{first, last}], 1-based and inclusive.
export function framesOf(numPages, labels, sectionPages = []) {
  const usable = labels && new Set(labels).size > 1;
  const starts = new Set(sectionPages);
  const frames = [];
  for (let page = 1; page <= numPages; page++) {
    const same = usable && page > 1 && labels[page - 1] === labels[page - 2];
    if (same && !starts.has(page)) frames[frames.length - 1].last = page;
    else frames.push({ first: page, last: page });
  }
  return frames;
}

// The two-level deck: each section holds the frames that start within it.
export function buildDeck(numPages, labels, sections) {
  const frames = framesOf(numPages, labels, sections.map((s) => s.page));
  return sections.map((section, i) => {
    const end = i + 1 < sections.length ? sections[i + 1].page : numPages + 1;
    return { ...section, frames: frames.filter((f) => f.first >= section.page && f.first < end) };
  });
}

// The page a frame shows at reveal.js fragment index `f` (undefined or -1
// before the first fragment, which is the frame's first page).
export function pageAtStep(frame, f) {
  const step = f === undefined || f === null ? -1 : f;
  return Math.min(frame.first + step + 1, frame.last);
}

// A reveal.js canvas with the aspect ratio of the PDF.
export function canvasSize(pageWidth, pageHeight, width = 1024) {
  return { width, height: Math.round((width * pageHeight) / pageWidth) };
}

// A link as CSS percentages of the page, or null if it goes anywhere other
// than a slide of this deck (`#/...`) or the web.  `rect` is [x1, y1, x2, y2] in viewport pixels.
export function linkBox(url, rect, viewWidth, viewHeight) {
  if (!url || !(url.startsWith("#/") || LINK_SCHEMES.test(url))) return null;
  const [x1, y1, x2, y2] = rect;
  const pct = (v, total) => `${((100 * v) / total).toFixed(3)}%`;
  return {
    url,
    left: pct(Math.min(x1, x2), viewWidth),
    top: pct(Math.min(y1, y2), viewHeight),
    width: pct(Math.abs(x2 - x1), viewWidth),
    height: pct(Math.abs(y2 - y1), viewHeight),
  };
}

// Where in the deck a PDF page is, as the URL hash reveal.js understands, or
// null if the deck has no such page.
export function hashOfPage(deck, page) {
  for (const [h, part] of deck.entries()) {
    const v = part.frames.findIndex((f) => page >= f.first && page <= f.last);
    if (v < 0) continue;
    const step = page - part.frames[v].first;
    return step ? `#/${h}/${v}/${step - 1}` : `#/${h}/${v}`;
  }
  return null;
}

// The address of a link written without a scheme, as \url{www.nitrc.org} comes
// out of pdfTeX as a file to launch.  Anything else is not for a browser.
export function withScheme(address) {
  if (/^https?:|^mailto:/i.test(address)) return address;
  if (/^[^\s@/]+@[^\s@/]+\.[^\s@/]+$/.test(address)) return `mailto:${address}`;
  return /^www\.[^\s/]+\.[^\s]+$/i.test(address) ? `http://${address}` : null;
}

// Web addresses are often only text on a slide.  Takes pdf.js text items and
// returns [{url, rect}], rect being [x1, y1, x2, y2] in PDF points, skipping
// any that overlaps a rect of `taken`, the links the PDF has itself.  Character
// positions are interpolated, which is close enough for a click target.
export function textLinks(items, taken = []) {
  const found = [];
  for (const line of textLines(items)) {
    for (const match of line.text.matchAll(WEB_ADDRESS)) {
      const address = match[0].replace(/[.,;:!?'"]+$/, "");
      const last = match.index + address.length - 1;
      const rect = [line.xs[match.index], line.y, line.xs[last] + line.widths[last], line.y + line.height];
      if (!HAS_DOMAIN.test(address) || taken.some((other) => overlap(rect, other))) continue;
      found.push({ url: withScheme(address), rect });
    }
  }
  return found;
}

// Horizontal items on one baseline as one string, with each character's place.
function textLines(items) {
  const lines = [];
  let line = null;
  for (const item of items) {
    const [a, b, , , x, y] = item.transform || [];
    if (!item.str || b || a <= 0) continue;
    const height = item.height || a;
    const width = item.width / item.str.length;
    const end = line && line.xs[line.xs.length - 1] + line.widths[line.widths.length - 1];
    if (!line || Math.abs(line.y - y) > height / 4 || x < end - height) {
      line = { text: "", xs: [], widths: [], y, height };
      lines.push(line);
    } else if (x - end > height / 4) {
      line.text += " ";
      line.xs.push(end);
      line.widths.push(x - end);
    }
    [...item.str].forEach((char, i) => {
      for (const unit of char) {  // match indices count UTF-16 units
        line.text += unit;
        line.xs.push(x + i * width);
        line.widths.push(width);
      }
    });
  }
  return lines;
}

function overlap(a, b) {
  const [ax1, ax2] = [Math.min(a[0], a[2]), Math.max(a[0], a[2])];
  const [ay1, ay2] = [Math.min(a[1], a[3]), Math.max(a[1], a[3])];
  const [bx1, bx2] = [Math.min(b[0], b[2]), Math.max(b[0], b[2])];
  const [by1, by2] = [Math.min(b[1], b[3]), Math.max(b[1], b[3])];
  return ax1 < bx2 && bx1 < ax2 && ay1 < by2 && by1 < ay2;
}

// The talks.yaml entry of a talk, if it has one.
export function talkEntry(talks, id) {
  return (talks || []).find((t) => t.path === `pdfdeck.html?talk=${id}`) || null;
}
