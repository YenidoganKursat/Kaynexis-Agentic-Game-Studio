.DEFAULT_GOAL := help

PYTHON ?= python3

help: ## Show available commands
	@grep -E '^[a-zA-Z0-9_.-]+:.*## ' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*## "}; {printf "%-18s %s\n", $$1, $$2}'

validate: ## Run the static project validation
	$(PYTHON) scripts/godot_smoke.py --static-only

test: ## Run the automated tests
	$(PYTHON) -m pytest -q tests/test_godot_surface.py

smoke: ## Run static checks and runtime smoke when Godot is available
	$(PYTHON) scripts/godot_smoke.py

export-linux: ## Export the Linux build
	$(PYTHON) scripts/godot_export.py --preset "Linux/X11"

export-windows: ## Export the Windows build
	$(PYTHON) scripts/godot_export.py --preset "Windows Desktop"
