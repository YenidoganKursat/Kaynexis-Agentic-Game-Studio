# Audio Direction Lite — Kaynexis Agentic Game Studio

## Audio pillars
- Critical gameplay timing cues always cut through the mix
- Audio feedback reinforces state changes before it chases spectacle
- The room should feel tense and reactive without drowning out player input feedback

## Mix hierarchy
- Highest priority: damage windows, dodge success, incoming threat pulses
- Secondary: enemy loop, room state changes, upgrade selection feedback
- Tertiary: ambience and musical support that can duck under combat-critical cues

## Event priorities
- Dodge success and failure need different envelopes and tonal identity
- Enemy pulse wind-up should be readable even with effects-heavy visuals
- Upgrade reward should feel distinct from combat resolution

## Implementation notes
- Start with engine-native playback unless a middleware need is proven
- Keep one-shot variation lightweight and deterministic
- Review repeated combat cues for fatigue before adding content scale
- For the full simple-to-advanced ladder, read `docs/reference/audio-animation-guide.md` and the matching engine presentation note before implementation
