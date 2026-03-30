# Unity UI

## Date
- 2026-03-29

## Summary
- Unity UI is healthiest when the project chooses a stack intentionally: UI Toolkit for data-heavy or tool-like screens, uGUI for quick runtime overlays or legacy code, and the Input System / event system assumptions are named instead of buried in scripts.
- The most used stack in newer projects is UI Toolkit with `UIDocument`, UXML, USS, UI Builder, and the runtime event system.
- Use uGUI when the screen is simple, the team already has a working runtime HUD path, or the project is still migrating from legacy UI.

## Primary sources
- [Unity UI Toolkit manual](https://docs.unity3d.com/2023.2/Documentation/Manual/UIElements.html)
- [Unity UI Builder](https://docs.unity3d.com/ja/current/Manual/best-practice-guides/ui-toolkit-for-advanced-unity-developers/ui-builder.html)
- [Unity runtime UI event system](https://docs.unity3d.com/ja/6000.0/Manual/UIE-Runtime-Event-System.html)
- [Unity UI Toolkit FAQ for input and event systems](https://docs.unity3d.com/ja/6000.0/Manual/UIE-faq-event-and-input-system.html)

## Why this matters to this repo
- UI tasks should say whether the screen is built for runtime HUD, editor tooling, or a reusable state-driven menu.
- UI Toolkit and uGUI have different strengths; the wrong choice can make a simple screen harder to own than the gameplay system behind it.
- Agents should not pick a stack only because it is familiar; they should pick the smallest stack that fits the case.

## Decision impact
- Prefer UI Toolkit for data-heavy screens, reusable layouts, or editor-adjacent tooling.
- Prefer uGUI for quick overlay HUDs, legacy projects, or when the runtime path is already stable.
- Prefer `ScriptableObject` or plain C# models for projected data instead of letting the UI own runtime truth.

## Simple-to-advanced ladder
1. A basic uGUI overlay or a minimal UI Toolkit screen.
2. A data-driven screen with `UIDocument`, UXML, USS, and explicit event ownership.
3. A reusable UI Builder template with shared style assets and controlled state projection.
4. A full screen-flow architecture with navigation, accessibility, and template reuse across several menus or HUDs.

## Ready-made template sources
- UI Builder templates and package samples.
- UI Toolkit sample projects and package examples.
- The Asset Store for reusable runtime UI packs when the official path is not enough.
- This repo's starter kits and UI examples.

## Common mistakes
- Letting `MonoBehaviour` own the whole screen state.
- Mixing transient widget state with durable game state.
- Using uGUI where UI Toolkit would keep the screen more reusable.
- Forgetting to name the template source and style source.

## Repo impact
- UI tasks should surface the stack, the template source, the projection boundary, and the validation path before implementation.

