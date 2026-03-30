# Production Research

Use these notes when release, CI, content delivery, or incident work needs a durable production contract.

## Production structure map

| Decision family | What it covers | Start here |
| --- | --- | --- |
| release validation and CI/CD | release readiness, protected builds, workflow gates, artifact evidence, trust boundaries, and runner assumptions | `release-validation.md`, `release-hardening.md`, `docs/reference/ci-cd.md`, `docs/reference/release-hardening-guide.md`, `studio/docs/active/build-pipeline.md` |
| versioning and provenance | canonical version file, changelog sync, tag policy, and commit-note contract | `versioning.md`, `docs/reference/version-guide.md`, `CHANGELOG.md`, `VERSION` |
| cross-platform support strategy | support tiers, family sequencing, release order, and first-family proof | `cross-platform.md`, `docs/reference/cross-platform-guide.md`, `docs/examples/cross-platform-example.md` |
| console readiness | PS5-like, Xbox-like, and Switch-like submission gates, controller-first UX, and cert evidence | `console.md`, `docs/reference/console-guide.md`, `docs/examples/console-example.md` |
| platform readiness | Windows, macOS, Linux/Steam Deck, web, mobile, TV, and porting deltas | `platform.md`, `platform-compatibility.md`, `docs/reference/platform-guide.md` |
| current market signals | sector, Steam, platform, and release timing signals | `sector-intel.md`, `steam-intel.md`, `docs/reference/sector-intel.md`, `docs/reference/steam-intel.md` |
| launch and channel planning | marketing strategy, community follow-up, and measurement loops | `marketing.md`, `docs/reference/marketing-guide.md` |
| marketing status and chart packs | current campaign movement, funnel health, and dashboard snapshots | `marketing-intel.md`, `docs/reference/marketing-intel.md` |
| delivery and incident ops | content pipeline, hotfix, rollback, and incident response | `content-pipeline.md`, `incident.md` |

## Notes
- `release-validation.md` — deterministic release readiness, artifact expectations, and known-issue visibility
- `release-hardening.md` — build integrity, code protection, symbol policy, and multiplayer trust boundaries
- `release-hardening.md` — protected builds, code protection, symbol policy, and multiplayer trust
- `versioning.md` — canonical version file, changelog sync, and tag policy
- `platform.md` — platform readiness and release deltas
- `cross-platform.md` — support tiers, family sequencing, and release order
- `console.md` — PS5-like, Xbox-like, and Switch-like submission evidence and cert assumptions
- `platform-compatibility.md` — source-backed family-by-family compatibility planning
- `content-pipeline.md` — content entry, validation, and packaging boundaries
- `incident.md` — hotfix, rollback, and incident response guidance
- `sector-intel.md` — current game-industry, platform, and market signals
- `steam-intel.md` — Steam-specific store, wishlist, forum, hardware, and market signals
- `marketing.md` — marketing strategy, channel fit, and measurement loops
- `marketing-intel.md` — current campaign movement, funnel health, and chart-pack snapshots
