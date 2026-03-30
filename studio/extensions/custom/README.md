# Custom Extension Pack

This folder is for project-specific extension packs that sit on top of the shared extension contract.

Use it when a pack needs:

- a project-only manifest
- a small set of hook points
- an explicit enable or disable decision
- a clear fallback if the pack is not loaded

If the task is actually about a broader reusable feature registry, go back to `docs/reference/custom-packs.md` first.

Suggested layout:

- `manifest.example.toml`
- `README.md`
- `eval-plan.md` for attach/detach smoke and fallback proof

If the task is really about fixed versus overrideable rules, go back to `docs/reference/custom-architecture.md` and `studio/checklists/discipline/custom.toml` first.
