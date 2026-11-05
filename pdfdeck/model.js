// The DOM-free half of pdfdeck.html: how PDF pages become reveal.js slides.
// Unit tested by tests/pdfdeck_model.test.mjs.

const NAME = "[A-Za-z0-9][A-Za-z0-9._-]*";
const TALK_ID = new RegExp(`^${NAME}(/${NAME})?$`);
const LINK_SCHEMES = /^(https?:|mailto:)/i;

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

// A link annotation as CSS percentages of the page, or null if it is not an
// external link.  `rect` is [x1, y1, x2, y2] in viewport pixels.
export function linkBox(url, rect, viewWidth, viewHeight) {
  if (!url || !LINK_SCHEMES.test(url)) return null;
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

// The talks.yaml entry of a talk, if it has one.
export function talkEntry(talks, id) {
  return (talks || []).find((t) => t.path === `pdfdeck.html?talk=${id}`) || null;
}
