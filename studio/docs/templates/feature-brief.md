# Feature Brief — {FEATURE_NAME}

## Player outcome
- What player problem/fantasy this serves

## Scope
- Must-have
- Nice-to-have
- Explicit non-goals

## Acceptance criteria
- Criterion 1
- Criterion 2
- Criterion 3

## Touched systems
- Code modules / scenes / prefabs / data / assets

## Architecture decisions
- World stack: 2D / 3D / hybrid
- Update domain: frame / fixed-step / turn / event-driven
- State owner: run/session owner, player-state owner, durable data owner
- Scale strategy: normal entities / pooling / instancing / DOTS / Mass / other

## System atlas lookup
- Primary system atlas: `{SYSTEM_ATLAS_REF}`
- Core class atlas: `{ENGINE_ATLAS_REF}`
- Fast owner map: `{ENGINE_MAP_REF}`
- Matching engine mini atlas: {ENGINE_MINI_ATLAS_NOTE}
- Example snippets consulted: combat, inventory, dialogue, quest, crafting, save, AI, UI, economy, network, accessibility, meta, live ops

## Combat / AI / traversal contract
- Navigation model: navmesh / graph / authored lanes / none
- Contact model: trigger / overlap / collision / direct query
- Damage/effect flow: where detection, resolution, state mutation, and feedback live

## Risks & dependencies
- Risks
- External dependencies
- Test focus
