# Capability Catalog Example

Goal: answer "what can this studio do?" without dumping the whole repo on the reader.

## Example prompt

> Show me everything this studio can do and the best starting docs for each major lane.

## Example answer shape

### Short answer

This repo can help with:

- engine and gameplay setup
- feature brief and mechanic design
- genre planning and maturity checks
- architecture, custom rules, and extensions
- quality, performance, benchmark, and engine-eval work
- engine bug analysis and troubleshooting
- marketing, Steam, sector, and platform intelligence
- audio, animation, UI, assets, content, and localization
- agent control, validation, prompt history, and transcripts

### Suggested lanes

| If the user wants... | Start here |
| --- | --- |
| the full studio overview | `docs/reference/capabilities.md` |
| the agent operating model | `docs/reference/agent-system.md` |
| the controller loop | `docs/reference/mastermind-guide.md` |
| the engine and gameplay surface | `docs/reference/engine-map.md` and `docs/reference/engine-atlas.md` |
| recurring engine bugs or first checks | `docs/reference/engine-bugs.md` and `docs/examples/engine-bugs-example.md` |
| the current market or marketing picture | `docs/reference/sector-intel.md`, `docs/reference/steam-intel.md`, `docs/reference/marketing-intel.md` |
| the performance and measurement stack | `docs/reference/perf-guide.md`, `docs/reference/benchmark-guide.md`, `docs/reference/engine-eval.md` |

### Simple follow-up

If the user wants one lane after the catalog, the reply should stay narrow:

- "For engine work, start with the engine map and the matching engine atlas."
- "For market signals, start with sector intel, Steam intel, or marketing intel depending on the question."
- "For broad orchestration, use the mastermind guide and agent portfolio."

## What to keep visible

- the capability family
- the best starting doc
- the validation path
- the next narrow lane
