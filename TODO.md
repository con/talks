# TODO

## Slides to find for talks listed as video only

These talks have a CONTube recording but no slides here, so `index.html`
lists them with the title linking to the video and marks them
"(no slides, video only)".  That is what a record with `schema:video` and no
`foaf:homepage` gets.

To add the slides of one: put the PDF at the repository root, add
`foaf:homepage` and `dcat:downloadURL` to its record, then follow the steps
for a PDF deck (`pdfdeck/sections.yaml`, `REUSE.toml`, `INDEX.md`).  The mark
goes away by itself.

- **DataLad** (NIF NeuroTools Webinar, 2018-03-02;
  `talk-2018-nif-datalad-webinar`)
  - https://datasets.datalad.org/centerforopenneuroscience/contube/web/#/video/59CE6iOr45k
  - No deck identified.  The video is titled "DataLad, Dr. Yaroslav O.
    Halchenko".
  - `2018-mcgill-datalad` has the venue "NIF/NIH online cast, McGill" and the
    date 2018-03, but this video is not that talk.  Its venue may need fixing.
- **Computational basis** (OHBM 2018 Educational Course "Hands on
  reproducible brain imaging", 2018-06-17; `talk-2018-ohbm-computational-basis`)
  - https://datasets.datalad.org/centerforopenneuroscience/contube/web/#/video/2Qm4krjaSfM
  - The session as the [OHBM 2018 program](https://www.humanbrainmapping.org/files/2018/2018%20Singapore%20Program_FINAL.pdf)
    names it, which also lists Michael Hanke for it; the lessons are on
    https://repronim.org/ohbm2018-training/.
  - Largely hands-on, so there may be no slides at all.
- **A guide to DANDI, the BRAIN Initiative archive for publishing and sharing
  neurophysiology data** (NWB User Days 2021, 2021-08-26;
  `talk-2021-nwb-dandi-guide`)
  - https://datasets.datalad.org/centerforopenneuroscience/contube/web/#/video/8OMLmUnc6Cs
  - Slides are shown in the video, but none were found publicly.
- **Research Data Management & Data tracking** (OHBM 2023 Educational Course,
  part 5, 2023-07-22; `talk-2023-ohbm-rdm-data-tracking`)
  - https://datasets.datalad.org/centerforopenneuroscience/contube/web/#/video/cYQWk8eQLlI
  - `TrainingCore/2023-OHBM-Educational-course/2023-OHBM-Educational-course.docx`
    on the ReproNim Drive may link the slides.
- **DataLad-Registry: Bringing Benefits of Centrality to DataLad** (Isaac To
  and Yaroslav O. Halchenko, distribits 2024, 2024-04-05;
  `talk-2024-distribits-datalad-registry`)
  - https://datasets.datalad.org/centerforopenneuroscience/contube/web/#/video/_McJ1BtLsiQ
  - The [talk page](https://www.distribits.live/talks/2024/to-registry/) has no
    slides, so ask Isaac, who presented it.
- **BIDS Talk & Q&A for 2024 The Neuro – Irv and Helga Cooper Foundation
  International Prize** (Open Science in Action Symposium, 2023-11-30;
  `talk-2024-neuro-prize-bids`)
  - https://datasets.datalad.org/centerforopenneuroscience/contube/web/#/video/6QoFWqfIZDU
  - The speaker says the slides were prepared by Ariel.  Check whether they
    are `202404xx-NSF-POSE-BIDS.pdf`, which credits Ariel Rokem and Rémi Gau.
  - The date is that of the prize ceremony on
    [The Neuro's page](https://www.mcgill.ca/neuro/article/rewarding-excellence-open-science),
    but the video says "2024" and was published 2024-04-29, so confirm it.
