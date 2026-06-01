# Abstract

Have you ever wanted something different out of the Brain Imaging Data Structure (BIDS) standard? Dr. Yaroslav O. Halchenko (leading the Center for Open Neuroscience at PBS Department of Dartmouth College) will give the NIMH Data Science & Sharing Team's Lunch & Learn series a half-hour talk on the past&future of BIDS with a focus on the development of BIDS 2.0, the next major release of the standard. This presentation and discussion will be especially interesting to neuroimaging researchers, dataset curators, and developers of BIDS-aware tools. Attendees can expect an overview of the overarching agenda guiding BIDS 2.0 together with a tour of how the work is organized across github.com/bids-standard/ organization repositories, plus pointers on how to weigh in or contribute.

# Talk planning

## Materials

- `BIDS.bib` BibTeX export of current state of our Zotero BIDS
  bibliography (we should recommend to re-use and contribute to):
  https://www.zotero.org/groups/5111637/bids/library

- `nihpp-2309.05768v2.*` files - stored paper on The Past, Present,
  and Future of the Brain Imaging Data Structure (BIDS)

- `BIDS2.0-INCF2024-poster*` files - are downloads of
  https://docs.google.com/presentation/d/189tCRORhhn1ZzN6DmtK_Wqneui-kaoGiPXh7nzI0WGU/edit?usp=sharing
  the poster presented at INCF2024

- `` files - are downloads of
  https://docs.google.com/presentation/d/1x-LdlVGItyX6oINm8URIP5cZWBvQG6bM/edit?usp=sharing&ouid=106463979469591360865&rtpof=true&sd=true
  a talk which was given to introduce BIDS at NSF Pose meeting (so
  might be worth taking some ideas/slides for intro of BIDS), to
  read about summary of which published at (worth citing)
  https://www.cell.com/patterns/fulltext/S2666-3899(25)00164-3
  "Open-source models for development of data and metadata standards"
  https://doi.org/10.1016/j.patter.2025.101316

- github project BIDS 2.0:
  https://github.com/orgs/bids-standard/projects/10 - compilation of
  issues (primarily from bids-2-devel repository but also from
  bids-specification) to organize and reflect progress towards BIDS
  2.0

  - includes also "BIDS 3.0" column/allocation to collect
    issues/developments slated for the next 2.0

  - TODO using github API, create a script to instantiate (and later
    resync) local dump (formatted json or better yaml) with issues/PRs
    and their state

- github repository https://github.com/bids-standard/bids-2-devel/ is
  a dedicated collection of issues, many of which were moved from
  bids-specification repository as not to be addressed within 1.x
  series or BIDS

  - TODO create a script to dump here a json or yaml file with issues
    and their comments. make sure to include labels for each issue
  - TODO similarly create a script for PRs (just information from
    description with people involved etc)

- github repository
  https://github.com/bids-standard/bids-specification/ is the official
  specification repository, ATM containing BIDS 1.x series and a
  label 'bids-2.0' with a collection of PRs

  - https://github.com/bids-standard/bids-specification/pulls?q=is%3Aopen+is%3Apr+label%3Abids-2.0

   TODO: itemize list here with titles

  - also there is a 1 issue allocated with bids-2.0 label already
    about inheritance principle

  https://github.com/bids-standard/bids-specification/issues/2155

- https://github.com/bids-standard/bids-utils -- to provide commands
  such as

  - migrate -- similar to py2to3 migration to smooth out
    upgrades/deprecations.

## What is the goal behind BIDS 2.0

### Originally: ambitious

TODO: Review the IDS2.0-INCF2024-poster and summarize original goals.

### Current: realistic

(Much) smaller changes to improve e.g. consistency
(e.g. "participants.tsv" -> "subjects.tsv"; .tsv files; summarization is a MUST
not just RECOMMENDED) and get people used to `bids-utils migrate` to
automate such transitions.

Establish a better base for future extensions/developments and thus
BIDS 3.0 with potentially more drastic changes!

## What has happened already in 1.x

TODO: Expand on this stubs

- dandi-devel issue
  https://github.com/bids-standard/bids-2-devel/issues/65 was largely
  solved in docs PR
  https://github.com/bids-standard/bids-specification/pull/1834 and  against dandi

- more consistent schema / overloads in sidecar files

- BIDS DatasetType "study" to provides solution for "composition"
  (https://github.com/bids-standard/bids-2-devel/issues/59)

## Oddities of "backward compatibility" as to the standard instead of software (TODO:
  improve naming)

in software - in semver - adding a new feature is simply boost of a
minor version.  Users can use that new feature or not as they wish.

With a standard, adding a new (even optional) feature to standard, somewhat forces
tools to adopt/support it!  E.g. think about refining inheritance
principle for .tsv files (currently not well defined!).  BIDS
specification can easily issue a new .minor version but tools
developers might not even notice that and keep not implementing it.

Not really specific to BIDS!  Likely many in the audience know about
DICOMs and manufacture specific fields etc, and delayed adoption of
standardized DICOM mechanisms (e.g. apparatus for clock time sync etc)
