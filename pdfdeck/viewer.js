// Presents one PDF as a reveal.js deck.  There are no per-slide files: each
// slide is a canvas painted from the PDF on demand, which pdf.js fetches with
// HTTP range requests.  See pdfdeck/README.md.
import * as pdfjs from "../3rd-party/pdfjs/pdf.min.js";
import { buildDeck, canvasSize, linkBox, pageAtStep, resolveTalk, sectionList, talkEntry, talkId } from "./model.js";

pdfjs.GlobalWorkerOptions.workerSrc = new URL("../3rd-party/pdfjs/pdf.worker.min.js", import.meta.url).href;

const PIXELS_MAX = 3200;  // widest bitmap we render, however large the screen
const THUMB_WIDTH = 320;  // overview tiles
const CACHE_SIZE = 10;    // rendered pages kept for instant stepping
const KEEP_FRAMES = 2;    // frames painted on either side of the current one

const slides = document.querySelector(".reveal .slides");
const bar = document.getElementById("bar");
const toc = document.getElementById("toc");

function fail(message, href, text) {
  document.body.classList.add("failed");
  const box = document.getElementById("message");
  box.textContent = message;
  if (href) {
    const a = document.createElement("a");
    a.href = href;
    a.textContent = text;
    box.append(" ", a);
  }
  document.documentElement.dataset.pdfdeck = "failed";
}

async function yamlFile(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`${url}: HTTP ${response.status}`);
  return window.jsyaml.load(await response.text());
}

function frameSection(frame) {
  const section = document.createElement("section");
  section.className = "frame";
  section.dataset.transition = "none";
  section.append(document.createElement("canvas"));
  const links = document.createElement("div");
  links.className = "links";
  section.append(links);
  for (let i = 0; i < frame.last - frame.first; i++) {
    const step = document.createElement("span");
    step.className = "fragment";
    section.append(step);
  }
  frame.section = section;
  return section;
}

function buildSlides(deck) {
  for (const part of deck) {
    const stack = document.createElement("section");
    stack.dataset.transition = "slide";
    stack.dataset.title = part.title;
    stack.append(...part.frames.map(frameSection));
    slides.append(stack);
  }
}

function buildToc(deck) {
  deck.forEach((part, h) => {
    const item = document.createElement("li");
    const button = document.createElement("button");
    button.textContent = part.title || `Section ${h + 1}`;
    button.addEventListener("click", () => {
      window.Reveal.slide(h, 0, -1);
      toc.hidden = true;
    });
    item.append(button);
    toc.querySelector("ol").append(item);
  });
}

function buildLectures(lectures, current) {
  const list = document.getElementById("lectures");
  for (const lecture of lectures) {
    const link = document.createElement("a");
    link.href = `pdfdeck.html?talk=${lecture.id}`;
    link.textContent = lecture.title;
    if (lecture.id === current) link.className = "current";
    const item = document.createElement("li");
    item.append(link);
    list.append(item);
  }
  list.hidden = !lectures.length;
}

// Rendered pages, most recently used last; entries are promises of canvases.
const cache = new Map();

function rendered(pdf, page, width) {
  const key = `${page}@${width}`;
  const hit = cache.get(key);
  if (hit) {
    cache.delete(key);
    cache.set(key, hit);
    return hit;
  }
  const job = pdf.getPage(page).then(async (pdfPage) => {
    const natural = pdfPage.getViewport({ scale: 1 });
    const viewport = pdfPage.getViewport({ scale: width / natural.width });
    const canvas = document.createElement("canvas");
    canvas.width = Math.round(viewport.width);
    canvas.height = Math.round(viewport.height);
    await pdfPage.render({ canvas, canvasContext: canvas.getContext("2d"), viewport }).promise;
    return canvas;
  });
  cache.set(key, job);
  job.catch(() => cache.delete(key));
  if (cache.size > CACHE_SIZE) cache.delete(cache.keys().next().value);
  return job;
}

async function pageLinks(pdf, page) {
  const pdfPage = await pdf.getPage(page);
  const viewport = pdfPage.getViewport({ scale: 1 });
  const annotations = await pdfPage.getAnnotations({ intent: "display" });
  return annotations
    .filter((a) => a.subtype === "Link")
    .map((a) => {
      const corners = [...viewport.convertToViewportPoint(a.rect[0], a.rect[1]),
        ...viewport.convertToViewportPoint(a.rect[2], a.rect[3])];
      return linkBox(a.url, corners, viewport.width, viewport.height);
    })
    .filter(Boolean);
}

async function paint(pdf, frame, page, width) {
  const canvas = frame.section.querySelector("canvas");
  if (canvas.dataset.page === `${page}@${width}`) return;
  frame.wanted = `${page}@${width}`;
  const bitmap = await rendered(pdf, page, width);
  const boxes = await pageLinks(pdf, page);
  if (frame.wanted !== `${page}@${width}`) return;  // moved on meanwhile
  canvas.width = bitmap.width;
  canvas.height = bitmap.height;
  canvas.getContext("2d").drawImage(bitmap, 0, 0);
  canvas.dataset.page = `${page}@${width}`;
  frame.section.dataset.page = page;
  const links = frame.section.querySelector(".links");
  links.replaceChildren(...boxes.map((box) => {
    const a = document.createElement("a");
    a.href = box.url;
    a.rel = "noopener";
    a.title = box.url;
    Object.assign(a.style, { left: box.left, top: box.top, width: box.width, height: box.height });
    return a;
  }));
}

function release(frame) {
  const canvas = frame.section.querySelector("canvas");
  frame.wanted = null;
  if (canvas.dataset.page) {
    canvas.width = canvas.height = 0;
    delete canvas.dataset.page;
  }
}

function start(pdf, deck, numPages, size) {
  const Reveal = window.Reveal;
  const frames = deck.flatMap((part) => part.frames);

  function pixelWidth() {
    const width = size.width * Reveal.getScale() * (window.devicePixelRatio || 1);
    return Math.min(PIXELS_MAX, Math.max(THUMB_WIDTH, Math.round(width)));
  }

  function current() {
    const { h, v, f } = Reveal.getIndices();
    const frame = deck[h].frames[v || 0];
    return { h, frame, page: pageAtStep(frame, f) };
  }

  function refreshBar({ h, page }) {
    document.getElementById("where").textContent = deck[h].title;
    document.getElementById("count").textContent = `${page} / ${numPages}`;
    [...toc.querySelectorAll("button")].forEach((b, i) => b.classList.toggle("current", i === h));
  }

  // Paint what is on screen first, then what the next keypress may reveal,
  // and let go of everything else: a 150 page talk must not hold 150 bitmaps.
  async function refresh() {
    if (Reveal.isOverview()) return overview();
    const here = current();
    const width = pixelWidth();
    refreshBar(here);
    await paint(pdf, here.frame, here.page, width);
    document.documentElement.dataset.pdfdeck = "ready";
    const at = frames.indexOf(here.frame);
    const near = frames.slice(Math.max(0, at - KEEP_FRAMES), at + KEEP_FRAMES + 1);
    const stacks = [deck[here.h - 1], deck[here.h + 1]].filter(Boolean).map((part) => part.frames[0]);
    for (const frame of frames) {
      if (!near.includes(frame) && !stacks.includes(frame)) release(frame);
    }
    if (here.page < here.frame.last) rendered(pdf, here.page + 1, width).catch(() => {});
    for (const frame of [...near, ...stacks]) {
      if (frame === here.frame) continue;
      const page = frames.indexOf(frame) < at ? frame.last : frame.first;
      await paint(pdf, frame, page, width);
    }
  }

  // Tiles show a frame fully built, and only reveal.js' visible ones are drawn.
  async function overview() {
    for (const frame of frames) {
      if (!Reveal.isOverview()) return;
      const hidden = frame.section.style.display === "none" || frame.section.parentNode.style.display === "none";
      if (!hidden) await paint(pdf, frame, frame.last, THUMB_WIDTH);
    }
  }

  for (const event of ["slidechanged", "fragmentshown", "fragmenthidden", "overviewshown", "overviewhidden", "resize"]) {
    Reveal.on(event, refresh);
  }
  document.getElementById("menu").addEventListener("click", () => { toc.hidden = !toc.hidden; });
  Reveal.addKeyBinding({ keyCode: 84, key: "T", description: "Sections" }, () => { toc.hidden = !toc.hidden; });
  bar.hidden = false;
  return refresh();
}

async function main() {
  const requested = talkId(window.location.search);
  if (!requested) return fail("No talk given: this page needs ?talk=<TALK-ID>.", "index.html", "All talks");

  const [talks, sections] = await Promise.all([yamlFile("talks.yaml"), yamlFile("pdfdeck/sections.yaml")]);
  const { id, event, lectures } = resolveTalk(sections, requested);
  const talk = talkEntry(talks, event);
  const lecture = lectures.find((l) => l.id === id);
  const title = lecture ? lecture.title : talk ? talk.title : id;
  const url = `${id}.pdf`;
  document.title = title;
  document.getElementById("pdf").href = url;
  document.getElementById("heading").textContent = [talk ? talk.title : title, talk && talk.venue, talk && talk.date].filter(Boolean).join(" · ");

  let pdf;
  try {
    pdf = await pdfjs.getDocument({
      url,
      disableAutoFetch: true,
      disableStream: true,
      rangeChunkSize: 1 << 20,
      standardFontDataUrl: "3rd-party/pdfjs/standard_fonts/",
    }).promise;
  } catch (error) {
    console.error(error);
    return fail(`Could not load ${url}.`, "index.html", "All talks");
  }

  const numPages = pdf.numPages;
  const firstPage = await pdf.getPage(1);
  const { width, height } = firstPage.getViewport({ scale: 1 });
  const size = canvasSize(width, height);
  const deck = buildDeck(numPages, await pdf.getPageLabels(), sectionList(sections && sections[id], numPages, title));
  buildSlides(deck);
  buildToc(deck);
  buildLectures(lectures, id);

  await window.Reveal.initialize({
    ...size,
    margin: 0,
    minScale: 0.05,
    maxScale: 8,
    center: false,
    hash: true,
    fragmentInURL: true,
    controls: true,
    progress: true,
    transitionSpeed: "fast",
    backgroundTransition: "none",
  });
  return start(pdf, deck, numPages, size);
}

main().catch((error) => {
  console.error(error);
  fail(`Could not start: ${error.message}`, "index.html", "All talks");
});
