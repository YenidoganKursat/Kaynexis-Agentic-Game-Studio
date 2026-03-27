# Manual Smoke Test

## Goal

Verify that the combat room opens, plays correctly, and resolves the reward choice.

## Steps

1. Open the project in Godot 4.x
2. Confirm `project.godot` loads without migration errors
3. Run the main scene
4. Move with `WASD` or arrow keys
5. Wait for the yellow telegraph ring
6. Dash with `Space` or `Enter` through the red pulse
7. Confirm the room clears and shows a reward choice
8. Press `1` or `2` and confirm the reward text updates

## Expected Result

- The project imports cleanly
- The player can move and dash
- The Pulse Warden can be defeated only by correct timing
- The reward choice appears after the clear
- No immediate startup errors appear
