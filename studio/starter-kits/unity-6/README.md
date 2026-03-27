# Unity 6 Starter Kit

Use this kit when the repo should target Unity 6 / 6000.x with a package-aware, asmdef-first structure.

Key assumptions:

- code is grouped by feature, not by giant shared folders
- `Packages/manifest.json` is committed and treated as a contract
- asmdef files create explicit runtime/editor/test boundaries
- the real editor binary can stay external while the repo still validates the intended commands
- the scaffold includes one sample combat-room director, one enemy data asset contract, and one edit-mode test
