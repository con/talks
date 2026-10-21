# Co-presenter materials for 2026-reproAI-MIT-STAMPED
# Scaffolded for docflow -- https://github.com/con/docflow
#
# WHAT THIS DOES
#   Syncs the workshop's shared Google Drive folder into materials/,
#   commits it to git-annex (never to git -- see .gitattributes), and tags
#   every synced key with the git-annex metadata field
#   distribution-restrictions=3rd-party.
#
# WHY THE METADATA MATTERS
#   Both public siblings of this dataset already carry the preferred-content
#   expression  (not metadata=distribution-restrictions=*)  -- verify with
#   `make check-publish`.  So `datalad push` (which defaults to --data auto,
#   i.e. git annex copy --auto) will not copy tagged content to
#   datasets.datalad.org or hub-con.  The files stay here; only the annex
#   pointers -- and therefore the file names -- travel.  That is accepted:
#   names public, bytes not.
#
# SETUP
#   Uses the existing `gdrive:` rclone remote.  Nothing to configure, but
#   check that the path resolves before the first sync:
#
#       make probe
#
#   If the folder lives in "Shared with me" rather than under your own
#   Drive tree, rclone needs an extra flag and a shorter path; `make probe`
#   tries both and tells you which one worked.  Then set, if needed:
#
#       make sync RCLONE_OPTS=--drive-shared-with-me GDRIVE_REMOTE='gdrive:LLMs @ MIT: October 2026/'

GDRIVE_REMOTE := gdrive:ReproNim/LLMs @ MIT: October 2026/
GDRIVE_LOCAL  := materials/
RCLONE_OPTS   :=
RESTRICTION   := 3rd-party
PUBLIC_REMOTES := datasets.datalad.org hub-con

# Google-native files have to be exported to something; Slides -> pptx.
EXPORT_FORMATS := pptx,docx,xlsx,pdf,svg

.PHONY: probe sync fetch restrict save check-publish status clean help
.DEFAULT_GOAL := help

## probe: check that the Drive path resolves (run this before the first sync)
probe:
	@echo "--- as a path in your own Drive tree:"
	@rclone lsf $(RCLONE_OPTS) "$(GDRIVE_REMOTE)" && echo "  OK -- use as is" || \
		echo "  failed"
	@echo "--- as a shared-with-me folder:"
	@rclone lsf --drive-shared-with-me "gdrive:LLMs @ MIT: October 2026/" && \
		echo "  OK -- re-run with RCLONE_OPTS=--drive-shared-with-me and the shorter GDRIVE_REMOTE" || \
		echo "  failed"

## sync: fetch from Drive, commit to annex, then tag as third-party
sync: fetch save restrict check-publish

## fetch: rclone sync only (no git operations)
fetch:
	@mkdir -p "$(GDRIVE_LOCAL)"
	rclone sync -P $(RCLONE_OPTS) --drive-export-formats $(EXPORT_FORMATS) \
		"$(GDRIVE_REMOTE)" "$(GDRIVE_LOCAL)"

## save: commit whatever is in materials/ (goes to annex per .gitattributes)
save:
	datalad save -m "materials: sync co-presenter materials from Google Drive" "$(GDRIVE_LOCAL)"

## restrict: tag every annexed file under materials/ as third-party
restrict:
	git annex metadata --set distribution-restrictions=$(RESTRICTION) "$(GDRIVE_LOCAL)"
	@echo "--- tagged:"
	@git annex find --metadata distribution-restrictions=$(RESTRICTION) "$(GDRIVE_LOCAL)" || true

## check-publish: assert restricted content is not wanted by, or present on, public siblings
check-publish:
	@for r in $(PUBLIC_REMOTES); do \
		w="$$(git annex wanted $$r 2>/dev/null)"; \
		printf '%-24s wanted: %s\n' "$$r" "$${w:-<unset -- FIX: see below>}"; \
		case "$$w" in \
			*distribution-restrictions*) ;; \
			*) echo "  !! run: git annex wanted $$r 'not metadata=distribution-restrictions=*'" ;; \
		esac; \
	done
	@echo "--- restricted content present on a public sibling (must be empty):"
	@for r in $(PUBLIC_REMOTES); do \
		git annex find --in="$$r" --metadata distribution-restrictions='*' 2>/dev/null \
			| sed "s|^|  $$r: |" || true; \
	done
	@echo "--- done"

## status: what is here, and what is restricted
status:
	@echo "--- untagged annexed files under $(GDRIVE_LOCAL) (should be empty after 'make restrict'):"
	@git annex find --not --metadata distribution-restrictions='*' "$(GDRIVE_LOCAL)" 2>/dev/null || true
	@echo "--- metadata:"
	@git annex metadata "$(GDRIVE_LOCAL)" 2>/dev/null || true

## clean: drop local content (keeps the annex pointers and the metadata)
clean:
	@echo "This drops LOCAL CONTENT of third-party materials, which has no other copy."
	@echo "Re-run 'make sync' to get it back from Drive.  Ctrl-C to abort."
	@printf 'Type yes to proceed: ' && read a && [ "$$a" = yes ]
	git annex drop --force "$(GDRIVE_LOCAL)"

help:
	@echo "Targets:"
	@sed -n 's/^## /  /p' $(MAKEFILE_LIST)
	@echo ""
	@echo "Remote: $(GDRIVE_REMOTE)  ->  $(GDRIVE_LOCAL)"
	@echo "Start with 'make probe'."
