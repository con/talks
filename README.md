# Annex content for `enh-2026-dhmc-ieeg` (con/talks PR 27)

Ephemeral branch: plain copies of the 7 images that `enh-2026-dhmc-ieeg`
references as git-annex symlinks (MD5E keys). Not meant to be merged.

git-annex knows each file's jsDelivr URL, pinned to this branch's commit, so
`git annex get <file>` works through the web remote. To also copy the
content to an annex remote:

```bash
git annex get pics/2026-dhmc-ieeg-*.svg pics/dandi-compute-figure.svg pics/neurosift-event-related-*-20261007.png
git annex copy --to datasets.datalad.org pics/2026-dhmc-ieeg-*.svg pics/dandi-compute-figure.svg pics/neurosift-event-related-*-20261007.png
```
