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


def pub(slug, date, path, kind="bibo:Slideshow", pdf=None, venue="Somewhere",
        roles=("marcrel:aut",), author_list=None):
    attrs = [{"predicate": "bibo:presentedAt", "value": venue},
             {"predicate": "foaf:homepage", "value": BASE + path}]
    if pdf:
        attrs.append({"predicate": "dcat:downloadURL", "value": BASE + pdf})
    if author_list:
        attrs.append({"predicate": "bibo:authorList", "value": author_list})
    return {"pid": f"xyzrins:publications/{slug}", "kind": kind, "title": slug,
            "attributes": attrs,
            "attributed_to": [{"object": "xyzrins:persons/someone", "roles": list(roles)}],
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


@pytest.mark.ai_generated
def test_pdf_shown_through_the_viewer_is_listed_and_covered(store, capsys):
    repo, add = store
    (repo / "2011-x.pdf").write_bytes(b"%PDF")
    add(slug="talk-2011-x", date="2011-08", path="pdfdeck.html?talk=2011-x", pdf="2011-x.pdf")
    entries = mk_index.load_entries()
    assert entries[0]["path"] == "pdfdeck.html?talk=2011-x"
    assert entries[0]["pdf"] == BASE + "2011-x.pdf"
    mk_index.check_coverage(entries)
    assert "has no talk record" not in capsys.readouterr().err
    page = mk_index.render(entries)
    assert 'href="pdfdeck.html?talk=2011-x"' in page
    assert 'href="2011-x.pdf"' in page


@pytest.mark.ai_generated
def test_root_pdf_without_a_record_is_still_reported(store, capsys):
    repo, _ = store
    (repo / "2011-orphan.pdf").write_bytes(b"%PDF")
    mk_index.check_coverage(mk_index.load_entries())
    assert "2011-orphan.pdf has no talk record" in capsys.readouterr().err


@pytest.mark.ai_generated
def test_presenter_is_bold_among_the_authors(store):
    _, add = store
    add(slug="t", date="2026-01-01", path="t.html",
        roles=("marcrel:aut", "marcrel:spk"), author_list="Some One; A & B")
    [e] = mk_index.load_entries()
    assert e["authors"] == ["Some One", "A & B"]
    assert e["presenters"] == ["Some One"]
    out = mk_index.render([e])
    assert '<span class="authors"><strong>Some One</strong>, A &amp; B</span>' in out


@pytest.mark.ai_generated
def test_talk_without_presenter_has_all_authors_bold_poster_none(store):
    _, add = store
    add(slug="t", date="2026-01-02", path="t.html", author_list="Some One; Other Person")
    add(slug="p", date="2026-01-01", path="p.pdf", kind="fabio:ConferencePoster")
    t, p = mk_index.load_entries()
    assert "presenters" not in t and "presenters" not in p
    out = mk_index.render([t, p])
    assert ('<span class="authors"><strong>Some One</strong>, '
            '<strong>Other Person</strong></span>') in out
    assert '<span class="authors">Some One</span>' in out


@pytest.mark.ai_generated
def test_people_on_whoweare_link_to_their_anchor(store):
    _, add = store
    persons = {
        "a": {"display_label": "Yaroslav O. Halchenko",
              "attributes": [{"predicate": "dlthings:tier", "value": "Centroids"}]},
        "b": {"display_label": "Jean-Baptiste Poline",
              "attributes": [{"predicate": "dlthings:tier", "value": "Collaborators"}]},
        "c": {"display_label": "Oliver Rübel",
              "attributes": [{"predicate": "dlthings:tier", "value": "Collaborators"}]},
        "d": {"display_label": "Not Listed"},
    }
    links = mk_index.whoweare_links(persons)
    assert links == {
        "Yaroslav O. Halchenko": mk_index.WHOWEARE + "yaroslav_o_halchenko_",
        "Jean-Baptiste Poline": mk_index.WHOWEARE + "jeanbaptiste_poline_",
        "Oliver Rübel": mk_index.WHOWEARE + "oliver_rübel_"}
    add(slug="t", date="2026-01-01", path="t.html", roles=("marcrel:spk",),
        author_list="Some One; Yaroslav O. Halchenko")
    out = mk_index.render(mk_index.load_entries(), links)
    assert (f'Some One</strong>, <a href="{mk_index.WHOWEARE}yaroslav_o_halchenko_">'
            'Yaroslav O. Halchenko</a></span>') in out
    assert ('2026-01-01 &middot; Somewhere &middot; '
            '<a class="alt file" href="t.html">t.html</a></span></li>') in out


@pytest.mark.ai_generated
def test_presenter_outside_the_author_list_is_warned(store, capsys):
    _, add = store
    add(slug="t", date="2026-01-01", path="t.html",
        roles=("marcrel:spk",), author_list="Other Person")
    mk_index.check_presenters(mk_index.load_entries())
    assert "presenter Some One is not among its authors" in capsys.readouterr().err


@pytest.mark.ai_generated
def test_doi_links_after_the_title(store):
    repo, add = store
    add(slug="d", date="2026-01-02", path="d.html")
    add(slug="n", date="2026-01-01", path="n.html")
    f = repo.parent / "records/XYZPublication/d.yaml"
    d = yaml.safe_load(f.read_text())
    d["identifiers"] = [{"notation": "https://example.org/x", "schema_type": "dlthings:Identifier"},
                        {"notation": "10.5281/zenodo.1", "schema_type": "dlthings:DOI"}]
    f.write_text(yaml.safe_dump(d))
    entries = mk_index.load_entries()
    assert entries[0]["doi"] == "10.5281/zenodo.1" and "doi" not in entries[1]
    out = mk_index.render(entries)
    assert out.count('href="https://doi.org/') == 1
    assert '(<a class="alt" href="https://doi.org/10.5281/zenodo.1">DOI</a>)' in out


@pytest.mark.ai_generated
def test_video_links_after_the_title(store):
    repo, add = store
    add(slug="v", date="2026-01-02", path="v.html")
    add(slug="n", date="2026-01-01", path="n.html")
    f = repo.parent / "records/XYZPublication/v.yaml"
    d = yaml.safe_load(f.read_text())
    url = "https://example.org/web/#/video/abc"
    d["attributes"].append({"predicate": "schema:video", "value": url})
    f.write_text(yaml.safe_dump(d))
    entries = mk_index.load_entries()
    assert entries[0]["video"] == url and "video" not in entries[1]
    out = mk_index.render(entries)
    assert out.count("CONTube") == 1
    assert f'(<a class="alt" href="{url}">📺 CONTube</a>)' in out


@pytest.mark.ai_generated
def test_video_only_talk_links_the_video_and_says_so(store):
    repo, add = store
    add(slug="v", date="2026-01-02", path="v.html")
    add(slug="n", date="2026-01-01", path="n.html")
    url = "https://example.org/web/#/video/abc"
    f = repo.parent / "records/XYZPublication/v.yaml"
    d = yaml.safe_load(f.read_text())
    d["attributes"] = [a for a in d["attributes"] if a["predicate"] != "foaf:homepage"]
    d["attributes"].append({"predicate": "schema:video", "value": url})
    f.write_text(yaml.safe_dump(d))
    entries = mk_index.load_entries()
    assert (entries[0]["path"], entries[0]["url"]) == ("", url)
    out = mk_index.render(entries)
    assert f'<a href="{url}">v</a>' in out
    assert f'📺 CONTube</a>) (no slides, video only) <span' in out
    assert out.count("no slides, video only") == 1
    assert 'class="alt file" href=""' not in out


@pytest.mark.ai_generated
def test_no_homepage_and_no_video_is_left_out(store):
    repo, add = store
    add(slug="x", date="2026-01-01", path="x.html")
    f = repo.parent / "records/XYZPublication/x.yaml"
    d = yaml.safe_load(f.read_text())
    d["attributes"] = [a for a in d["attributes"] if a["predicate"] != "foaf:homepage"]
    f.write_text(yaml.safe_dump(d))
    assert mk_index.load_entries() == []


@pytest.mark.ai_generated
def test_google_slides_link_after_the_pdf(store):
    repo, add = store
    add(slug="talk-2020-x", date="2020-01-01", path="pdfdeck.html?talk=2020-x", pdf="2020-x.pdf")
    f = repo.parent / "records/XYZPublication/talk-2020-x.yaml"
    d = yaml.safe_load(f.read_text())
    url = "https://docs.google.com/presentation/d/abc"
    d["attributes"].append({"predicate": "dcterms:source", "value": url})
    f.write_text(yaml.safe_dump(d))
    out = mk_index.render(mk_index.load_entries())
    assert (f'PDF</a>) (<a class="alt" href="{url}">Google Slides</a>)') in out
