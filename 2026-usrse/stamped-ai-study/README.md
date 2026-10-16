# STAMPED in Practice poster

Can research guidance help AI agents do sound science and leave work others can inspect and reproduce?
This **44 × 44 inch** poster presents a comparison of four kinds of assistance across three rounds of a shared neuroscience task.
It shows both scientific results and how the research guidance was tested and revised.

## Read the poster

- [Download the current PDF](https://hub.centerforopenneuroscience.org/git-annex-p2phttp/git-annex/40d344f5-0628-494e-82e4-9fab0949ed12/key/MD5E-s910371--6f48fd0b93942251b8caa9b6b4499a89.pdf).
- [View the image preview](https://hub.centerforopenneuroscience.org/git-annex-p2phttp/git-annex/40d344f5-0628-494e-82e4-9fab0949ed12/key/MD5E-s1141436--34dba72fb838f6c37d03eddb4322138b.png).
- [Read the poster and figure guide](https://github.com/leej3/stamped-in-practice/blob/main/docs/poster.md) for context before following individual research records.

The PDF and preview are publicly downloadable; their contents have been checked against the reviewed local export.
GitHub may show annexed files as pointers, so use the download links above rather than expecting those pointers to display the poster.

## Follow the story

The left column introduces STAMPED and the experiment.
The centre shows one agent's brain analysis and where repeated analyses agree.
The right compares scientific adequacy and research practices, including their progression across rounds.
The scientific and checklist measures describe different outcomes; an improvement in one does not establish an improvement in the other.
The plot shows 95% Wilson intervals for scientific adequacy and individual checklist scores with means ± one standard deviation.
Each linked table score opens the condition’s individual filled checklists and original responses.
The table uses mean app scores out of all 31 items; the plot uses the fraction of evaluated items met, a separate measure.

Choose a starting point for the part you want to explore:

- [Results and interpretation](https://github.com/leej3/stamped-in-practice/blob/main/docs/results.md) explains the measures, missing assessments and limits of the comparison, then leads to the underlying tables.
- [Scientific figures](https://github.com/leej3/stamped-in-practice/blob/main/docs/poster.md#interpret-the-scientific-figures) explains what each image represents and where its inputs and plotting code live.
- [Research skills and assessment](https://github.com/leej3/stamped-in-practice/blob/main/docs/skills.md) introduces the workflows, the independent assessor and the revisions tested in each round.
- [Repository map](https://github.com/leej3/stamped-in-practice/blob/main/docs/repository-map.md) explains why evidence links open different branches and how to read an individual research delivery.

The poster's general links and QR codes lead to these introductions.
Links labelled **Analysis code**, **Numerical results**, **Figure code**, **Map inputs** or **Round data + denominators** open the named material directly.

## Edit or reproduce the poster

This directory is in the presentation repository, `con/talks`, on the `codex/stamped-example-poster` branch.
The scientific records and figure-generation workflow belong to `leej3/stamped-in-practice`; this directory holds display copies, their source bindings and the editable [HTML](index.html) and [CSS](poster.css).
The [build guide](BUILDING.md) covers retrieval, source imports, the exact environment and export checks.

The exported poster passes checks for its page size, minimum 24-point text, links, QR codes and public downloads, plus a visual review.
These agent checks support author review.
The [build guide's verification records](BUILDING.md#verification-and-provenance) contain the details; the [completion record](completion-plan.md) and [poster history](https://github.com/con/talks/commits/codex/stamped-example-poster/2026-usrse/stamped-ai-study) preserve how the poster developed.
