"""pdfdeck.html: the viewer's unit tests, and the catalogue's integrity."""
import pathlib
import re
import shutil
import subprocess

import pytest
import yaml

REPO = pathlib.Path(__file__).resolve().parent.parent
SECTIONS = yaml.safe_load((REPO / "pdfdeck/sections.yaml").read_text()) or {}
TALKS = yaml.safe_load((REPO / "talks.yaml").read_text())
VIEWED = {t["path"].split("=", 1)[1]: t for t in TALKS
          if t["path"].startswith("pdfdeck.html?talk=")}
EVENTS = {talk.split("/")[0] for talk in SECTIONS if "/" in talk}


@pytest.mark.ai_generated
@pytest.mark.skipif(not shutil.which("node"), reason="needs node")
def test_model_unit_tests():
    r = subprocess.run(["node", "--test", "tests/pdfdeck_model.test.mjs"],
                       cwd=REPO, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


@pytest.mark.ai_generated
def test_every_viewed_talk_has_sections_and_every_entry_a_talk():
    assert set(VIEWED) == {talk.split("/")[0] for talk in SECTIONS}


@pytest.mark.ai_generated
@pytest.mark.parametrize("talk", sorted(SECTIONS))
def test_sections_are_well_formed(talk):
    pages = [p for p in SECTIONS[talk] if p != "title"]
    assert pages[0] == 1, "a talk's first section starts on page 1"
    assert pages == sorted(set(pages)), "pages ascend"
    assert all(isinstance(p, int) for p in pages)
    assert all(str(t).strip() for t in SECTIONS[talk].values())
    assert ("title" in SECTIONS[talk]) == ("/" in talk), "lectures, and only they, have a title"


@pytest.mark.ai_generated
@pytest.mark.parametrize("talk", sorted(set(VIEWED) - EVENTS))
def test_talk_id_is_servable_and_has_a_pdf_link(talk):
    assert re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", talk)
    assert (REPO / f"{talk}.pdf").is_symlink() or (REPO / f"{talk}.pdf").exists()
    assert VIEWED[talk]["pdf"].endswith(f"/{talk}.pdf")


@pytest.mark.ai_generated
@pytest.mark.parametrize("event", sorted(EVENTS))
def test_an_event_has_no_single_pdf_and_each_lecture_has_one(event):
    assert "pdf" not in VIEWED[event]
    for talk in SECTIONS:
        if talk.startswith(f"{event}/"):
            assert re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*", talk)
            assert (REPO / f"{talk}.pdf").is_symlink() or (REPO / f"{talk}.pdf").exists()


@pytest.mark.ai_generated
@pytest.mark.parametrize("talk", sorted(SECTIONS))
def test_sections_fit_the_pdf(talk):
    pymupdf = pytest.importorskip("pymupdf")
    pdf = REPO / f"{talk}.pdf"
    if not pdf.exists():
        pytest.skip("annexed content not present")
    with pymupdf.open(pdf) as doc:
        assert max(p for p in SECTIONS[talk] if p != "title") <= doc.page_count
