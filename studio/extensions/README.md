# Extensions

Use this folder for opt-in extension packs that add custom capability surfaces without rewriting the canonical architecture.

If the task needs a reusable custom feature registry or broader pack bundle before an opt-in extension is designed, start with `docs/reference/custom-packs.md` first.

This folder is for:

- plugin-like add-ons
- optional hook packs
- editor-side helper surfaces
- project-specific manifests that can be enabled or disabled cleanly

This folder is not for:

- the canonical architecture families
- the custom request contract lane
- third-party library selection notes

Recommended pack layers:

1. canonical architecture
2. custom pack registry
3. custom architecture contract
4. extension pack
5. project-specific override

Suggested pack shape:

- `custom/README.md`
- `custom/manifest.example.toml`
- `custom/eval-plan.md` for attach/detach proof and fallback checks

If you need project-specific house-rule overrides rather than optional capability surfaces, use `studio/checklists/custom/` instead.
