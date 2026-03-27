# Layered Checklists

Checklists are structured manifests that the shared Codex workflow can merge deterministically.

Merge order:

1. `base`
2. `engine`
3. `discipline`
4. `milestone`
5. `custom`

Later layers override earlier ones by `item.id`.
