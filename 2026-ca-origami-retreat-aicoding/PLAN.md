# Plan: "A few words of intro into AI assisted coding"

Slides URL: <https://datasets.datalad.org/centerforopenneuroscience/talks/2026-ca-origami-retreat-aicoding.html#/>

## Narrative Arc

1. Bridge from the YODA webinar ("where I left off") — preserving ALL digital artifacts
2. Why? Because AI can now USE all of it
3. Where are you on the AI coding maturity ladder? (orient the audience)
4. Quick walk through each ladder level
5. Introduce Claude Code as a concrete tool
6. Present the 5-stage spec-driven development loop (central thesis)
7. Map "vibe coding" vs "spec-driven" vs "compound engineering" onto that loop
8. Show the ecosystem of tools enabling this
9. Point to real AI-assisted project examples
10. Point to reusable Skills
11. Close

---

## Slide-by-Slide Plan

### S1. Title Slide (FIX existing)

- Change `<title>` and `<h2>` to: **"A few words of intro into AI assisted coding"**
- Update subtitle/description for retreat context
- Generate new QR code for `https://datasets.datalad.org/centerforopenneuroscience/talks/2026-ca-origami-retreat-aicoding.html#/`
  - Use `qrencode` CLI or similar
  - Save as `pics/2026-ca-origami-retreat-aicoding-qrcode.png`
- Update event line (from "ReproNim Webinar" to retreat name/date)
- Update the slides URL link
- Trim project logos to relevant ones (keep DataLad, DANDI; drop ReproNim, OBC, BIDS unless relevant)

### S2. Reality Check / Disclaimer (KEEP as-is)

Already good — sets expectations that this is an intro/pointers talk, not a full tutorial.

### S3. WARNING! AI Intensifies (KEEP as-is)

HBR article image — good framing for why this matters now.

### S4. "Previously on..." — ReproNim Webinar Reference (NEW — replaces TODO at line 126)

Brief slide bridging from the YODA webinar:
- Thumbnail or link to [YouTube](https://www.youtube.com/watch?v=1XbTbJ_P2x0)
- [AnnexTube mirror at t=3053](https://datasets.datalad.org/repronim/ReproTube/web/#/channel/ReproNim/video/1XbTbJ_P2x0?tab=wide=1&t=3053&q=AI&cs=1&filter=1)
- One-liner: "Where I left off — preserving ALL digital artifacts as AI-accessible knowledge base"

### S5. YODA Beyond Code & Data (KEEP as-is)

Already in the deck — the expanded YODA vision slide. Bridges nicely.

### S6. con/serve Mermaid Diagram (FILL TODO line 187)

Insert the mermaid diagram from <https://con.github.io/serve/> directly — the deck has the mermaid plugin.
Shows: INBOUND (Comms, Media, Code, AI Sessions, Pubs, Cloud) → THE VAULT (git-annex, DataLad, YODA/STAMPED, Working Surfaces) → OUTBOUND (Archives, Backup, Web Publishing).

Visually answers "how do we actually do this at scale?"

### S7. AI Coding Maturity Ladder — Overview (FILL TODO line 191)

Show `pics/borrowed/ai-ladder-skills.png` with the 5 rungs listed.
- Credit: [Jo Van Eyck "You are Not Ready: Agentic coding in 2026"](https://www.youtube.com/watch?v=6W_-YWHKwZ4)
- Prompt the audience: **"Where are you on this ladder?"**

### S8. Ladder Level 1: Chat

- Having ChatGPT/Claude open in a browser, copy-pasting code, asking questions
- Skills: basics of prompt engineering + context engineering (what to feed in, what NOT to)
- Mastery: you can write a good prompt and get decent, consistent quality output
- Time: hours to weeks
- *"Not rocket science, can pick up basics in hours but take weeks to become 'efficient'*

### S9. Ladder Level 2: Mid-Loop Generation

- LLM meets you **in your IDE** — "autocomplete on steroids"
- Type a code comment → get 1-3 alternative implementations
- Skills: evaluating alternative designs, critically selecting the best option, using types in strongly typed languages
- Time: relatively quick to pass through
- *Key: learn to critically evaluate suggestions, not just accept them*

### S10. Ladder Level 3: In-the-Loop Agentic Coding

- The **"babysitting phase"** — you actively watch the agent work
- You see it struggle, doom-loop, and you intervene
- Skills: recognizing doom loops, installing guard rails, building a prompt/skill library, extracting reusable skills & meta-prompts
- Time: **2-3 months minimum** regardless of seniority
- *"You need to see them struggle and you need to get frustrated with these struggles"*
- This is where most people should spend serious time

### S11. Ladder Level 4: On-the-Loop Agentic Coding

- You **spec the work, hand it off, go have coffee**
- Come back to high-quality artifacts, verify, move on
- Running **multiple Claude Code sessions in parallel** (each in own worktree)
- Prerequisites: all prior skills + reusable skills, MCP servers, test automation, security scanners
- *"Not a lot of people are here today"*

### S12. Ladder Level 5: Multi-Agent Coding

- The frontier — Claude Code Teams, Devin-style orchestration
- **Everyone is still figuring this out**
- *"If you have any tips, share/discuss with colleagues!"*
- **Warning**: *"If you start here without the foundations, you will shoot yourself, your organization, and your friends in the foot"*

### S13. Intro to Claude Code — What Is It? (FILL TODO line 195)

- CLI-based agentic coding tool by Anthropic (open source!)
- Works in your terminal: reads/edits files, runs commands, plans, iterates
- Key: it's an **agent**, not a chatbot — it has a loop with tools
- `CLAUDE.md` = project-level instructions / persistent memory
- Skills/commands = reusable automation patterns
- Hooks = guard rails that run automatically

### S14. Claude Code — How It Works in Practice

- Plan mode → Implementation → Review cycle
- Works with any language/framework, integrates with git
- Can show a brief example or screenshot of a session
- Mention: `@pytest.mark.ai_generated` convention for AI-written tests

### S14b. con/yolo — Sandboxed Claude Code (NEW)

Point to [con/yolo](https://github.com/con/yolo):
- Containerized (Podman) setup for running Claude Code in isolation
- Enables "YOLO mode" (permission bypass) **safely** inside a container
- Preserves your config and working directory paths — seamless compatibility with native sessions
- Great for: running agents with fewer interruptions while limiting blast radius
- Relates to ladder level 4 (on-the-loop): you need safe autonomy to let agents work unsupervised

### S15. The 5-Stage Development Loop (FILL TODO line 199) — CENTRAL THESIS

Mermaid diagram:

```
Idea → 1. Overall Design/Specification
     → 2. Aspect Design/Prompt
     → 3. AI Work (may still prompt)
     → 4. Review (inspection/tests)
     → 5. Compound/Condense into Spec
     → loop back to 2
```

Color-coded regions:
- **"Vibe coding"** = loop of 2→3→4 only (no initial spec, no condensing back)
- **"Spec-driven"** = starting from 1 (using spec-kit, OpenSpec, LAD)
- **"Compound engineering"** = doing 5 and looping back to 2 = **optimal pattern**

This is the **key insight** of the talk: each unit of work should make subsequent work easier.

### S16. Spec-Driven Tools Ecosystem (NEW, part of TODO line 199 context)

Table or list of tools enabling stages 1 and 5:

| Tool | What it does | Stage |
|------|-------------|-------|
| [spec-kit](https://github.com/github/spec-kit) | GitHub's official spec-driven dev toolkit: constitution → specify → plan → tasks → implement | 1 |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | Lightweight, tool-agnostic spec framework. Proposal/Specs/Design/Tasks artifacts | 1 |
| [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) | Claude Code plugin: plan → work → review → compound cycle | 5→2 |
| [LAD](https://github.com/chrisfoulon/LAD) (ad-hoc) | Project-specific dev guidelines adapted per repo | 1+5 |

Video reference: ["This Claude Code Plugin Transforms Vibe Coders Into Senior Engineers"](https://www.youtube.com/watch?v=IQ1_5jPiQoE)

Real example for LAD: [dandi-cli PR #1805](https://github.com/dandi/dandi-cli/pull/1805) — adapted LAD specs to project-specific practices (click CliRunner, tox, `@pytest.mark.ai_generated`)

### S17. AI-Assisted Project Examples (FILL TODO line 203)

Point to real research software built/maintained with AI assistance:
- **mykrok** — not found on GitHub (404 at con/mykrok); skipped in slides, verify URL
- **[AnnexTube](https://github.com/con/annextube)** — YouTube archival into git-annex/DataLad
- **[con/serve](https://con.github.io/serve/)** — the archival system itself
- **[citations-collector](https://github.com/con/citations-collector)** — spec-driven development example
- **[dandi-cli](https://github.com/dandi/dandi-cli)** — LAD specs, AI-generated tests

Key point: these are **real research tools**, not toy demos.

### S18. Reusable Skills (FILL TODO line 208)

Point to [con/skills](https://github.com/con/skills/) collection:
- `github-project-status` — repo health reports
- `introduce-codespell` — automated spell-checking setup
- `issue-triage` — intelligent issue analysis
- `pr-review-update` — PR management
- `tinuous-analyzer` — CI failure investigation
- `repo-hygiene`, `consolidate-dependabot-prs`, etc.

Key point: **Skills are reusable across projects** — write once, benefit everywhere. This IS stage 5 (compound/condense) in action. The more you condense your workflow into skills, the more efficient every future project becomes.

### S19. Thank You (KEEP, minor tweaks)

Already good:
- "Don't forget about YODA"
- "Let the AI agents be with you"
- YODA image

---

## Assets Needed

1. **QR code** — generate for the new URL using `qrencode -o pics/2026-ca-origami-retreat-aicoding-qrcode.png`
2. **`pics/borrowed/ai-ladder-skills.png`** — already staged in git
3. **`pics/borrowed/2026-ai-intensifies.png`** — already staged in git
4. **Mermaid diagrams** — inline in the markdown slides (plugin already loaded)
5. Possibly a **Claude Code screenshot** for the intro slides (or just describe textually)

## Guideline: Link Everything

The talk should be **informative and link-rich**. Every significant term or concept mentioned in the slides should hyperlink to its original/canonical documentation or resource. This makes the slides useful as a self-contained reference people can revisit.

Key linking targets:
- `CLAUDE.md` → https://code.claude.com/docs/en/memory
- Skills / slash commands → https://code.claude.com/docs/en/skills
- Hooks → https://code.claude.com/docs/en/hooks
- Plan mode → https://code.claude.com/docs/en/common-workflows
- MCP servers → https://code.claude.com/docs/en/mcp
- Claude Code overview → https://code.claude.com/docs/en/overview
- "not truly open source" → https://github.com/anthropics/claude-code/issues/8517
- Context engineering → https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Git worktrees → https://git-scm.com/docs/git-worktree
- Devin → https://devin.ai/
- Claude Code Teams → https://code.claude.com/docs/en/agent-teams

## Additional References / Materials

- Video: ["You are Not Ready: Agentic coding in 2026"](https://www.youtube.com/watch?v=6W_-YWHKwZ4) — ladder framework source
- Video: ["This Claude Code Plugin Transforms Vibe Coders..."](https://www.youtube.com/watch?v=IQ1_5jPiQoE) — compound engineering demo
- Article: [HBR: AI Doesn't Reduce Work, It Intensifies It](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it) — already in WARNING slide
- YODA webinar: [YouTube](https://www.youtube.com/watch?v=1XbTbJ_P2x0) | [AnnexTube](https://datasets.datalad.org/repronim/ReproTube/web/#/channel/ReproNim/video/1XbTbJ_P2x0?tab=wide=1&t=3053&q=AI&cs=1&filter=1)
- [con/serve docs](https://con.github.io/serve/) — mermaid diagram source
- [spec-kit](https://github.com/github/spec-kit), [OpenSpec](https://github.com/Fission-AI/OpenSpec), [Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [chrisfoulon/LAD](https://github.com/chrisfoulon/LAD) → [dandi-cli PR #1805](https://github.com/dandi/dandi-cli/pull/1805)
