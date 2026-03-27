using UnityEngine;

namespace StarterKit.Runtime
{
    public class CombatRoomDirector : MonoBehaviour
    {
        [SerializeField] private EnemyArchetype enemyArchetype;
        [SerializeField] private PlayerAvatar playerAvatar;
        [SerializeField] private PulseEnemy pulseEnemy;
        [SerializeField] private int waveSize = 3;

        public string DescribeSlice()
        {
            var archetypeName = enemyArchetype == null ? "Unknown Enemy" : enemyArchetype.displayName;
            var playerSummary = playerAvatar == null ? "No Player" : playerAvatar.DescribeControlSurface();
            var enemySummary = pulseEnemy == null ? "No Enemy Actor" : pulseEnemy.DescribePressureProfile();
            return $"Starter slice: {waveSize}x {archetypeName} | {playerSummary} | {enemySummary}";
        }

        public string DescribeNextExpansion()
        {
            return "Next expansion: add room state, reward choice, and pooled projectile pressure.";
        }
    }
}
