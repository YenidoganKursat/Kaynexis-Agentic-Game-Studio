---
name: security-threat-model
description: Build a repo- or feature-level threat model with abuse paths, trust boundaries, exploit severity, and mitigations. Use for backend, economy, multiplayer, auth, or modding work.
---

# Security Threat Model

## When to use
Build a repo- or feature-level threat model with abuse paths, trust boundaries, exploit severity, and mitigations. Use for backend, economy, multiplayer, auth, or modding work.

## Inputs to gather
- system/feature
- actors
- assets to protect
- cheat/exploit concerns

## Recommended roles
- `security_engineer`
- `technical_director`
- `backend_engineer`

## Primary docs / outputs
- `studio/docs/templates/adr.md`
- `studio/docs/templates/telemetry-schema.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Choose the smallest useful output that moves the project forward.
3. Make the highest-risk issue, blocker, or readiness gap unambiguous.
4. Update or create durable docs when the result should persist.
5. Recommend the next best role or skill if more work remains.

## Category rules
- Prioritize severe player-facing, security, certification, and release risks over cosmetic issues.
- Make evidence, repro, and owner/action clarity explicit.
- Return a clear go/no-go or priority recommendation when the task is evaluative.

## Deliverables
- threat model
- severity-ranked issues
- mitigation plan
- logging/monitoring needs

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
