using UnityEngine;

namespace StarterKit.Runtime
{
    public class PulseEnemy : MonoBehaviour
    {
        [SerializeField] private EnemyArchetype archetype;
        [SerializeField] private float pulseWindupSeconds = 1.2f;
        [SerializeField] private float pulseRadius = 3.0f;

        public EnemyArchetype Archetype => archetype;
        public float PulseWindupSeconds => pulseWindupSeconds;
        public float PulseRadius => pulseRadius;

        public void Configure(EnemyArchetype source)
        {
            if (source == null)
            {
                return;
            }

            archetype = source;
            pulseWindupSeconds = source.attackWindupSeconds;
            pulseRadius = source.pulseRadius;
        }

        public string DescribePressureProfile()
        {
            var displayName = archetype == null ? "Unknown Enemy" : archetype.displayName;
            return $"{displayName} | windup {pulseWindupSeconds:0.0}s | radius {pulseRadius:0.0}m";
        }
    }
}
