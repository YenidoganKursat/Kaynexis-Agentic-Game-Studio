# Cross-Platform Example

## Scope
- A Steam-first survival game wants a support-tier plan for Windows, macOS, Linux / Steam Deck, web demo, Android / iOS, and webOS / TV.
- The team needs a simple matrix that says what is core, what is supported, what is demo-only, and what is still research-only.

## Baseline
- One codebase is allowed.
- One support promise is not.
- The core family should own the first slice.
- The next family should be the one that stresses the same loop and the same release assumptions.

## Decision order
1. Name the core family.
2. Name the support tier for each family.
3. Separate input, session, save, policy, packaging, and performance deltas.
4. Pick the first validation per family.
5. Write the release sequence before implementation.

## Example support map
| Family | Tier | First delta | First validation | Release note |
|---|---|---|---|---|
| Windows PC | `core` | Keyboard/mouse and controller parity | Launch + input smoke | Primary release path |
| macOS | `supported` | Signing, sandbox, and Apple Silicon behavior | Signed build + controller pass | Same content, different packaging |
| Linux / Steam Deck | `supported` | Steamworks, Proton, controller, and verification expectations | Steam-specific launch + controller pass | Deck evidence must be visible |
| Web demo | `demo` | Browser startup, memory budget, and focus loss | Time-to-interactive + browser resume | Discovery surface, not full parity |
| Android / iOS | `research` | Touch, battery, thermal, suspend/resume | One touch session + one background/resume pass | Keep scope small until proven |
| webOS / TV | `research` | Remote navigation, 10-foot readability, safe areas | Focus navigation + readability pass | Treat as a separate UI contract |

## Dashboard schema
- Header cards: core family, next family, current blocker, confidence
- Matrix: family, tier, input model, perf envelope, policy risk, release order
- Heatmap: readiness by family
- Release card: go/no-go, first lever, fallback lever, owner

## Good agent prompts
- "Build a support-tier matrix for Windows, macOS, Linux / Steam Deck, web, Android / iOS, and webOS / TV before any porting work."
- "Tell me which platform differences are launch blockers versus future research for a Steam-first build."
- "Summarize the biggest compatibility risks for webOS TV and Steam Deck using official docs first."

## Validation
- The support tier is explicit for every family.
- The first validation step is named before tuning.
- The output includes one chart or matrix plus one release implication.

## Related docs
- [docs/reference/cross-platform-guide.md](../reference/cross-platform-guide.md)
- [docs/reference/platform-guide.md](../reference/platform-guide.md)
- [docs/research/game-development/production/cross-platform.md](../research/game-development/production/cross-platform.md)
- [docs/examples/platform-example.md](platform-example.md)
- [studio/docs/active/platform-targets.md](/Users/kursatyenidogan/Documents/codex/kaynexisGame/studio/docs/active/platform-targets.md)
