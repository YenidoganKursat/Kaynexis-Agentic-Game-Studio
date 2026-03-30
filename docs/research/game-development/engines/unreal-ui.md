# Unreal UI

## Date
- 2026-03-29

## Summary
- Unreal UI is healthiest when `UMG` / Widget Blueprints own presentation, CommonUI owns input and screen-activation behavior, and gameplay truth stays in gameplay classes or components.
- The most used stack is `UMG` + Widget Blueprints + CommonUI + Enhanced Input, with MVVM or viewmodels when the screen becomes larger or more data-driven.
- Use UMG for HUDs, menus, and overlays; use CommonUI when controller-first input and screen activation matter.

## Primary sources
- [UMG UI Designer Quick Start Guide](https://dev.epicgames.com/documentation/de-de/unreal-engine/umg-ui-designer-quick-start-guide?application_version=4.27)
- [Input Fundamentals for CommonUI in Unreal Engine](https://dev.epicgames.com/documentation/zh-cn/unreal-engine/input-fundamentals-for-commonui-in-unreal-engine)
- [Using CommonUI With Enhanced Input in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-commonui-with-enhnaced-input-in-unreal-engine?application_version=5.6)

## Why this matters to this repo
- Unreal UI work gets fragile when widgets own authority or when input routing is not defined up front.
- UMG can be a very fast path for menus and HUDs, but the project should still name the data owner and the screen owner explicitly.
- CommonUI becomes more valuable as soon as screen activation, controller focus, and input routing need to remain predictable.

## Decision impact
- Prefer UMG / Widget Blueprints for HUDs, menus, and overlays.
- Prefer CommonUI when controller-first navigation or screen activation needs to be explicit.
- Prefer viewmodels or projected data objects when the UI becomes more than a thin overlay.

## Simple-to-advanced ladder
1. A basic Widget Blueprint HUD or menu.
2. A UMG screen with explicit data projection and named input routing.
3. A CommonUI-based flow with activatable screens and controller-first navigation.
4. A larger screen system using viewmodels, CommonUI, and gameplay-framework integration.

## Ready-made template sources
- The UMG quick start guide and its menu examples.
- CommonUI docs and sample patterns.
- Widget Blueprint templates created in the editor.
- Fab or marketplace UI packs when the official path is not enough.
- This repo's starter kits and UI examples.

## Common mistakes
- Letting widgets own combat or save authority.
- Skipping input and focus planning for controller-first screens.
- Hiding gameplay state inside the widget graph.
- Treating CommonUI as optional once the screen count grows.

## Repo impact
- UI briefs for Unreal should name the widget owner, the input owner, the projected data owner, and the template source before implementation.
