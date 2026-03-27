using UnityEngine;

namespace StarterKit.Runtime
{
    public class PlayerAvatar : MonoBehaviour
    {
        [SerializeField] private float moveSpeed = 7.5f;
        [SerializeField] private float dashDistance = 4.5f;
        [SerializeField] private float dashCooldown = 0.9f;

        public float MoveSpeed => moveSpeed;
        public float DashDistance => dashDistance;
        public float DashCooldown => dashCooldown;

        public string DescribeControlSurface()
        {
            return $"Move {moveSpeed:0.0} | Dash {dashDistance:0.0}m / {dashCooldown:0.0}s";
        }
    }
}
