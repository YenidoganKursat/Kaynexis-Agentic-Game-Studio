using UnityEngine;

namespace StarterKit.Runtime
{
    public class CombatRoomDirector : MonoBehaviour
    {
        [SerializeField] private EnemyArchetype enemyArchetype;
        [SerializeField] private int waveSize = 3;

        public string DescribeSlice()
        {
            var archetypeName = enemyArchetype == null ? "Unknown Enemy" : enemyArchetype.displayName;
            return $"Starter slice: {waveSize}x {archetypeName}";
        }
    }
}
