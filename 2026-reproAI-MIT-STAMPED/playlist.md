# Companion video playlist — `2026-reproAI-MIT-STAMPED`

A curated playlist to publish on the
[**ReproNim YouTube channel**](https://www.youtube.com/@repronim) alongside
the talk, so the audience can follow every video reference from one place.

**Proposed playlist title**: *STAMPED & AI-assisted scientific software — companion viewing*
**Proposed description**:

> Companion playlist for "STAMPED principles and their role in the age of
> AI-driven scientific software development" (Y. O. Halchenko, LLM Workshop,
> MIT, 2026-10-16).
> Slides: https://datasets.datalad.org/centerforopenneuroscience/talks/2026-reproAI-MIT-STAMPED.html
> Grouped as: the principles → the provenance machinery → the AI-practice
> evidence. Videos 4–8 are not ours; they are included under YouTube's
> playlist mechanism, which links rather than copies.

All metadata below was read from YouTube with `yt-dlp` on **2026-10-06** —
licenses in particular are *verified*, not assumed.

## The playlist

| # | Video | Channel | Date | Len | License | Why it is in the talk |
| -- | ------------------------------------------------------------------------------------------------------- | -------------------- | ---------- | ----- | --------------------- | ------------------------------------------------------------------------- |
| 1 | [YODA: Structure your studies, observable and reproducible they become](https://www.youtube.com/watch?v=1XbTbJ_P2x0) | ReproNim             | 2026-02-06 | 61 m  | Standard (ours)       | The predecessor talk — slide 3, "Standing on two talks"                    |
| 2 | [Pragmatic YODA: YODA principles and their wild life encounters](https://www.youtube.com/watch?v=EuKVapscUQ4) | DataLad              | 2025-11-12 | 28 m  | **CC-BY**             | The distribits parent of the YODA spine                                    |
| 3 | [Isaac To, Y. Halchenko: DataLad-Registry](https://www.youtube.com/watch?v=_McJ1BtLsiQ)                     | DataLad              | 2024-04-09 | 18 m  | **CC-BY**             | Where the "`datalad run` in the wild" statistics come from                 |
| 4 | [Joey Hess: "git annex is complete, right?"](https://www.youtube.com/watch?v=pp8IeGXpRRI)                   | DataLad              | 2024-04-09 | 21 m  | **CC-BY**             | Background for the Tracked layer; also the HI↔AI "Reject" row              |
| 5 | [Michał Szczepanik: compute on demand](https://www.youtube.com/watch?v=lP-VPjwonB0)                        | DataLad              | 2025-11-12 | 22 m  | **CC-BY**             | `git-annex addcomputed` — provenance that regenerates rather than stores   |
| 6 | [Jo Van Eyck: You are Not Ready — Agentic coding in 2026](https://www.youtube.com/watch?v=6W_-YWHKwZ4)      | Jo Van Eyck          | 2026-02-08 | 31 m  | Standard — link only  | Source of the **AI coding maturity ladder** (L1–L5) slide                  |
| 7 | [Simon Willison: Engineering practices that make coding agents work](https://www.youtube.com/watch?v=owmJyKVu5f8) | The Pragmatic Engineer | 2026-03-19 | 28 m  | Standard — link only  | The harness argument, from the other direction                             |
| 8 | [Simon Willison: An AI state of the union (Lenny's Podcast)](https://youtu.be/wc8FBhQtdsA)                  | Lenny's Podcast      | 2026-04-02 | 100 m | Standard — link only  | "Testing is the new bottleneck"; the *"I haven't used it yet"* point       |

Suggested order: **1 → 2 → 3 → 5 → 4 → 6 → 7 → 8** (ours first, principles
before machinery, AI-practice last).

### Not on YouTube (link from the deck only)

- [Oscar Esteban, *Using LLMs in Neuroimaging Research: LLMs for Coding*](https://www.nipreps.org/presentations/2026-OHBM-AI-Educational/) — OHBM 2026 Educational; web deck, no recording located.
- [*A few words of intro into AI assisted coding*](https://datasets.datalad.org/centerforopenneuroscience/talks/2026-ca-origami-retreat-aicoding.html) — CA Origami Retreat 2026; not recorded.

If either is recorded later, add it as #9/#10 and re-sync this file.

## Creating the playlist

Needs an account with edit rights on the ReproNim channel. Either:

**Web UI** — YouTube Studio → Content → Playlists → New playlist, paste the
title/description above, then add each video by URL in the suggested order.

**API** (reproducible, and the ids are already here):

```bash
# requires an OAuth token with https://www.googleapis.com/auth/youtube scope
# on an account that can edit the ReproNim channel
yt-dlp --flat-playlist --print id <existing-playlist-url>   # sanity-check ids
# then youtube.playlists.insert + youtube.playlistItems.insert per id, in order:
# 1XbTbJ_P2x0 EuKVapscUQ4 _McJ1BtLsiQ lP-VPjwonB0 pp8IeGXpRRI 6W_-YWHKwZ4 owmJyKVu5f8 wc8FBhQtdsA
```

Once created, add the playlist URL to:

- the deck's appendix ("Related CON talks" slide),
- this file's header,
- `INDEX.md`'s entry for the talk.

## ReproTube / archival backup

**Licensing rule applied here**: only mirror what the licence permits.
The four **CC-BY** videos (#2–#5) may be redistributed with attribution.
#1 is ReproNim's own. #6–#8 are Standard YouTube Licence — they are
**linked, never mirrored**.

Status checked against <https://datasets.datalad.org/repronim/ReproTube/>
on 2026-10-06 — **everything that may be mirrored already is**:

| Video | In ReproTube? | Path |
| ------------------------------- | ------------- | --------------------------------------------------------------------------------- |
| #1 YODA webinar                 | **yes**       | `ReproNim/videos/2026/02/2026-02-06_YODA-Structure-your-studies-…/`                |
| #2 Pragmatic YODA               | **yes**       | `DataLad/playlists/Distribits-2025/0011_…Pragmatic-YODA…/`                         |
| #3 DataLad-Registry             | **yes**       | `DataLad/playlists/Distribits-2024/0022_…DataLad-Registry…/`                       |
| #4 git-annex is complete, right?| **yes**       | `DataLad/playlists/Distribits-2024/0029_…git-annex-is-complete-right/`             |
| #5 compute on demand            | **yes**       | `DataLad/playlists/Distribits-2025/0026_…compute-on-demand/`                       |
| #6–#8 external, Standard licence| **no — and correctly so** | link only                                                             |

So no archival work is outstanding. ReproTube already tracks both the
`ReproNim` and `DataLad` channels (see
[`channels.tsv`](https://datasets.datalad.org/repronim/ReproTube/channels.tsv))
and is syncing current — a 2026-10-05 ReproNim video is present.

### One open item

[`annextube`](https://github.com/con/annextube) models **channels**, and
mirrors each channel's *own* playlists. It has no concept of a curated
**cross-channel** playlist, which is what this one is. So this playlist can
live on YouTube, but it will not round-trip into ReproTube as a unit.

Two options, neither urgent:

1. Leave it. Every mirrorable video is already archived under its own
   channel; the playlist is a *view*, and views are cheap to recreate.
   (This is the YODA/"dashboards visualise, don't own" position, and is
   the recommended default.)
2. File a small feature request on `con/annextube`: allow a configured
   playlist URL to be archived as a cross-channel view, storing only the
   ordered id list plus symlinks into the existing per-channel video dirs
   — no duplicated bytes, and it would skip any video whose licence
   forbids mirroring.

## Re-verifying this file

```bash
for id in 1XbTbJ_P2x0 EuKVapscUQ4 _McJ1BtLsiQ lP-VPjwonB0 pp8IeGXpRRI 6W_-YWHKwZ4 owmJyKVu5f8 wc8FBhQtdsA; do
  uv run --with yt-dlp yt-dlp --skip-download --no-warnings \
    --print "%(id)s|%(license)s|%(channel)s|%(upload_date)s|%(duration)s|%(title)s" \
    "https://www.youtube.com/watch?v=$id"
done
```

A video's licence **can change**. Re-run the above before any mirroring
action, not just before publishing the playlist.
