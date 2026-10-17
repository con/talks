"""tools/mk_index.py: records -> index.html, on a throwaway record store."""
import importlib.util
import pathlib

import pytest
import yaml

SPEC = importlib.util.spec_from_file_location(
    "mk_index", pathlib.Path(__file__).resolve().parent.parent / "tools/mk_index.py")
mk_index = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mk_index)
BASE = mk_index.BASE


def pub(slug, date, path, kind="bibo:Slideshow", pdf=None, venue="Somewhere"):
    attrs = [{"predicate": "bibo:presentedAt", "value": venue},
             {"predicate": "foaf:homepage", "value": BASE + path}]
    if pdf:
        attrs.append({"predicate": "dcat:downloadURL", "value": BASE + pdf})
    return {"pid": f"xyzrins:publications/{slug}", "kind": kind, "title": slug,
            "attributes": attrs,
            "attributed_to": [{"object": "xyzrins:persons/someone"}],
            "generated_by": [{"at_time": date, "object": "xyzrins:."}]}


@pytest.fixture
def store(tmp_path, monkeypatch):
    repo, records = tmp_path / "talks", tmp_path / "records"
    for d in (repo, records / "XYZPublication", records / "XYZPerson"):
        d.mkdir(parents=True)
    (records / "XYZPerson/someone.yaml").write_text(yaml.safe_dump(
        {"pid": "xyzrins:persons/someone", "given_name": "Some", "family_name": "One"}))
    monkeypatch.setattr(mk_index, "HERE", repo)
    monkeypatch.setattr(mk_index, "RECORDS", records)

    def add(**kw):
        d = pub(**kw)
        (records / f"XYZPublication/{kw['slug']}.yaml").write_text(yaml.safe_dump(d))
    return repo, add


@pytest.mark.ai_generated
def test_newest_first_month_after_known_days(store):
    _, add = store
    add(slug="a", date="2026-06", path="a.html")
    add(slug="b", date="2026-06-02", path="b.html")
    add(slug="c", date="2025-01-01", path="c.html")
    assert [e["path"] for e in mk_index.load_entries()] == ["b.html", "a.html", "c.html"]


@pytest.mark.ai_generated
def test_wip_and_unpublished_are_left_out(store):
    repo, add = store
    (repo / "wip.html").write_text("<title>[WiP] Draft</title>")
    add(slug="wip", date="2026-01-01", path="wip.html")
    add(slug="ok", date="2026-01-01", path="ok.html")
    d = pub("elsewhere", "2026-01-01", "x.html")
    d["attributes"][1]["value"] = "https://example.org/x.html"
    (mk_index.RECORDS / "XYZPublication/elsewhere.yaml").write_text(yaml.safe_dump(d))
    assert [e["path"] for e in mk_index.load_entries()] == ["ok.html"]


@pytest.mark.ai_generated
def test_render_poster_tag_pdf_and_years(store):
    _, add = store
    add(slug="p", date="2026-10-19", path="v/p.html", kind="fabio:ConferencePoster",
        pdf="v/p.pdf", venue="Conf & Co")
    add(slug="t", date="2024-04", path="t.html")
    out = mk_index.render(mk_index.load_entries())
    assert out.index("<h2>2026</h2>") < out.index("<h2>2024</h2>")
    assert '<span class="kind">poster</span>' in out
    assert '(<a class="alt" href="v/p.pdf">PDF</a>)' in out
    assert "2026-10-19 &middot; Conf &amp; Co" in out
    assert out.count('<ul class="talks">') == out.count("</ul>") == 2


@pytest.mark.ai_generated
def test_root_deck_without_record_is_warned(store, capsys):
    repo, add = store
    (repo / "2026-new-talk.html").write_text("<title>New</title>")
    add(slug="ok", date="2026-01-01", path="ok.html")
    mk_index.check_coverage(mk_index.load_entries())
    assert "2026-new-talk.html has no talk record" in capsys.readouterr().err
