# Eval Plan: Assets

## Goal
- Verify that asset-heavy work routes through the asset guide, asset example, and asset pipeline research before implementation.

## What to test
- Asset ownership questions should name the runtime owner, authored-data owner, and editor owner.
- Asset import questions should name the source file, import boundary, and load path.
- Asset alternative questions should land on the right engine-specific choice instead of a generic guess.

## Minimum acceptance
- A task about asset management should surface `docs/reference/asset-guide.md`.
- A task about asset management should surface `docs/examples/asset-example.md`.
- A checklist for asset work should include `assets-owner`, `assets-alternative`, and `assets-import-boundary`.

## Failure modes
- Asset tasks are routed only to visuals or generic content pipeline notes.
- Runtime state and authored data are mixed together.
- Source art and imported artifacts are not separated in the docs or checklist.
