.DEFAULT_GOAL := help

PYTHON ?= python3
PROJECT_NAME ?= Untitled Project
ENGINE ?= godot-4
ENGINE_VERSION ?= TBD
PLATFORM ?= pc-premium
GENRE ?= action-roguelite
TASK ?= Investigate controller aim drift
FEATURE ?= Example Feature
BUG ?= Example Bug
QA_TITLE ?= Example Feature
EVAL_TITLE ?= Example Eval

help: ## Show common repo commands
	@grep -E '^[a-zA-Z0-9_.-]+:.*## ' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*## "}; {printf "%-16s %s\n", $$1, $$2}'

studio: ## Open the front-door Codex Studio CLI
	$(PYTHON) scripts/codex_studio.py

start: ## Guided interactive setup for a new game repo
	$(PYTHON) scripts/start_game_studio.py

setup: ## Bootstrap docs, install hooks when possible, and run checks
	$(PYTHON) scripts/setup_repo.py --project-name "$(PROJECT_NAME)" --engine "$(ENGINE)" --engine-version "$(ENGINE_VERSION)" --platform "$(PLATFORM)" --genre "$(GENRE)"

baseline: ## Seed active docs with a concrete project baseline
	$(PYTHON) scripts/seed_project_baseline.py --project-name "$(PROJECT_NAME)" --engine "$(ENGINE)" --engine-version "$(ENGINE_VERSION)" --platform "$(PLATFORM)" --genre "$(GENRE)"

doctor: ## Run local tooling and repo health checks
	$(PYTHON) scripts/doctor.py

ci-local: ## Run the local CI-equivalent checks
	$(PYTHON) -m compileall -q scripts docs studio evals tests
	$(PYTHON) scripts/doctor.py
	$(PYTHON) scripts/validate_engine_kits.py
	$(PYTHON) scripts/run_local_evals.py
	$(PYTHON) scripts/godot_smoke.py --static-only
	$(PYTHON) -m pytest -q tests
	$(PYTHON) scripts/validate_repo_layout.py
	$(PYTHON) scripts/validate_docs.py
	$(PYTHON) scripts/validate_assets.py

validate: ## Run layout, docs, and asset validation
	$(PYTHON) scripts/validate_engine_kits.py
	$(PYTHON) scripts/godot_smoke.py --static-only
	$(PYTHON) scripts/validate_repo_layout.py
	$(PYTHON) scripts/validate_docs.py
	$(PYTHON) scripts/validate_assets.py

test: ## Run the automated repo tests
	$(PYTHON) -m pytest -q tests

godot-smoke: ## Run static Godot smoke checks and runtime smoke if Godot is installed
	$(PYTHON) scripts/godot_smoke.py

godot-smoke-strict: ## Require a local Godot binary for the smoke check
	$(PYTHON) scripts/godot_smoke.py --require-engine

export-linux: ## Export the Godot build using the Linux/X11 preset
	$(PYTHON) scripts/godot_export.py --preset "Linux/X11"

export-windows: ## Export the Godot build using the Windows Desktop preset
	$(PYTHON) scripts/godot_export.py --preset "Windows Desktop"

status: ## Print studio status
	$(PYTHON) scripts/studio_status.py

bootstrap: ## Re/bootstrap active docs using the selected presets
	$(PYTHON) scripts/bootstrap_studio.py --project-name "$(PROJECT_NAME)" --engine "$(ENGINE)" --engine-version "$(ENGINE_VERSION)" --platform "$(PLATFORM)" --genre "$(GENRE)"

hooks: ## Install git hooks into .git/hooks
	./scripts/install_git_hooks.sh

radar: ## Scan the repo for the highest-impact structural gaps
	$(PYTHON) scripts/project_radar.py --warn-only

route: ## Route a task description to likely skills, agents, and docs
	$(PYTHON) scripts/route_task.py "$(TASK)"

checklist: ## Resolve the layered checklist bundle for a task
	$(PYTHON) scripts/codex_studio.py checklist --task "$(TASK)"

research: ## Scaffold a research note inside the knowledge base
	$(PYTHON) scripts/codex_studio.py research --category systems --title "$(EVAL_TITLE)"

engine-kits: ## Validate all starter-kit manifests and scaffold markers
	$(PYTHON) scripts/validate_engine_kits.py

unity-test-command: ## Print the Unity test command for the starter-kit scaffold
	$(PYTHON) scripts/unity_adapter.py test --project-path studio/starter-kits/unity-6/scaffold --unity-path /Applications/Unity/Hub/Editor/6000.0.0f1/Unity --dry-run --json

unity-build-command: ## Print the Unity build command for the starter-kit scaffold
	$(PYTHON) scripts/unity_adapter.py build --project-path studio/starter-kits/unity-6/scaffold --unity-path /Applications/Unity/Hub/Editor/6000.0.0f1/Unity --dry-run --json

unreal-package-command: ## Print the Unreal package command for the starter-kit scaffold
	$(PYTHON) scripts/unreal_adapter.py package --project-path studio/starter-kits/unreal-5/scaffold --uat-path /Applications/Epic/UE_5.5/Engine/Build/BatchFiles/RunUAT.sh --dry-run --json

feature: ## Scaffold a feature brief, ADR, and test plan
	$(PYTHON) scripts/scaffold_feature.py "$(FEATURE)" --with-adr --with-test-plan

bug: ## Scaffold bug triage docs
	$(PYTHON) scripts/scaffold_bugfix.py "$(BUG)"

qa: ## Generate a lightweight QA matrix
	$(PYTHON) scripts/generate_qa_matrix.py "$(QA_TITLE)"

eval: ## Scaffold an eval plan for behavior or instruction changes
	$(PYTHON) scripts/scaffold_eval_plan.py "$(EVAL_TITLE)"

evals: ## Run the local eval corpus
	$(PYTHON) scripts/run_local_evals.py

hooks-enable: ## Enable optional Codex hooks in .codex/config.toml
	$(PYTHON) scripts/toggle_codex_hooks.py --enable

hooks-disable: ## Disable optional Codex hooks in .codex/config.toml
	$(PYTHON) scripts/toggle_codex_hooks.py --disable

docker-build: ## Build the optional helper container
	docker compose build

docker-shell: ## Open a shell in the optional helper container
	docker compose run --rm app

docker-verify: ## Build the helper container and run a smoke import check
	docker compose build
	docker compose run --rm app python -c "import requests, numpy, pandas, dotenv; print('docker-ok')"
