# BIDS 1.x deprecation / breaking-change history

Background research for the slide arguing that **BIDS 2.0 isn't the first time
we've broken things** — the 1.x line already shipped deprecations, renames,
removals, and tightenings that downstream tools had to accommodate.

Primary source: [`bids-standard/bids-specification` `src/CHANGES.md`](https://github.com/bids-standard/bids-specification/blob/master/src/CHANGES.md)
plus the live schema in `src/schema/`. Cross-referenced via PR numbers.

## Headline

**Across BIDS 1.0 → 1.11, the standard accumulated ~20 distinct
deprecations / renames / removals / behavior changes that are still observable
as `deprecated` annotations or warnings in the current schema** — plus a
handful of irreversible renames done before the "deprecation" mechanism was
formally defined (in [`bids-specification#634`](https://github.com/bids-standard/bids-specification/pull/634),
1.4.1, Oct 2020).

In other words: BIDS 1.x has already broken backward compatibility multiple
times. The difference is that those breakages were each smuggled in piecemeal
under `[FIX]` / `[ENH]` / `[MISC]` changelog tags rather than gathered into a
versioned, communicated major bump. BIDS 2.0 just bundles them properly.

## Timeline table

Pre-deprecation-mechanism: outright renames / removals (1.0.x → 1.4.0)

| Version | Date | Change | Severity | Reference |
|---|---|---|---|---|
| 1.0.0-rc3 | (pre-1.0) | Renamed `PhaseEncodingDirection` values `x`/`y`/`z` → `i`/`j`/`k` to avoid confusion with FSL | rename (semantics) | CHANGES.md §1.0.0-rc3 |
| 1.0.0-rc3 | (pre-1.0) | Renamed `SliceEncodingDirection` values `x`/`y`/`z` → `i`/`j`/`k` | rename | CHANGES.md §1.0.0-rc3 |
| 1.0.0-rc2 | (pre-1.0) | `EchoTimeDifference` replaced by `EchoTime1` + `EchoTime2` | removal + replacement | CHANGES.md §1.0.0-rc2 |
| 1.0.0-rc2 | (pre-1.0) | Removed requirement that TSV files cannot include more than two consecutive spaces | rule removal | CHANGES.md §1.0.0-rc2 |
| 1.1.1 | 2018-06-06 | Replaced `ManufacturersCapModelName` with `CapManufacturer` + `CapManufacturersModelName` (meg.json) | rename (split) | CHANGES.md §1.1.1 |
| 1.1.1 | 2018-06-06 | Removed `EEGSamplingFrequency` and `ManufacturersAmplifierModelName` from meg.json | removal | CHANGES.md §1.1.1; [`bids-specification#236`](https://github.com/bids-standard/bids-specification/pull/236) (re-removed in 1.2.1) |
| 1.2.1 | 2019-08-14 | Final removal of `ManufacturersAmplifierModelName` ("again") | removal | [`bids-specification#236`](https://github.com/bids-standard/bids-specification/pull/236) |
| 1.4.0 | 2020-06-11 | `_part-` reference dropped from example, introduced `_split-` entity | rename / scope change | [`bids-specification#460`](https://github.com/bids-standard/bids-specification/pull/460) |
| 1.4.0 | 2020-06-11 | BESA removed from list of restricted keywords for EEG coordinate systems | removal | [`bids-specification#457`](https://github.com/bids-standard/bids-specification/pull/457) |

Deprecation mechanism formalized (1.4.1+) — entries below remain
"deprecated, validators SHOULD warn" in current schema:

| Version | Date | Change | Severity | Reference |
|---|---|---|---|---|
| 1.4.1 | 2020-10-13 | Added formal definition of "DEPRECATED" requirement level (validators SHOULD warn, fields stay in schema for back-compat) | new policy mechanism | [`bids-specification#634`](https://github.com/bids-standard/bids-specification/pull/634) |
| 1.5.0 | 2021-02-23 | Anatomical MRI suffixes `T2star`, `FLASH`, `PD` deprecated — replaced by `T2starw`, `MTS`/etc. and parametric variants; added "back into schema" as `# deprecated` markers so validators recognize legacy data | renames marked deprecated | [`bids-specification#725`](https://github.com/bids-standard/bids-specification/pull/725); see [`src/schema/rules/files/raw/anat.yaml`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/rules/files/raw/anat.yaml) lines 13-15 |
| 1.6.0 | 2021-04-22 | `Unit` metadata renamed to `Units` (consistency with all other plural fields) | rename | [`bids-specification#773`](https://github.com/bids-standard/bids-specification/pull/773) |
| 1.7.0 | 2022-02-15 | `DCOffsetCorrection` (ieeg.json) deprecated — use `SoftwareFilters` instead | deprecated field | [`bids-specification#799`](https://github.com/bids-standard/bids-specification/pull/799); schema marker in `src/schema/rules/sidecars/ieeg.yaml:69` |
| 1.7.0 | 2022-02-15 | `ScanDate` (PET) deprecated in favor of `acq_time` column in scans.tsv | deprecated field | [`bids-specification#798`](https://github.com/bids-standard/bids-specification/pull/798); schema marker in `src/schema/rules/sidecars/pet.yaml:172` |
| 1.8.0 | 2022-10-29 | Introduced BIDS URIs; **dataset-relative / participant-relative path forms deprecated** for `IntendedFor`, `Sources`, `AssociatedEmptyRoom`, `BasedOn`, `RawSources` (the latter two field names themselves were also deprecated) | path semantics change + field deprecation | [`bids-specification#918`](https://github.com/bids-standard/bids-specification/pull/918); schema markers in `src/schema/objects/metadata.yaml` and `src/schema/rules/sidecars/derivatives/common_derivatives.yaml:10,40` |
| 1.8.0 | 2022-10-29 | `ElektaNeuromag` coordinate system deprecated → `NeuromagElektaMEGIN` | rename (enum value) | schema marker in `src/schema/objects/enums.yaml:27, 320`; validator check `ELEKTA_NEUROMAG_DEPRECATED` in `src/schema/rules/checks/deprecations.yml` |
| 1.8.0 | 2022-10-29 | `MISCChannelCount` (EEG, motion) deprecated → `MiscChannelCount` (camelCase fix) | rename | schema markers in `src/schema/rules/sidecars/eeg.yaml:74`, `motion.yaml:65` |
| 1.9.0 | 2023-11-20 | `atlas` entity removed and replaced with `seg` (in prep for BEP038) | removal + rename | [`bids-specification#1579`](https://github.com/bids-standard/bids-specification/pull/1579) |
| 1.9.0 | 2023-11-20 | `channels.tsv` column `orientation_component` renamed → `component` | rename | [`bids-specification#1417`](https://github.com/bids-standard/bids-specification/pull/1417) |
| 1.9.0 | 2023-11-20 | `index` definition reverted to non-negative (permitting zero) — earlier 1.4.1 had made it nonnegative integer; numerical semantics churn | behavior change | [`bids-specification#1482`](https://github.com/bids-standard/bids-specification/pull/1482) cf. [`#535`](https://github.com/bids-standard/bids-specification/pull/535), [`#578`](https://github.com/bids-standard/bids-specification/pull/578), [`#590`](https://github.com/bids-standard/bids-specification/pull/590) |
| 1.10.1 | 2025-09-03 | `"89+"` string for default `age` column deprecated; columns get richer typing in sidecars | deprecated value | [`bids-specification#2162`](https://github.com/bids-standard/bids-specification/pull/2162); schema marker in `src/schema/objects/columns.yaml:44` |
| 1.10.1 | 2025-09-03 | Inheritance Principle: **value overloading** flagged as discouraged, with explicit plan to deprecate in BIDS 2.0 | behavior change (forward-deprecation) | [`bids-specification#1834`](https://github.com/bids-standard/bids-specification/pull/1834) |
| 1.11.0 | 2026-02-04 | (Implicit) `phase` suffix in func/ already deprecated in favor of `part-phase` + `bold`; reaffirmed in schema | deprecated suffix | schema markers in `src/schema/rules/files/raw/func.yaml:30`, `src/schema/rules/checks/func.yaml:5` (`PHASE_SUFFIX_DEPRECATED`); see also derivatives `imaging.yaml:240` |
| (various) | (various) | `HardcopyDeviceSoftwareVersion` (MRI sidecar) carried forward as deprecated | deprecated field | schema marker in `src/schema/rules/sidecars/mri.yaml:39` |

### Items that look like deprecations but aren't (in the strict sense)

- The 1.4.0 / 1.6.0 schema introduction itself was **not** a deprecation of
  prose-defined behavior — but it did force every downstream
  tool to track a new YAML-based format. PRs around the schema sprint
  ([`bids-specification#1075`](https://github.com/bids-standard/bids-specification/pull/1075),
  [`#1078`](https://github.com/bids-standard/bids-specification/pull/1078) etc.)
  amount to a *de facto* format switch even though they were not labelled as
  breaking.
- Numerous "clarifications" (e.g. [`#1116`](https://github.com/bids-standard/bids-specification/pull/1116)
  no blank/duplicate TSV headers; [`#927`](https://github.com/bids-standard/bids-specification/pull/927)
  EDF/BDF extensions MUST be lowercase) functionally tightened previously
  permissive validators. Not formally deprecations, but datasets that were
  valid pre-clarification can fail post-clarification.

## Themes the slide can highlight

### 1. Field renames — the most common breakage pattern
Renaming a JSON key is technically a breaking change for any consumer that
keys off the old name. 1.x did this repeatedly:
- `Unit` → `Units` (1.6.0, [`#773`](https://github.com/bids-standard/bids-specification/pull/773))
- `ManufacturersCapModelName` → `CapManufacturer` + `CapManufacturersModelName` (1.1.1)
- `EchoTimeDifference` → `EchoTime1`/`EchoTime2` (1.0.0-rc2)
- `ElektaNeuromag` → `NeuromagElektaMEGIN` (1.8.0)
- `MISCChannelCount` → `MiscChannelCount` (1.8.0)
- `orientation_component` → `component` in channels.tsv (1.9.0,
  [`#1417`](https://github.com/bids-standard/bids-specification/pull/1417))
- `atlas` entity → `seg` (1.9.0, [`#1579`](https://github.com/bids-standard/bids-specification/pull/1579))
- Anatomical suffixes: `T2star`/`FLASH`/`PD` → `T2starw`/parametric variants (1.5.0, [`#725`](https://github.com/bids-standard/bids-specification/pull/725))

### 2. Semantic / format swaps under a stable field name
The same key, but the value-space changed:
- `PhaseEncodingDirection` and `SliceEncodingDirection` values: `x`/`y`/`z` → `i`/`j`/`k` (1.0.0-rc3) — the same string now means a different axis convention.
- BIDS URIs (1.8.0, [`#918`](https://github.com/bids-standard/bids-specification/pull/918)) deprecated raw-relative paths in `IntendedFor`, `Sources`, `AssociatedEmptyRoom`. Consumers expecting only POSIX-ish paths must now also handle `bids::sub-…` URIs.
- `index` numeric semantics churn (1.4.1 → 1.9.0): is `0` a valid run index? The answer changed twice ([`#535`](https://github.com/bids-standard/bids-specification/pull/535) / [`#590`](https://github.com/bids-standard/bids-specification/pull/590) / [`#1482`](https://github.com/bids-standard/bids-specification/pull/1482)).

### 3. Schema-format swap (de facto major change)
The migration from prose-defined rules to YAML schema (rolled out from ~1.6.0
through 1.7.0/1.8.0 schema sprints, [`#1075`](https://github.com/bids-standard/bids-specification/pull/1075),
[`#919`](https://github.com/bids-standard/bids-specification/pull/919))
re-grounded every downstream validator and tool. No `[BREAKING]` tag, but
arguably the largest infrastructural break of 1.x. Metaschema landed in 1.10.0
([`#1787`](https://github.com/bids-standard/bids-specification/pull/1787)).

### 4. Deprecation as a permanent feature
The 1.4.1 "DEPRECATED" definition ([`#634`](https://github.com/bids-standard/bids-specification/pull/634))
created a *category* of permanently-warned fields. The schema today carries
**at least 9 fields, 3 enum/suffix values, and 1 column value at
`level: deprecated`** — every one of these is a backward-compat shim for a
real change that already happened in 1.x. A clean 2.0 lets us drop these
shims.

### 5. MAY → SHOULD / RECOMMENDED tightenings
Less load-bearing but cumulatively important:
- `dataset_description.Authors` made RECOMMENDED in 1.7.0 ([`#1092`](https://github.com/bids-standard/bids-specification/pull/1092))
- `electrodes.tsv` clarified as REQUIRED for iEEG in 1.10.1 ([`#1896`](https://github.com/bids-standard/bids-specification/pull/1896))
- `recording` entity made REQUIRED for pet/blood ([`#1005`](https://github.com/bids-standard/bids-specification/pull/1005), 1.7.0)
- `events.tsv` MUST be sorted by onset in 1.10.0 ([`#1732`](https://github.com/bids-standard/bids-specification/pull/1732))
- DOI values SHOULD now be fully specified URIs; bare DOIs deprecated (see common-principles.md)

Each of these can fail a previously-valid dataset under a strict validator.

## Talk-ready one-liner

> "BIDS has effectively been making breaking changes for years — across 1.x
> we already renamed or deprecated ~20 fields, suffixes and value
> conventions, and shipped a parallel YAML-schema rewrite of the spec.
> The current schema still carries ~9 deprecated metadata fields, 3
> deprecated suffixes/enum values, and a deprecated column value as
> permanent backward-compat shims. BIDS 2.0 isn't the first break — it's
> the first one we get to *name*, *batch*, and *clean up after*."

## Caveats / gaps

- The changelog after the 1.4.1 "deprecation" formalization is fairly explicit
  about deprecations. Pre-1.4.1 entries (notably 1.0.x-rc series and 1.1.1) are
  terse one-liners; we're trusting the changelog summary as the source of
  truth and not chasing every PR.
- `[FIX]` entries that "clarify" pre-existing behavior are not counted in the
  ~20 count above unless the clarification demonstrably narrowed
  previously-valid input (a few are listed under Theme 5 as illustrative, not
  exhaustive).
- Some deprecations were per-modality replicas of a single decision (e.g.
  `MISCChannelCount` in both EEG and motion sidecars). Counted as one
  decision, two schema sites.
