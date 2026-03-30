# Bug Example

## Title
- Pulse hit registers while player is visibly outside the warning ring

## Repro
1. Start the combat room
2. Wait for the enemy pulse to expand
3. Dash diagonally out of the ring near the edge
4. Observe damage still applied

## Expected
- Damage should apply only while the player remains in the dangerous pulse band.

## Actual
- Damage applies even after the player sprite appears outside the ring.

## Severity
- High gameplay readability regression

## Validation after fix
- Re-test edge exits at multiple approach angles
- Capture one video or GIF for the fixed read
