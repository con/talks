---
marp: true
theme: default
paginate: true
size: 16:9
header: ''
footer: 'mechababs · McGill · 2026-08-11'
style: |
  section {
    font-family: "Inter", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 26px;
    padding: 60px 70px;
    background: #fbfbf9;
    color: #1c2024;
  }
  h1 {
    font-size: 58px;
    color: #10403b;
    letter-spacing: -0.02em;
    margin-bottom: 0.2em;
  }
  h2 {
    font-size: 40px;
    color: #10403b;
    letter-spacing: -0.015em;
    border-bottom: 3px solid #cfe3df;
    padding-bottom: 12px;
    margin-bottom: 0.5em;
  }
  h3 {
    font-size: 28px;
    color: #2b6a60;
    margin-bottom: 0.3em;
  }
  strong { color: #0d3330; }
  a { color: #2b6a60; }
  code {
    background: #eef2f1;
    color: #14524a;
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 0.92em;
  }
  pre {
    background: #10403b;
    border-radius: 8px;
    padding: 22px 26px;
  }
  pre code { background: transparent; color: #eaf3f1; font-size: 30px; }
  table { font-size: 23px; border-collapse: collapse; width: 100%; }
  th {
    background: #10403b; color: #fbfbf9;
    text-align: left; padding: 10px 14px; font-weight: 600;
  }
  td { padding: 10px 14px; border-bottom: 1px solid #dde5e3; vertical-align: top; }
  td:first-child, td:first-child code { white-space: nowrap; }
  ul { line-height: 1.55; }
  li { margin-bottom: 0.35em; }
  blockquote {
    border-left: 5px solid #c98a3c;
    background: #fdf6ec;
    padding: 14px 22px;
    font-style: normal;
    color: #5c4420;
  }
  footer { color: #9aa6a3; font-size: 15px; }
  section::after { color: #9aa6a3; font-size: 15px; }
  section.lead { justify-content: center; text-align: left; }
  section.lead h1 { font-size: 66px; border: none; }
  section.punch h2 { border: none; }
  section.term pre { padding: 18px 22px; }
  section.term pre code { font-size: 16px; line-height: 1.45; }
  section.term h2 { font-size: 34px; margin-bottom: 0.35em; }
  .small { font-size: 21px; color: #5a6664; }
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# mechababs

## STAMPED execution of BIDS Apps at scale

>Austin Macdonald
Center for Open Neuroscience,
Department of Psychological and Brain Sciences, Dartmouth College

`github.com/con/mechababs`

---

## Why: So many datasets!

- OpenNeuro has many public BIDS datasets, perhaps 1000+ are targets
- Goal: run MRIQC and fMRIPrep across all of them, and publish the outputs to OpenNeuroDerivatives
- The hard parts:
  - **scale**
  - provenance capture
  - inconsistency of datasets

---

## How: STAMPED

Properties a research object should have — `github.com/stamped-principles`

- **S**elf-contained — everything under one boundary
- **T**racked — version control and provenance
- **A**ctionable — executable, documented workflows
- **M**odular — independent, composable parts
- **P**ortable — runs anywhere, specifications explicit
- **E**phemeral — the compute environment is transient
- **D**istributable — shareable, persistent, retrievable

---

## How: DataLad

- DataLad can be tricky
- Humans are error prone
- Provenance that depends on a human remembering to `datalad save` is provenance you cannot trust
- So for this project: **the tool does DataLad, the user does not**

---

## What: BABS

[BABS](https://github.com/PennLINC/babs) (PennLINC) implements the **FAIRly big** workflow
<span class="small">Wagner, Waite, Wierzba et al. · `psychoinformatics-de/fairly-big-processing-workflow`</span>

 - DataLad Native
 - Ephemeral execution
 - Per-subject isolation

---

## BABS interface

- **`babs init`** — scaffold the jobs from a config, a container, and an inclusion list
- **`babs submit`** — break the work into one job per subject/session
- **`babs status`** — where every job is: queued, running, done, failed, and log locations
- **`babs merge`** — combine the per-job branches

```
partial clone → datalad run → push to RIA → merge
```

---

## What: mechababs

**Automation and orchestration 1 level up**

A **campaign**: a pipeline of BIDS Apps applied to arbitrary datasets.

- DataLad-native, same as babs. The user still does not do DataLad.
- **Declarative, not imperative.** Humans make decisions in config files, not at execution time.
- `mechababs iterate` is **a reconciler**: read current state, determine the next step, advance.

---

## Splitting the config layer

BABS takes one config file per derivative.

mechababs decomposes it, so pieces can be shared.
One config per axis, composed at deploy time into the single config babs consumes.
Recomposed per dataset X bids-app X cluster

| Axis | Holds | Who owns it |
|---|---|---|
| **Cluster** | SLURM resources, job preamble, scratch paths | the lab, shared across all its runs |
| **BIDS App** | container reference, app flags | the method, shared across labs |
| **Dataset** | which data, which subjects | shared across derivatives in a study|

---

## Output structure

**BIDS Study + BIDS Derivative.** Every level is a DataLad dataset and valid BIDS.

### Superstudy — *mechababs produces optionally*
run many studies through one campaign, view them together

### Study — *mechababs produces*
one or more raw source datasets, plus the derivatives made from them
**will be fully operable alone**
`GeneratedBy` mechababs + babs

### Derivative — *produced by babs*
execution provenance: could be repeated on a different system
`GeneratedBy` the BIDS App itself

---
<!-- _class: term -->

## Derivative details

```
$ tree -L 1 derivatives/fMRIPrep-25.2.5+anat
.
├── dataset_description.json                  # GeneratedBy the BIDS App
├── CHANGELOG.md
├── README.md
├── desc-aparcaseg_dseg.tsv
├── desc-aseg_dseg.tsv
├── code                                      # the babs scaffold
├── containers                                # the image that ran
├── sourcedata                                # the raw data, pinned
├── logs
├── sub-0001
├── sub-0001.html
├── sub-0001_fMRIPrep-25.2.5+anat-25-2-5.zip
└── sub-0002, sub-0003                        # the same three each

7 directories, 11 files
```

---

<!-- _class: term -->

## Study details

```
$ tree -L 2 studies/study-ds003097
.
├── dataset_description.json
├── derivatives
│   ├── derivatives+datasets.{tsv,json}
│   ├── derivatives+subjects.{tsv,json}
│   ├── fMRIPrep-25.2.5+anat
│   ├── fMRIPrep-25.2.5+minimal
│   └── MRIQC-22.0.1
└── sourcedata
    ├── ds003097
    ├── sourcedata.{tsv,json}
    └── sourcedata+subjects.{tsv,json}

7 directories, 9 files
```

Every directory here is its own DataLad dataset. The `+` tables summarize the level below.

---

## mechababs flow

`bootstrap.sh` builds the campaign. Everything after it is `mechababs <command>`, run from inside it.

| | | |
|---|---|---|
| `bootstrap.sh` | clone the pinned babs + mechababs, build the venv, make the campaign a DataLad dataset | once |
| `configure` | bind a set of BIDS-App configs to a cluster, vendor containers, write the config and the empty ledger | once |
| `add-dataset` | register a dataset by URL — one ledger row | per dataset |
| `iterate` | **reconcile**: what's next? do it! | repeatedly |
| `status` | read-only: one row per job, across every (dataset, pipeline) cell | any time |

**`iterate` is the loop.** Everything above it is setup.

---

## Provenance capture

- Every action that makes a change goes through DataLad
- Every dataset is **clean before and after** every command
- The commits pin the exact versions of mechababs, babs, and the BIDS App
- Each job's `singularity run` is in the code, and as a `datalad run` record

---

## Gaps and problems

- How does a derivative link back to its study?
- DataLad performance degrades as more datasets are included (the clean check)
- Limited disk on the cluster
- The messy real world: how should **manual** actions outside the automation be recorded?
- Use cases need wider feedback https://github.com/con/mechababs/pull/101

---

## BIDS Study: the path to convergence

- This is where the orchestration provenance can go
- This is how multiple derivatives are connected
- BIDS lesson: standardization is how we can share tooling

---

<!-- _class: punch -->
<!-- _footer: '' -->

## BEP 028: the gaps we have already hit

> BEP028 records the **happy path**. A real campaign is not a happy path.

- **No cross-dataset reference.** BIDS-Prov's URI scheme is dataset-internal, so "this derivative's provenance continues in that study" is inexpressible. We carry W3C PROV's `Bundle` pending an answer.
- **No human in the graph.** No Person agent, no way to say what role they played, no way to say config v2 revises v1.
- **No failure.** An Activity is assumed to have produced something. There is no slot for "this run died, here is why."

**One idea:** a BEP028 PROV support library in Python.
Would need to be collaborative.

---

## nipoppy has some advantages

Battle hardened in the messy real world

- **Boutiques.** Declarative descriptors give real input validation and a config that reads cleanly. babs takes raw flag YAML with no validation at all.
- **Layouts.** Your project layout has flexibility baked into the architecture.
- **Pipeline catalog.** Retrieval and sharing of pipeline configs is STAMPED's **D** done better than "YAML in a git repo."
