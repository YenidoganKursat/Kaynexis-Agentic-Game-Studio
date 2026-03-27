using NUnit.Framework;
using StarterKit.Runtime;
using UnityEngine;

namespace StarterKit.EditModeTests
{
    public class HealthTests
    {
        [Test]
        public void ApplyDamage_ClampsToZero()
        {
            var gameObject = new GameObject("Health");
            var health = gameObject.AddComponent<Health>();

            health.ResetHealth(20);
            health.ApplyDamage(50);

            Assert.That(health.CurrentHealth, Is.EqualTo(0));
            Assert.That(health.IsAlive, Is.False);

            Object.DestroyImmediate(gameObject);
        }
    }
}
