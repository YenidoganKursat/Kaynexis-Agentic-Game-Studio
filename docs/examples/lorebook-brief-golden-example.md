# Lorebook Brief Golden Example

## Canon scope
- The lorebook stores world canon for the Aster Vale setting, including factions, locations, historical events, artifacts, and glossary terms.
- It does not store live quest state or temporary conversation state.

## Entry types
- Characters
- Factions
- Locations
- Artifacts
- Timeline events
- Glossary terms

## Entry schema
- Stable id: `faction.iron_saints`
- Title: Iron Saints
- Summary: A frontier order that guards relic routes and forbids unlicensed excavation.
- Canon status: `canon`
- Tags: `faction`, `frontier`, `law`, `relics`
- Related entries: `location.red_forge`, `item.relic_key`
- Unlock conditions: Discover the Iron Saints in the first town questline
- Gameplay hooks: faction reputation, quest gating, merchant access
- Localization keys: `lore.faction.iron_saints.title`, `lore.faction.iron_saints.summary`
- Owner: narrative director

## Access rules
- The player can read faction and location entries after the relevant discovery event.
- Artifact and timeline entries unlock later through quests and exploration.
- Dialogue can query the lorebook, but quest state remains the authority for unlocks.

## Update rules
- Rewriting the summary for tone does not change canon.
- A revision is required if a faction alignment or historical fact changes.
- Localization may change prose, but stable ids and tags remain fixed.

## Implementation notes
- Save/load must persist unlocked lore ids.
- UI should present entries as short, skimmable cards with expandable detail.
- Dialogue and quest systems should request unlocks rather than directly mutating canon.
