// Unit tests of pdfdeck/model.js; run by tests/test_pdfdeck.py, or directly
// with `node --test tests/pdfdeck_model.test.mjs`.
import assert from "node:assert/strict";
import { test } from "node:test";

import {
  buildDeck, canvasSize, framesOf, lecturesOf, linkBox, pageAtStep, resolveTalk, sectionList, talkEntry, talkId,
} from "../pdfdeck/model.js";

test("talkId takes a plain file stem", () => {
  assert.equal(talkId("?talk=2011-euroscipy-pymvpa"), "2011-euroscipy-pymvpa");
  assert.equal(talkId("?a=1&talk=2015_x.y"), "2015_x.y");
});

test("talkId takes a lecture within an event folder", () => {
  assert.equal(talkId("?talk=2014-giessen/mvpa-intro"), "2014-giessen/mvpa-intro");
});

test("talkId refuses anything that could leave the talks directory", () => {
  for (const search of ["", "?talk=", "?talk=../secret", "?talk=a/b/c", "?talk=a/", "?talk=/a", "?talk=a/.b", "?talk=a/../b", "?talk=.hidden",
    "?talk=a..b", "?talk=https://evil.example/x", "?talk=%2e%2e%2fsecret", "?talk=a%00b"]) {
    assert.equal(talkId(search), null, search);
  }
});

const EVENTS = {
  solo: { 1: "Only" },
  "ws/b": { title: "Second first", 1: "One" },
  "ws/a": { title: "Then this", 1: "One" },
  "wsx/c": { title: "Another event" },
};

test("lecturesOf keeps the file's order and only that event", () => {
  assert.deepEqual(lecturesOf(EVENTS, "ws"), [
    { id: "ws/b", title: "Second first" }, { id: "ws/a", title: "Then this" }]);
  assert.deepEqual(lecturesOf(EVENTS, "solo"), []);
  assert.deepEqual(lecturesOf(null, "ws"), []);
});

test("resolveTalk opens an event on its first lecture", () => {
  assert.equal(resolveTalk(EVENTS, "ws").id, "ws/b");
  assert.equal(resolveTalk(EVENTS, "ws").event, "ws");
});

test("resolveTalk keeps a named lecture and a plain talk", () => {
  assert.equal(resolveTalk(EVENTS, "ws/a").id, "ws/a");
  assert.equal(resolveTalk(EVENTS, "ws/a").lectures.length, 2);
  assert.deepEqual(resolveTalk(EVENTS, "solo"), { id: "solo", event: "solo", lectures: [] });
});

test("a lecture's title is not a section", () => {
  assert.deepEqual(sectionList({ title: "Lecture", 1: "One", 3: "Two" }, 5), [
    { page: 1, title: "One" }, { page: 3, title: "Two" }]);
});

test("sectionList sorts numerically and keeps titles as strings", () => {
  assert.deepEqual(sectionList({ 10: "Late", 2: "Mid", 1: 2009 }, 12), [
    { page: 1, title: "2009" }, { page: 2, title: "Mid" }, { page: 10, title: "Late" }]);
});

test("sectionList always covers page 1", () => {
  assert.deepEqual(sectionList({ 3: "B" }, 5, "Talk"), [{ page: 1, title: "Talk" }, { page: 3, title: "B" }]);
  assert.deepEqual(sectionList(undefined, 5, "Talk"), [{ page: 1, title: "Talk" }]);
  assert.deepEqual(sectionList({}, 5), [{ page: 1, title: "" }]);
});

test("sectionList drops pages the PDF does not have", () => {
  assert.deepEqual(sectionList({ 1: "A", 6: "gone", 0: "zero", "x": "bad" }, 5), [{ page: 1, title: "A" }]);
});

test("framesOf groups consecutive equal labels", () => {
  assert.deepEqual(framesOf(5, ["1", "2", "2", "2", "3"]), [
    { first: 1, last: 1 }, { first: 2, last: 4 }, { first: 5, last: 5 }]);
});

test("framesOf does not merge equal labels that are not adjacent", () => {
  // beamer restarts numbering after \appendix
  assert.deepEqual(framesOf(4, ["1", "2", "1", "1"]), [
    { first: 1, last: 1 }, { first: 2, last: 2 }, { first: 3, last: 4 }]);
});

test("framesOf treats pages as frames without usable labels", () => {
  const each = [{ first: 1, last: 1 }, { first: 2, last: 2 }, { first: 3, last: 3 }];
  assert.deepEqual(framesOf(3, null), each);
  assert.deepEqual(framesOf(3, ["", "", ""]), each);
  assert.deepEqual(framesOf(3, ["7", "7", "7"]), each);
});

test("framesOf opens a frame at a section start", () => {
  assert.deepEqual(framesOf(4, ["1", "1", "1", "2"], [1, 2]), [
    { first: 1, last: 1 }, { first: 2, last: 3 }, { first: 4, last: 4 }]);
});

test("buildDeck puts every page in exactly one section", () => {
  const deck = buildDeck(6, ["1", "2", "2", "3", "4", "4"], [
    { page: 1, title: "A" }, { page: 4, title: "B" }]);
  assert.deepEqual(deck.map((s) => s.title), ["A", "B"]);
  assert.deepEqual(deck[0].frames, [{ first: 1, last: 1 }, { first: 2, last: 3 }]);
  assert.deepEqual(deck[1].frames, [{ first: 4, last: 4 }, { first: 5, last: 6 }]);
  const pages = deck.flatMap((s) => s.frames).flatMap((f) =>
    Array.from({ length: f.last - f.first + 1 }, (_, i) => f.first + i));
  assert.deepEqual(pages, [1, 2, 3, 4, 5, 6]);
});

test("pageAtStep walks a frame's overlays and stays inside it", () => {
  const frame = { first: 5, last: 7 };
  assert.equal(pageAtStep(frame, undefined), 5);
  assert.equal(pageAtStep(frame, null), 5);
  assert.equal(pageAtStep(frame, -1), 5);
  assert.equal(pageAtStep(frame, 0), 6);
  assert.equal(pageAtStep(frame, 1), 7);
  assert.equal(pageAtStep(frame, 9), 7);
});

test("canvasSize keeps the page's aspect ratio", () => {
  assert.deepEqual(canvasSize(363, 272), { width: 1024, height: 767 });
  assert.deepEqual(canvasSize(454, 283), { width: 1024, height: 638 });
});

test("linkBox gives percentages, whichever way the rectangle runs", () => {
  const box = { url: "https://x.org", left: "10.000%", top: "20.000%", width: "30.000%", height: "10.000%" };
  assert.deepEqual(linkBox("https://x.org", [100, 200, 400, 300], 1000, 1000), box);
  assert.deepEqual(linkBox("https://x.org", [400, 300, 100, 200], 1000, 1000), box);
});

test("linkBox keeps external links only", () => {
  assert.ok(linkBox("mailto:a@b.c", [0, 0, 1, 1], 10, 10));
  assert.ok(linkBox("HTTP://x.org", [0, 0, 1, 1], 10, 10));
  for (const url of [undefined, "", "javascript:alert(1)", "file:///etc/passwd", "data:text/html,x"]) {
    assert.equal(linkBox(url, [0, 0, 1, 1], 10, 10), null, url);
  }
});

test("talkEntry finds a talk by its viewer path", () => {
  const talks = [{ path: "x.html" }, { path: "pdfdeck.html?talk=t", title: "T" }];
  assert.equal(talkEntry(talks, "t").title, "T");
  assert.equal(talkEntry(talks, "u"), null);
  assert.equal(talkEntry(null, "t"), null);
});
