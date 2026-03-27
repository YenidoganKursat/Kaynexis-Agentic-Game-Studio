using NUnit.Framework;
using StarterKit.Runtime;
using UnityEngine;

namespace StarterKit.EditModeTests
{
    public class CombatRoomDirectorTests
    {
        [Test]
        public void DescribeSlice_ReturnsStarterPrefix()
        {
            var gameObject = new GameObject("CombatRoomDirector");
            var director = gameObject.AddComponent<CombatRoomDirector>();

            StringAssert.Contains("Starter slice:", director.DescribeSlice());

            Object.DestroyImmediate(gameObject);
        }
    }
}
