# Layered Checklists

Checklists are structured manifests that the shared Codex workflow can merge deterministically.

Merge order:

1. `base`
2. `engine`
3. `discipline`
4. `milestone`
5. `custom`

Later layers override earlier ones by `item.id`.

The base layer currently carries repository health, naming, and feature-slice rules so the shortest canonical names and the most important validation checks stay in every bundle.
The discipline layer carries architecture, capabilities, theory, custom, custom_packs, extensions, assets, benchmark, quality, performance, advanced_performance, gpu, genre, hierarchy, library, versioning, presentation, bugfix, engine_bugs, gameplay, UI, narrative, mastermind, agent_validation, agent_execution, speedpack, openai_codex, openai_models, sector, steam_intel, marketing, marketing_intel, release_hardening, platform_compatibility, console, engine_fit, engine_eval, agents, transcript, and role-specific packs such as producer, technical_director, qa_lead, release_manager, build_release_engineer, docs_researcher, performance_analyst, game_designer, engine_programmer, gameplay_programmer, ui_programmer, narrative_director, art_director, and audio_director so each specialist lane can stay narrow without losing the higher-order control contract.

Use `studio/checklists/discipline/custom_packs.toml` for the shared custom pack registry contract, `studio/checklists/discipline/custom.toml` for the narrower custom architecture and rule-pack contract, and `studio/checklists/custom/` for project-specific house rules or override manifests that should win later in the merge order.
If you are pointing someone at the exact override folder, use `studio/checklists/custom/README.md` as the canonical path for the project-specific notes page.
Use `studio/checklists/discipline/extensions.toml` for the shared extension-pack contract, and use `studio/extensions/` for optional add-on manifests and pack notes that should stay reviewable.
Use `studio/checklists/discipline/speedpack.toml` for the shortest safe-start contract and keep `docs/reference/agent-speedpack.md` nearby when a task should stay fast.
Use `studio/checklists/discipline/console.toml` for the console-premium porting and submission contract, and keep `studio/docs/active/platform-targets.md` synchronized when a console family becomes core or supported.
