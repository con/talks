# Completing the STAMPED in Practice poster

The poster is the target argument for the study, with real example results and open comparison slots.
Its purpose is to help choose the evidence to collect, not to report a moving progress total.
The underlying data exports retain timestamps and hashes for reproducibility.

## The argument to complete

We iteratively improve research skills by testing the scientific work they produce.
A versioned research object lets others inspect both the scientific result and the process that changed the skills.
The completed poster should establish which revisions improved scientific adequacy, reproducibility and consistency, show costs and adverse outcomes, and invite new studies that test transfer.
An improved result is an empirical question, not an assumed conclusion.

| Poster element | Present now | Evidence needed to finish |
| --- | --- | --- |
| Scientific case | NARPS H1; 54 fixed AO86 participant gain-effect maps; linked paper, task and data | Confirm the scientific panel is the intended scope of reproduction: group inference from supplied contrasts |
| Group maps and condensed result | Run 09 maps, correction, regional coefficient and CI, generated from archived artifacts | Choose the final illustrative analysis by a stated rule; keep its exact source revision and inference details |
| Variability across conditions | Individual native mask sizes and corrected positive voxel counts from eight completed runs | Extract all allocated runs and iterations; preserve native method choices; show points and ranges |
| Checked outcomes | All 36 allocated runs have slots; available primary judgments populate science, replay and checklist counts | Finish and bind all 36 primary and 12 assigned duplicate judgments; preserve item-level validity and disagreement |
| Iterative improvement | Revision 1 is pinned; two change-to-retest slots | For each revision, link the observed failure, reusable change, and next-round outcome; final round receives no further tuning |
| Evidence and reuse | Links to skills, inputs, source, outputs, plans and figure code | Finish registering and publishing the research objects and assessment evidence; verify a recipient can retrieve each required payload |
| Invitation | Use STAMPED; try the skills; contribute a hypothesis, data and reference result | Select the next studies with researchers at the conference |

## Continue the experiment; add a consistent extraction layer

The registered [comparison plan](https://github.com/leej3/stamped-in-practice/blob/main/comparison-plan.md) already covers scientific adequacy, checklist attainment, operational outcomes, effort and descriptive variability.
These poster requirements do not by themselves require a restart.
Freeze a versioned secondary extraction specification, extract from stopped-worker artifacts, and leave the original work intact.
Record round-one additions as retrospective; apply the same specification to later rounds.

The existing native mask/count figure shows analytic variation, including the choice of Bonferroni or permutation correction.
It is not an estimate of the effect of an assistance strategy, and different native regions should not be pooled as a single vmPFC effect.
A fixed-region mean recomputed from the same 54 input maps would be identical across conditions by construction.
That would be a useful reference value, but an uninformative comparison of the assistance conditions.

A useful additional spatial endpoint is **pairwise agreement of corrected positive maps on common evaluation support**, reported within each condition and iteration:

1. Verify image geometry, coordinate system and map semantics; do not mix effect, t, z or p maps.
2. Retain each worker's native search mask and corrected positive map, with method, family and alpha.
3. Define the evaluation support independently of the desired result, documenting its anatomical source and coverage rule.
Retain both common-support size and native-support size, plus each run’s coverage fraction.
Voxels outside a native search mask are unassessed, not negative.
4. Compute full-domain Dice only when both runs assessed the evaluation domain.
Otherwise mark it unavailable or report a separately labeled pair-specific intersection and its size.
On the declared support, compute pairwise Dice overlap of corrected positive maps and positive voxel counts.
Record both-empty maps explicitly; do not silently assign perfect agreement to an empty denominator.
5. Show all three pairwise comparisons for three runs, with run IDs and method labels.
Treat agreement as descriptive; a common mistake can also produce agreement.

If all agents produce identical effect or t fields on shared support, report that null variation.
Do not manufacture variation by changing the endpoint after seeing the result.
Scientific adequacy, coverage choices and reproducibility can still differ.

## Collect one bound record per run

Retain a machine-readable record linking these fields to immutable artifact hashes and public or declared recipient URLs:

| Record | Required fields |
| --- | --- |
| Assignment | study, iteration, run ID, condition, replicate, input revision, worker stop commit, skill revision, model/settings |
| Actual skill exposure | discovered, installed and used skills; versions; unsuccessful attempts; evidence |
| Scientific result | participant IDs/exclusions, model/design/weights, effect units, native region, effect/statistic maps, coverage/search mask, spatial reference, correction family/method/alpha, permutations/seed, hypothesis conclusion |
| Native estimate | effect, interval and interval method; corrected regional and whole-brain positive voxels; native mask/region sizes |
| Assessment | judgment ID/role, assessor/procedure revision, adequacy, every checklist item, validity overrides and missing reasons |
| Replay | entry point, generated-output manifest, input hashes before/after, candidate outputs, exact/numerical comparison per file, missing outputs, scope and elapsed time |
| Delivery and effort | worker delivery, coordinator preservation, independent retrieval, intervention, worker elapsed time and measured costs with their scope |
| Secondary extraction | specification/code version, source hashes, evaluation support, alignment, metric/value/units and missing reason |

Do not make publication of an artifact or coordinator recovery count as worker delivery success.
Keep duplicate and supplementary judgments separate from the first assigned primary.

## Repair measurement collection, not the scientific record

The measurement disposition retains first-assigned judgments and marks infrastructure-affected measures unavailable.
The current aggregation scripts and documentation still need to be reconciled with that disposition; an older aggregation rule would exclude original primaries.
Preserve raw item verdicts and their external validity overlays instead of replacing historical grades.

For future replay collection, distinguish generated outputs from inputs and authored reports.
An output manifest plus an input-hash guard prevents the replay tool from deleting a required input.
Define file-specific comparisons before evaluation: numerical arrays can have a declared tolerance; timestamps and authored prose need an explicit policy.
Run 09 illustrates why this matters: 12 of 14 candidate files were byte-identical, the JSON timestamp changed, and the report was not regenerated.

These fixes need versioned assessment procedures and consistent interpretation across comparisons.
They do not justify selecting a more favorable reassessment as the primary.
Keep assessor amendments visible in the machine-readable results and stratify affected measures where necessary.

## When a new comparison is needed

Start a newly registered comparison if the desired poster requires a different scientific task, a mandatory common model/region, participant-level preprocessing, substantive changes to worker instructions, or a new primary assessment definition that cannot be applied comparably to existing objects.
That is a design decision to make before launching affected workers.
A new comparison should preserve and link the current study as evidence that motivated it, rather than discard it.

## Finish the poster from the records

1. Publish and bind each completed run, assessment and payload retrieval receipt.
2. Refresh the assessment export and figure inputs from those exact revisions.
3. Extend the variability figure by iteration using the extraction specification.
4. Replace the two revision slots with the actual changes and their subsequent outcomes.
5. Add a concise comparison result supported by the completed matrix, including null or adverse findings.
6. Rebuild the PDF, inspect its layout, and verify links and QR codes.

The current figure inputs and assessment export are reproducible saved data, not promises that the later result slots have been measured.
