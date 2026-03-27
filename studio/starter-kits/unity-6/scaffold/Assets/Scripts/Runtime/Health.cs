using UnityEngine;

namespace StarterKit.Runtime
{
    public class Health : MonoBehaviour
    {
        [SerializeField] private int maxHealth = 30;
        [SerializeField] private int currentHealth = 30;

        public int MaxHealth => maxHealth;
        public int CurrentHealth => currentHealth;
        public bool IsAlive => currentHealth > 0;

        public void ResetHealth(int value)
        {
            maxHealth = Mathf.Max(1, value);
            currentHealth = maxHealth;
        }

        public void ApplyDamage(int amount)
        {
            currentHealth = Mathf.Max(0, currentHealth - Mathf.Max(0, amount));
        }
    }
}
