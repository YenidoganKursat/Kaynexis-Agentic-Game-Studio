.DEFAULT_GOAL := help

PYTHON ?= python3
PROJECT_NAME ?= Codex Game Studio Pro Max
ENGINE ?= godot-4
ENGINE_VERSION ?= 4.x
PLATFORM ?= pc-premium
GENRE ?= action-roguelite
TASK ?= Investigate controller aim drift
FEATURE ?= Example Feature
BUG ?= Example Bug
QA_TITLE ?= Example Feature
EVAL_TITLE ?= Example Eval
UNITY_STUB ?= tools/engine-stubs/unity/Unity
UNREAL_STUB ?= tools/engine-stubs/unreal/RunUAT.sh

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
	$(PYTHON) scripts/validate_workflows.py
	$(PYTHON) scripts/doctor.py
	$(PYTHON) scripts/validate_engine_kits.py
	$(PYTHON) scripts/run_local_evals.py
	$(PYTHON) scripts/godot_smoke.py --static-only
	$(PYTHON) -m pytest -q tests
	$(PYTHON) scripts/validate_repo_layout.py
	$(PYTHON) scripts/validate_docs.py
	$(PYTHON) scripts/validate_assets.py
	$(PYTHON) scripts/version_guard.py --output-dir build/ci/version
	$(PYTHON) scripts/ci_artifact_report.py --output-dir build/ci/local
	$(PYTHON) scripts/doc_sync_guard.py --json
	$(PYTHON) scripts/ci_quality_gate.py --report build/ci/local/ci-report.json --min-score 80 --minimum-readiness validation-ready

validate: ## Run layout, docs, and asset validation
	$(PYTHON) scripts/validate_workflows.py
	$(PYTHON) scripts/validate_engine_kits.py
	$(PYTHON) scripts/godot_smoke.py --static-only
	$(PYTHON) scripts/version_guard.py --json
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

ci-workflows: ## Validate GitHub workflow coverage and action pinning
	$(PYTHON) scripts/validate_workflows.py

ci-doc-sync: ## Fail if changed code likely needs docs updates
	$(PYTHON) scripts/doc_sync_guard.py --json

ci-quality: ## Generate and enforce the local CI quality gate
	$(PYTHON) scripts/version_guard.py --output-dir build/ci/version
	$(PYTHON) scripts/ci_artifact_report.py --output-dir build/ci/latest
	$(PYTHON) scripts/ci_quality_gate.py --report build/ci/latest/ci-report.json --min-score 80 --minimum-readiness validation-ready

ci-report: ## Generate CI health artifacts into build/ci/latest
	$(PYTHON) scripts/version_guard.py --output-dir build/ci/version
	$(PYTHON) scripts/ci_artifact_report.py --output-dir build/ci/latest

starter-kit-smoke: ## Run starter-kit contract smoke for all supported engines
	$(PYTHON) scripts/starter_kit_contract_smoke.py --engine godot-4 --output-dir build/ci/starter-kit
	$(PYTHON) scripts/starter_kit_contract_smoke.py --engine unity-6 --output-dir build/ci/starter-kit
	$(PYTHON) scripts/starter_kit_contract_smoke.py --engine unreal-5 --output-dir build/ci/starter-kit

unity-test-command: ## Print the Unity test command for the starter-kit scaffold
	$(PYTHON) scripts/unity_adapter.py test --project-path studio/starter-kits/unity-6/scaffold --unity-path $(UNITY_STUB) --dry-run --json

unity-build-command: ## Print the Unity build command for the starter-kit scaffold
	$(PYTHON) scripts/unity_adapter.py build --project-path studio/starter-kits/unity-6/scaffold --unity-path $(UNITY_STUB) --dry-run --json

unreal-package-command: ## Print the Unreal package command for the starter-kit scaffold
	$(PYTHON) scripts/unreal_adapter.py package --project-path studio/starter-kits/unreal-5/scaffold --uat-path $(UNREAL_STUB) --dry-run --json

feature: ## Scaffold a feature brief, ADR, test plan, and eval plan
	$(PYTHON) scripts/scaffold_feature.py "$(FEATURE)" --with-adr --with-test-plan --with-eval-plan

bug: ## Scaffold bug triage docs plus optional validation artifacts
	$(PYTHON) scripts/scaffold_bugfix.py "$(BUG)" --with-test-plan --with-eval-plan

qa: ## Generate a lightweight QA matrix
	$(PYTHON) scripts/generate_qa_matrix.py "$(QA_TITLE)"

eval: ## Scaffold an eval plan for behavior or instruction changes
	$(PYTHON) scripts/scaffold_eval_plan.py "$(EVAL_TITLE)"

evals: ## Run the local eval corpus
	$(PYTHON) scripts/run_local_evals.py

bench: ## Run the repo-local benchmark corpus
	$(PYTHON) scripts/run_bench.py

version: ## Validate version metadata and changelog sync
	$(PYTHON) scripts/version_guard.py --json

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
