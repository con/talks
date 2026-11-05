"""pdfdeck.html end to end, in a real browser, on PDFs made here.

Each page of a test PDF is a solid colour derived from its number, so reading
a pixel back from the canvas proves which page is on screen.

    uv run --with pytest --with pyyaml --with playwright --with pymupdf pytest tests/
"""
import functools
import http.server
import os
import re
import threading

import pytest

pymupdf = pytest.importorskip("pymupdf")
sync_api = pytest.importorskip("playwright.sync_api")
expect = sync_api.expect

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pytestmark = pytest.mark.ai_generated

# page labels as beamer writes them: frame 2 has three overlays, frame 4 two
LABELS = ["1", "2", "2", "2", "3", "4", "4", "5"]
SECTIONS = """\
overlays:
  1: Opening
  5: Middle
  8: Closing
workshop/first:
  title: The first lecture
  1: Start
  2: End
workshop/second:
  title: The second lecture
  1: Only
"""
TALKS = """\
- path: pdfdeck.html?talk=overlays
  title: A Test Talk
  venue: Testconf
  date: '2011-01'
- path: pdfdeck.html?talk=workshop
  title: A Test Workshop
  venue: Testshop
  date: '2012-02'
"""


def colour(page):
    return (page * 25 % 256, (255 - page * 20) % 256, 100)


def make_pdf(path, pages, labels=None, width=363, height=272):
    doc = pymupdf.open()
    for n in range(1, pages + 1):
        page = doc.new_page(width=width, height=height)
        page.draw_rect(page.rect, fill=[c / 255 for c in colour(n)], color=None)
        page.insert_text((20, 40), f"Page {n}")
    if labels:
        doc.set_page_labels([{"startpage": i, "prefix": label, "firstpagenum": 1, "style": ""}
                             for i, label in enumerate(labels)])
    doc[1].insert_link({"kind": pymupdf.LINK_URI, "uri": "https://example.org/on-page-2",
                        "from": pymupdf.Rect(36, 27, 181, 68)})
    doc[1].insert_link({"kind": pymupdf.LINK_URI, "uri": "javascript:alert(1)",
                        "from": pymupdf.Rect(0, 100, 50, 150)})
    doc.save(path)


def make_links_pdf(path):
    """A slide with every kind of link, and the page one of them goes to."""
    doc = pymupdf.open()
    doc.new_page(width=363, height=272)
    for n in (2, 3):
        page = doc.new_page(width=363, height=272)
        page.draw_rect(page.rect, fill=[c / 255 for c in colour(n)], color=None)
    first = doc[0]
    first.insert_text((20, 40), "Text http://example.org/text here")
    first.insert_text((20, 80), "http://example.org/own")
    first.insert_link({"kind": pymupdf.LINK_URI, "uri": "http://example.org/own",
                       "from": pymupdf.Rect(15, 65, 200, 90)})
    first.insert_link({"kind": pymupdf.LINK_GOTO, "page": 2, "to": pymupdf.Point(0, 0),
                       "from": pymupdf.Rect(20, 120, 120, 150)})
    first.insert_link({"kind": pymupdf.LINK_LAUNCH, "file": "www.example.org",
                       "from": pymupdf.Rect(20, 160, 120, 190)})
    first.insert_link({"kind": pymupdf.LINK_LAUNCH, "file": "demo.avi",
                       "from": pymupdf.Rect(20, 200, 120, 230)})
    doc.save(path)


def make_big_pdf(path, pages=30):
    """Pages holding about 1MB of incompressible image each."""
    doc = pymupdf.open()
    for _ in range(pages):
        page = doc.new_page(width=363, height=272)
        pix = pymupdf.Pixmap(pymupdf.csRGB, 600, 600, os.urandom(600 * 600 * 3), False)
        page.insert_image(page.rect, pixmap=pix)
    doc.save(path, deflate=False, use_objstms=1)  # as pdfTeX does


class Handler(http.server.SimpleHTTPRequestHandler):
    """A static server with the Range support datasets.datalad.org has."""
    ranged = {}  # bytes sent per file in answer to Range requests

    def log_message(self, *args):
        pass

    def do_GET(self):
        path = self.translate_path(self.path)
        match = re.fullmatch(r"bytes=(\d+)-(\d*)", self.headers.get("Range", ""))
        if not (path.endswith(".pdf") and os.path.isfile(path)):
            return super().do_GET()
        size = os.path.getsize(path)
        start, end = (int(match[1]), int(match[2] or size - 1)) if match else (0, size - 1)
        end = min(end, size - 1)
        self.send_response(206 if match else 200)
        self.send_header("Content-Type", "application/pdf")
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(end - start + 1))
        if match:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.end_headers()
        name = os.path.basename(path)
        with open(path, "rb") as f:
            f.seek(start)
            left = end - start + 1
            while left:
                chunk = f.read(min(left, 1 << 16))
                try:
                    self.wfile.write(chunk)
                except (BrokenPipeError, ConnectionResetError):
                    return  # pdf.js drops its first request once it sees Accept-Ranges
                left -= len(chunk)
                if match:
                    Handler.ranged[name] = Handler.ranged.get(name, 0) + len(chunk)


@pytest.fixture(scope="session")
def site(tmp_path_factory):
    root = tmp_path_factory.mktemp("site")
    for name in ("pdfdeck.html", "3rd-party", "reveal.js"):
        (root / name).symlink_to(os.path.join(REPO, name))
    (root / "pdfdeck").mkdir()
    for name in ("model.js", "viewer.js"):
        (root / "pdfdeck" / name).symlink_to(os.path.join(REPO, "pdfdeck", name))
    (root / "pdfdeck/sections.yaml").write_text(SECTIONS)
    (root / "talks.yaml").write_text(TALKS)
    (root / "index.html").write_text("<title>All talks</title>")
    make_pdf(root / "overlays.pdf", len(LABELS), LABELS)
    make_pdf(root / "plain.pdf", 3)
    make_pdf(root / "wide.pdf", 2, width=454, height=283)
    make_big_pdf(root / "big.pdf")
    make_links_pdf(root / "links.pdf")
    (root / "workshop").mkdir()
    make_pdf(root / "workshop/first.pdf", 2)
    make_pdf(root / "workshop/second.pdf", 3)
    handler = functools.partial(Handler, directory=str(root))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{server.server_address[1]}", root
    server.shutdown()


@pytest.fixture(scope="session")
def browser():
    with sync_api.sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(viewport={"width": 1024, "height": 768})
    page = context.new_page()
    page.errors = []
    page.on("pageerror", lambda e: page.errors.append(str(e)))
    page.on("console", lambda m: page.errors.append(m.text) if m.type == "error" else None)
    yield page
    context.close()


def open_talk(page, site, talk="overlays", hash_=""):
    page.goto(f"{site[0]}/pdfdeck.html?talk={talk}{hash_}")
    page.wait_for_function("document.documentElement.dataset.pdfdeck === 'ready'")


def wait_for_page(page, number):
    """Wait until the visible slide shows PDF page `number`; check its pixels."""
    page.wait_for_function(
        "n => document.querySelector('section.frame.present')?.dataset.page === String(n)"
        " && document.querySelector('section.frame.present canvas').dataset.page.startsWith(n + '@')",
        arg=number)
    assert pixel(page) == pytest.approx(colour(number), abs=2)


def pixel(page):
    return page.evaluate("""() => {
        const c = document.querySelector('section.frame.present canvas');
        const d = c.getContext('2d').getImageData(c.width - 3, c.height - 3, 1, 1).data;
        return [d[0], d[1], d[2]];
    }""")


def indices(page):
    return page.evaluate("Reveal.getIndices()")


def test_opens_on_the_first_page(page, site):
    open_talk(page, site)
    wait_for_page(page, 1)
    assert page.title() == "A Test Talk"
    expect(page.locator("#where")).to_have_text("Opening")
    expect(page.locator("#count")).to_have_text("1 / 8")
    expect(page.locator("#pdf")).to_have_attribute("href", "overlays.pdf")
    assert page.errors == []


def test_sections_are_columns_and_frames_are_rows(page, site):
    open_talk(page, site)
    assert page.locator(".slides > section").count() == 3
    per_section = page.evaluate(
        "[...document.querySelectorAll('.slides > section')].map(s => s.querySelectorAll('section.frame').length)")
    assert per_section == [2, 2, 1]
    assert page.locator("section.frame .fragment").count() == 3  # 2 for frame 2, 1 for frame 4


def test_right_goes_to_the_next_section(page, site):
    open_talk(page, site)
    page.keyboard.press("ArrowRight")
    wait_for_page(page, 5)
    expect(page.locator("#where")).to_have_text("Middle")
    page.keyboard.press("ArrowRight")
    wait_for_page(page, 8)
    page.keyboard.press("ArrowLeft")
    wait_for_page(page, 5)


def test_down_goes_to_the_next_frame(page, site):
    open_talk(page, site)
    page.keyboard.press("ArrowDown")
    wait_for_page(page, 2)
    assert indices(page)["v"] == 1


def test_space_steps_through_every_page_in_order(page, site):
    open_talk(page, site)
    for number in range(1, len(LABELS) + 1):
        wait_for_page(page, number)
        expect(page.locator("#count")).to_have_text(f"{number} / 8")
        page.keyboard.press("Space")
    assert page.errors == []


def test_going_back_through_overlays_undoes_them(page, site):
    open_talk(page, site, hash_="#/0/1/1")
    wait_for_page(page, 4)
    page.keyboard.press("Shift+Space")
    wait_for_page(page, 3)
    page.keyboard.press("Shift+Space")
    wait_for_page(page, 2)
    page.keyboard.press("Shift+Space")
    wait_for_page(page, 1)


def test_overlays_stay_on_one_slide(page, site):
    open_talk(page, site, hash_="#/0/1")
    wait_for_page(page, 2)
    page.keyboard.press("Space")
    wait_for_page(page, 3)
    assert indices(page)["h"] == 0 and indices(page)["v"] == 1 and indices(page)["f"] == 0


def test_url_tracks_the_position_and_restores_it(page, site):
    open_talk(page, site)
    for _ in range(3):
        page.keyboard.press("Space")
    wait_for_page(page, 4)
    page.wait_for_function("location.hash.startsWith('#/0/1/')")
    url = page.url
    page.goto("about:blank")
    page.goto(url)
    page.wait_for_function("document.documentElement.dataset.pdfdeck === 'ready'")
    wait_for_page(page, 4)


def test_section_transitions_differ_from_frame_transitions(page, site):
    open_talk(page, site)
    stacks = page.evaluate("[...document.querySelectorAll('.slides > section')].map(s => s.dataset.transition)")
    frames = page.evaluate("[...document.querySelectorAll('section.frame')].map(s => s.dataset.transition)")
    assert set(stacks) == {"slide"} and set(frames) == {"none"}


def test_pdf_links_are_clickable_and_unsafe_ones_are_gone(page, site):
    open_talk(page, site, hash_="#/0/1")
    wait_for_page(page, 2)
    link = page.locator("section.frame.present .links a")
    expect(link).to_have_count(1)
    assert link.get_attribute("href") == "https://example.org/on-page-2"
    box, slide = link.bounding_box(), page.locator("section.frame.present canvas").bounding_box()
    assert box["x"] - slide["x"] == pytest.approx(0.1 * slide["width"], abs=3)
    assert box["width"] == pytest.approx(0.4 * slide["width"], abs=3)


def test_addresses_in_text_are_links_and_only_once(page, site):
    open_talk(page, site, talk="links")
    links = page.locator("section.frame.present .links a")
    expect(links).to_have_count(4)
    hrefs = [a.get_attribute("href") for a in links.all()]
    assert hrefs.count("http://example.org/own") == 1
    assert "http://example.org/text" in hrefs
    assert "demo.avi" not in hrefs


def test_a_text_link_sits_on_its_text(page, site):
    open_talk(page, site, talk="links")
    link = page.locator('section.frame.present .links a[href="http://example.org/text"]')
    box, slide = link.bounding_box(), page.locator("section.frame.present canvas").bounding_box()
    scale = slide["width"] / 363
    assert slide["y"] + 25 * scale < box["y"] + box["height"] / 2 < slide["y"] + 45 * scale
    assert box["x"] > slide["x"] + 40 * scale


def test_a_link_without_a_scheme_gets_one(page, site):
    open_talk(page, site, talk="links")
    expect(page.locator('section.frame.present .links a[href^="http://www.example.org"]')).to_have_count(1)


def test_a_link_within_the_pdf_goes_to_that_slide(page, site):
    open_talk(page, site, talk="links")
    page.locator('section.frame.present .links a[href^="#/"]').click()
    wait_for_page(page, 3)
    assert page.evaluate("Reveal.getIndices().v") == 2


def test_a_footer_link_under_the_bar_can_be_clicked(page, site):
    open_talk(page, site, talk="links")
    page.evaluate("""() => {
        const a = document.querySelector('section.frame.present .links a[href^="#/"]');
        Object.assign(a.style, {left: '10%', top: '93%', width: '20%', height: '5%'});
    }""")
    page.locator('section.frame.present .links a[href^="#/"]').click()
    wait_for_page(page, 3)


def test_links_follow_the_overlay_on_screen(page, site):
    open_talk(page, site, hash_="#/0/1")
    wait_for_page(page, 2)
    page.keyboard.press("Space")
    wait_for_page(page, 3)
    expect(page.locator("section.frame.present .links a")).to_have_count(0)


def test_section_list_by_key_and_by_button(page, site):
    open_talk(page, site)
    toc = page.locator("#toc")
    expect(toc).to_be_hidden()
    page.keyboard.press("t")
    expect(toc).to_be_visible()
    expect(toc.locator("#heading")).to_have_text("A Test Talk · Testconf · 2011-01")
    assert toc.locator("ol > li button").all_text_contents() == ["Opening", "Middle", "Closing"]
    assert toc.locator("ol > li").count() == 3  # numbered from 1: no stray items
    page.keyboard.press("t")
    expect(toc).to_be_hidden()
    page.locator("#menu").click()
    toc.get_by_role("button", name="Closing").click()
    wait_for_page(page, 8)
    expect(toc).to_be_hidden()


def test_overview_shows_frames_fully_built_and_returns(page, site):
    open_talk(page, site)
    page.keyboard.press("o")
    page.wait_for_function("Reveal.isOverview()")
    page.wait_for_function(
        "[...document.querySelectorAll('section.frame canvas')].every(c => c.dataset.page)")
    built = page.evaluate("[...document.querySelectorAll('section.frame')].map(s => +s.dataset.page)")
    assert built == [1, 4, 5, 7, 8]
    assert page.evaluate("document.querySelector('section.frame canvas').width") == 320
    page.keyboard.press("Escape")
    page.wait_for_function("!Reveal.isOverview()")
    page.wait_for_function("document.querySelector('section.frame.present canvas').width > 320")
    wait_for_page(page, 1)


def test_bitmaps_are_released_when_far_away(page, site):
    make_pdf(site[1] / "long.pdf", 40)
    open_talk(page, site, talk="long")
    for number in range(1, 16):
        page.keyboard.press("Space")
        page.wait_for_function("n => document.querySelector('section.frame.present').dataset.page === String(n)",
                               arg=number + 1)
    page.wait_for_timeout(300)
    painted = page.evaluate("[...document.querySelectorAll('section.frame canvas')].filter(c => c.dataset.page).length")
    assert 1 <= painted <= 7
    held = page.evaluate("[...document.querySelectorAll('section.frame canvas')].filter(c => c.width > 300).length")
    assert held == painted


def test_bitmap_follows_the_window_size(page, site):
    open_talk(page, site)
    small = page.evaluate("document.querySelector('section.frame.present canvas').width")
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.wait_for_function("w => document.querySelector('section.frame.present canvas').width > w", arg=small)
    wait_for_page(page, 1)


def test_slide_fills_the_window_at_the_pdfs_aspect_ratio(page, site):
    open_talk(page, site, talk="wide")
    assert page.evaluate("Reveal.getConfig().height / Reveal.getConfig().width") == pytest.approx(283 / 454, abs=.002)
    box = page.locator("section.frame.present canvas").bounding_box()
    assert box["width"] == pytest.approx(1024, abs=2)


def test_talk_without_labels_or_sections_still_works(page, site):
    open_talk(page, site, talk="plain")
    assert page.locator(".slides > section").count() == 1
    assert page.locator("section.frame").count() == 3
    assert page.locator("section.frame .fragment").count() == 0
    assert page.title() == "plain"
    page.keyboard.press("ArrowDown")
    wait_for_page(page, 2)


def test_opening_a_large_pdf_does_not_download_it_all(page, site):
    # pdf.js first sends a plain GET and drops it on seeing Accept-Ranges, which
    # over a real network costs little and on localhost cannot be told apart
    # from a full download; what it then asks for is what matters.
    Handler.ranged.pop("big.pdf", None)
    open_talk(page, site, talk="big")
    page.wait_for_timeout(500)
    assert 0 < Handler.ranged["big.pdf"] < 0.5 * (site[1] / "big.pdf").stat().st_size


@pytest.mark.parametrize("query", ["", "?talk=", "?talk=../talks", "?talk=https://example.org/x"])
def test_bad_talk_names_are_refused_before_any_request(page, site, query):
    requests = []
    page.on("request", lambda r: requests.append(r.url))
    page.goto(f"{site[0]}/pdfdeck.html{query}")
    expect(page.locator("#message")).to_contain_text("No talk given")
    expect(page.locator("#message a")).to_have_attribute("href", "index.html")
    assert not [u for u in requests if u.endswith(".pdf") or u.startswith("https://example.org")]


def test_an_event_opens_on_its_first_lecture(page, site):
    open_talk(page, site, talk="workshop")
    assert page.locator("#pdf").get_attribute("href") == "workshop/first.pdf"
    assert page.title() == "The first lecture"
    assert page.locator(".slides > section").count() == 2


def test_lectures_are_listed_and_the_list_moves_between_them(page, site):
    open_talk(page, site, talk="workshop")
    page.keyboard.press("t")
    expect(page.locator("#heading")).to_contain_text("A Test Workshop")
    links = page.locator("#lectures a")
    expect(links).to_have_text(["The first lecture", "The second lecture"])
    expect(page.locator("#lectures a.current")).to_have_text("The first lecture")
    links.nth(1).click()
    page.wait_for_function("document.documentElement.dataset.pdfdeck === 'ready'")
    assert page.url.endswith("?talk=workshop/second")
    assert page.locator("#pdf").get_attribute("href") == "workshop/second.pdf"
    assert page.locator(".slides > section").count() == 1
    page.keyboard.press("t")
    expect(page.locator("#lectures a.current")).to_have_text("The second lecture")


def test_a_talk_of_its_own_lists_no_lectures(page, site):
    open_talk(page, site)
    page.keyboard.press("t")
    expect(page.locator("#lectures")).to_be_hidden()


def test_missing_pdf_says_so(page, site):
    page.goto(f"{site[0]}/pdfdeck.html?talk=absent")
    expect(page.locator("#message")).to_contain_text("Could not load absent.pdf")
    expect(page.locator(".reveal")).to_be_hidden()
