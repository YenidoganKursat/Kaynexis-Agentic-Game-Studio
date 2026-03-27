using UnityEngine;

namespace StarterKit.Runtime
{
    [CreateAssetMenu(menuName = "StarterKit/Enemy Archetype")]
    public class EnemyArchetype : ScriptableObject
    {
        public string displayName = "Pulse Warden";
        public int baseHealth = 30;
        public int contactDamage = 10;
    }
}
