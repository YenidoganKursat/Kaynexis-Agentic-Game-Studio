# Manual Smoke Test

## Goal

Verify the first playable combat room opens, runs, and resolves its reward choice.

## Steps

1. Open the repo in Godot 4.x
2. Confirm `project.godot` loads without migration errors
3. Run the main scene
4. Move with `WASD` or arrow keys
5. Wait for the Pulse Warden's yellow telegraph ring, then dash with `Space` or `Enter` through the red pulse
6. Confirm the room clears and shows an upgrade choice
7. Press `1` or `2` and confirm the slice resolves with a reward message

## Expected result

- Project imports cleanly
- Main scene runs
- The player can move and dash
- The Pulse Warden can be defeated only by a correctly timed dash
- A reward choice appears after the clear
- No immediate startup errors appear
