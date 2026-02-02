# Proposed Slide Structure & Narrative Arc

## Act I: The YODA Foundation (Keep & Enhance)
*Current slides work well - minor enhancements*

1. **Title Slide** ✓ (already updated)
2. **YODA Principles Overview** ✓ (keep as-is)
3. **NEW: Evolution of YODA**
   - From "research data organization" (2018) → "comprehensive digital material management" (2026)
   - Beyond code/data: bash history, zoom recordings, meeting notes, experimental stimuli
   - Theme: *"If it's digital and matters, version control it shall be"*

## Act II: YODA Meets Real-World Workflows (Expand)
*Connect YODA principles to ReproFlow ecosystem*

4. **Principle 1: Version Control** ✓ (keep current content)
   - Add: `con/duct` for execution tracing → *observability as provenance*
   - Add: `tinuous` for CI logs → even build artifacts become referenceable

5. **NEW: Beyond Code - The Unrealized YODA**
   - Bash history capture in datasets
   - Zoom/Teams recordings as subdatasets
   - Lab meeting notes, presentations (this very slide deck!)
   - ReproStim: video capture of actual stimuli shown
   - Theme: *"Capture you must what actually happened, not what should have"*

6. **Principle 2: Portable Environments** ✓ (keep)
   - Enhance with ReproMan for orchestrating across HPC/cloud

7. **Principle 3: Modular Composition** ✓ (keep core)
   - **EXPAND significantly**: This is where BIDS comes in

## Act III: Hierarchical Composition - BIDS as YODA Exemplar (NEW)
*The breakthrough insight: BIDS is YODA at scale*

8. **NEW: BIDS Studies as Composed Datasets**
   ```
   study/
   ├── sub-01/  (subdataset - raw data)
   ├── sub-02/  (subdataset)
   ├── derivatives/
   │   ├── mriqc/  (subdataset - QC results)
   │   ├── fmriprep/  (subdataset - preprocessed)
   │   └── analysis-smith2025/  (subdataset - paper)
   └── code/  (stimuli, protocols)
   ```
   - Each level knows only what's below
   - "Do not look up" enables independent reuse

9. **NEW: Real Examples - OpenNeuroDerivatives**
   - Show the actual structure (you have slides for this already around line 718)
   - Highlight: ReproMan job specs capture *how* each derivative was created
   - Each derivative = independent dataset but composed into study

10. **NEW: From ReproIn to ReproFlow**
    - **ReproIn**: MRI scanner → BIDS (automated)
    - **ReproStim**: Capture actual stimuli presented
    - **ReproMon**: Monitor acquisition in real-time
    - **ReproMan**: Run processing pipelines
    - **con/duct**: Trace execution details
    - **tinuous**: Capture CI/CD artifacts
    - Full provenance chain: scanner → preprocessing → analysis → paper

## Act IV: The AI Frontier - Structure Enables Intelligence (NEW)
*This is the novel contribution for ReproNim audience*

11. **NEW: The Problem with Unstructured "RAG"**
    - LLMs hallucinate
    - Web content disappears
    - No version control of sources
    - No provenance
    - Image: *"Depends on untracked web"* meme

12. **NEW: Structured Collections as AI Substrate**
    - **BIDS datasets** → AI can learn cross-study patterns
    - **DataLad-Registry** → 10,000+ datasets with metadata
    - **OpenNeuroStudies** → Aggregated structured knowledge
    - But: Structure preserved, provenance intact

13. **NEW: Condensed Frontiers with Deep Links**
    ```
    study-summary/  (AI-generated, version controlled)
    ├── README.md  (NotebookLM summary)
    ├── key-findings.md
    ├── anomalies-detected.md
    └── .datalad/
        └── config  (links to full subdatasets)
    ```
    - AI tools (NotebookLM, Claude, etc.) generate *summaries*
    - Summaries are version controlled
    - Links to source subdatasets preserved
    - Can always drill down to raw data
    - Theme: *"Surface you create, depth you preserve"*

14. **NEW: Observability → Insight**
    - `duct` traces + LLM analysis = "Why did this fail?"
    - Bash history + code = "What actually ran?"
    - Zoom recordings + meeting notes = "What was decided?"
    - All timestamped, all linked, all version controlled

15. **NEW: Agentic Workflows on YODA**
    - AI agents can:
      - Traverse subdatasets programmatically
      - Generate derivative summaries
      - Detect anomalies across studies
      - Propose new analyses
    - But: Always within YODA structure
    - Agents don't replace structure, they leverage it
    - Example: `datalad run --agent=claude "Summarize QC failures across all subjects"`

## Act V: The Vision (NEW)

16. **NEW: Every Lab, A YODA**
    - Lab notebook → DataLad dataset
    - Weekly meetings → Zoom recording subdataset + notes
    - Every experiment → BIDS + ReproStim stimuli
    - Every analysis → `datalad run` with `con/duct`
    - Every paper → Subdataset linking to all of above

17. **NEW: OpenNeuro-Scale Insights**
    - When 1000 studies share structure:
      - Cross-study meta-analysis becomes `datalad get` + `pandas merge`
      - AI can learn "what normal looks like"
      - Outliers auto-detected
      - Replication attempts auto-verified
    - But: No centralization required
    - Each dataset remains independent, composable module

18. **Take Home Messages** (Enhanced)
    - YODA isn't just for data - it's for *everything digital*
    - Structure doesn't constrain - it enables
    - AI tools amplify structured collections, don't replace them
    - Observability + reproducibility = trustworthy science
    - Start small: version control your next meeting notes

## New Slides to Create

1. **Evolution of YODA slide** - timeline graphic
2. **Unrealized YODA slide** - examples of digital artifacts we should capture
3. **BIDS as YODA slide** - show hierarchy with "do not look up" arrows
4. **ReproFlow ecosystem diagram** - all components connected
5. **AI on unstructured vs structured slide** - contrasting approaches
6. **Condensed frontiers diagram** - show AI summary layer with links down
7. **Agentic workflows slide** - example commands
8. **Vision slide** - "Every Lab, A YODA" graphic

## Suggested Deletions/Condensations

- Keep but condense: detailed git-annex stats (slide ~325) - just mention briefly
- Keep but reduce: container families details (slide ~469) - focus on ReproNim/containers
- Merge: some datalad-run examples are repetitive
