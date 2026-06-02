# SPDX-FileCopyrightText: 2026 Yaroslav Halchenko <yaroslav.o.halchenko@dartmouth.edu>
# SPDX-License-Identifier: MIT
#
# Fetch BIDS 2.0 development state from GitHub into data/ as YAML so the
# presentation in this directory can summarise it offline.
#
# Requirements:
#   - Python 3.10+ with PyYAML installed (pip install pyyaml)
#   - GitHub CLI `gh` authenticated (`gh auth login`) or GH_TOKEN exported.
#     For Project #10 you need read:project scope (classic PAT) or
#     the fine-grained PAT "Projects" permission (Read).

PYTHON      ?= python3
SCRIPTS      = scripts
DATA         = data
ORG          = bids-standard
PROJECT_NUM  = 10

.PHONY: sync sync-bids-2-devel sync-bids-spec sync-project clean help

sync: sync-bids-2-devel sync-bids-spec sync-project
	@date -u +"%Y-%m-%dT%H:%M:%SZ" > $(DATA)/fetched-at.txt
	@echo "Sync complete at $$(cat $(DATA)/fetched-at.txt)"

sync-bids-2-devel:
	$(PYTHON) $(SCRIPTS)/fetch_repo.py $(ORG)/bids-2-devel $(DATA)/bids-2-devel

sync-bids-spec:
	$(PYTHON) $(SCRIPTS)/fetch_repo.py $(ORG)/bids-specification \
	    $(DATA)/bids-specification --label bids-2.0

sync-project:
	$(PYTHON) $(SCRIPTS)/fetch_project.py $(ORG) $(PROJECT_NUM) \
	    $(DATA)/project-$(PROJECT_NUM)/items.yaml

clean:
	rm -rf $(DATA)

help:
	@echo "Targets:"
	@echo "  sync               (default) fetch everything"
	@echo "  sync-bids-2-devel  fetch issues+PRs from bids-2-devel"
	@echo "  sync-bids-spec     fetch label:bids-2.0 issues+PRs from bids-specification"
	@echo "  sync-project       fetch GitHub Project #$(PROJECT_NUM) items"
	@echo "  clean              remove data/"
