# Render the Markdown drafts in this folder to HTML / PDF for easier reading.
#
# Tools needed:
#   pandoc                                (Debian: apt install pandoc)
# Optional, for PDF (one of):
#   xelatex / lualatex / pdflatex         (Debian: apt install texlive-xetex)
#   wkhtmltopdf                           (Debian: apt install wkhtmltopdf)
#   weasyprint                            (pip install weasyprint, or uv tool install weasyprint)
#
# Usage:
#   make                  -- builds <name>.html for every *.md in this folder
#   make pdf              -- builds <name>.pdf for every *.md (needs a PDF engine)
#   make html             -- explicit alias for the default
#   make proposal         -- just talk-proposal-draft.html + talk-proposal-draft.pdf
#   make clean            -- remove generated *.html / *.pdf
#
# Per-file targets work too, e.g.:
#   make talk-proposal-draft.html
#   make talk-proposal-draft.pdf
#   make projects-audit.html

# Inputs
MDS := $(wildcard *.md)
HTMLS := talk-proposal-draft.html  # $(MDS:.md=.html)
PDFS := talk-proposal-draft.pdf  # $(MDS:.md=.pdf)

# Pick a PDF engine that's actually on PATH.  First match wins.
PDF_ENGINE := $(firstword $(foreach e,xelatex lualatex pdflatex wkhtmltopdf weasyprint, \
                $(if $(shell command -v $(e) 2>/dev/null),$(e))))

# Pandoc options.  Title metadata is supplied per-recipe via $* so it
# expands to the stem of the file being built.
# Reader is `commonmark_x` (CommonMark + pandoc's extensions).  Neither
# `gfm` nor `commonmark_x` supports the `raw_tex` extension; for
# LaTeX-specific bits like `\newpage` we use commonmark_x's built-in
# `raw_attribute` extension instead — fence the LaTeX with
# ```{=latex} … ``` in the .md, and pandoc emits it only in the LaTeX
# output (HTML / other writers silently drop it).
PANDOC      := pandoc
PANDOC_OPTS := --standalone \
               --from commonmark_x \
               --shift-heading-level-by=0 \
               --wrap=preserve

# HTML-specific
HTML_OPTS := --to html5 \
             --embed-resources \
             --css=https://cdn.jsdelivr.net/npm/water.css@2/out/water.css

# PDF-specific (LaTeX engines).
# Margins: 0.85in all-around is tighter than the default 1in but still
# reads as "reasonable margins" per typical conference rules — gains
# ~15% page area to help fit a 1-page abstract.  Top/bottom slightly
# tighter than left/right keeps line-length comfortable.
# Colors: xcolor's default name set doesn't include "darkblue"/"darkgreen",
# and pandoc passes the linkcolor/urlcolor value directly as an xcolor
# *name* (it does not auto-recognize a bare hex string).  Define the two
# names in the preamble via header-includes, then refer to them normally.
PDF_LATEX_OPTS := --to pdf \
                  -V 'geometry=top=0.5in, bottom=0.5in, left=0.75in, right=0.75in' \
                  -V fontsize=11pt \
                  -V colorlinks=true \
                  -V linkcolor=darkgreen \
                  -V urlcolor=darkblue \
                  -V toccolor=darkgreen \
                  -V 'header-includes=\definecolor{darkblue}{HTML}{00008B}\definecolor{darkgreen}{HTML}{006400}'

# PDF via HTML (wkhtmltopdf / weasyprint) — same look as the HTML render
PDF_HTML_OPTS := --to html5 --css=https://cdn.jsdelivr.net/npm/water.css@2/out/water.css

.PHONY: all html pdf proposal clean help check

all: pdf

html: $(HTMLS)

pdf: $(PDFS)

proposal: talk-proposal-draft.html talk-proposal-draft.pdf

# Generic pattern: any.md -> any.html
%.html: %.md
	@echo "==> $@"
	$(PANDOC) $(PANDOC_OPTS) $(HTML_OPTS) \
	  --metadata title="$*" \
	  -o "$@" "$<"

# Generic pattern: any.md -> any.pdf, chosen by PDF_ENGINE
ifneq ($(filter xelatex lualatex pdflatex,$(PDF_ENGINE)),)
%.pdf: %.md
	@echo "==> $@  (engine: $(PDF_ENGINE))"
	$(PANDOC) $(PANDOC_OPTS) $(PDF_LATEX_OPTS) \
	  --metadata title="$* (CON / US-RSE'26 draft)" \
	  --pdf-engine=$(PDF_ENGINE) \
	  -o "$@" "$<"
else ifneq ($(filter wkhtmltopdf weasyprint,$(PDF_ENGINE)),)
%.pdf: %.md
	@echo "==> $@  (engine: $(PDF_ENGINE), via HTML)"
	$(PANDOC) $(PANDOC_OPTS) $(PDF_HTML_OPTS) \
	  --metadata title="$* (CON / US-RSE'26 draft)" \
	  --pdf-engine=$(PDF_ENGINE) \
	  -o "$@" "$<"
else
%.pdf: %.md
	@echo "ERROR: no PDF engine found on PATH."; \
	  echo "  Install one of: xelatex (texlive-xetex), wkhtmltopdf, weasyprint"; \
	  echo "  or run 'make html' instead."; \
	  false
endif

clean:
	rm -f $(HTMLS) $(PDFS)

check:
	@command -v $(PANDOC) >/dev/null && echo "pandoc: OK ($$($(PANDOC) --version | head -1))" \
	  || echo "pandoc: MISSING (apt install pandoc)"
	@if [ -n "$(PDF_ENGINE)" ]; then \
	   echo "PDF engine: $(PDF_ENGINE)"; \
	 else \
	   echo "PDF engine: none on PATH (xelatex / wkhtmltopdf / weasyprint)"; \
	 fi

help:
	@sed -n '1,/^# Per-file targets/p' $(firstword $(MAKEFILE_LIST)) | sed 's/^# \{0,1\}//'
