# Unity Atlas

This page is the deeper Unity companion to `engine-map.md` and `engine-atlas.md`.

Use it when an agent needs to know which Unity class family should own runtime behavior, shared data, editor tooling, or contact flow.

This is a core atlas, not an exhaustive class catalog.

## Read this with

- `docs/reference/engine-map.md`
- `docs/reference/engine-atlas.md`
- `docs/research/game-development/engines/unity-map.md`
- `docs/research/game-development/engines/unity-classes.md`
- `docs/research/game-development/engines/unity-systems.md`

## Core ownership model

| Family | Runtime owner | Shared data owner | Editor owner | Example use |
| --- | --- | --- | --- | --- |
| Scene identity | `GameObject` | `ScriptableObject` | Inspector | object composition, hierarchy, prefab host |
| Runtime behavior | `MonoBehaviour` | plain C# model / service | Inspector / custom editor | scene-bound logic, orchestration |
| Reuse blueprint | `Prefab` | `ScriptableObject` | Prefab stage / Inspector | repeated enemies, projectiles, props |
| Physics/contact | `Collider2D` / `Collider` | service or definition asset | Inspector | pickups, damage, sensing |
| Motion | `Rigidbody2D` / `Rigidbody` / `CharacterController` | tuning asset | Inspector | movement and knockback |
| UI | UI Toolkit or uGUI | `ScriptableObject` or view model | UI Builder / Inspector | HUD, menu, tools |
| Editor tooling | `EditorWindow` / `Editor` | asset or code model | Editor only | authoring, validation, batch tools |

## Core classes and what they are for

### `GameObject`

- What it is: the scene identity and component host
- Good for: composition, attachment, scene organization
- Not good for: shared tuning or full game logic
- Input: prefab instantiation, scene placement
- Output: component host, hierarchy structure
- Example use: enemy object with movement, health, and visual components

### `Transform`

- What it is: hierarchy and spatial state
- Good for: positions, parenting, local/world conversion
- Not good for: gameplay rules
- Input: motion and attachment updates
- Output: spatial coordinates
- Example use: camera follow anchor, weapon socket, UI anchor

### `MonoBehaviour`

- What it is: scene-bound runtime behavior
- Good for: orchestration, glue, input response, state updates
- Not good for: everything at once
- Input: lifecycle callbacks, gameplay events
- Output: behavior, commands, scene updates
- Example use: player controller, enemy brain, room director

### `ScriptableObject`

- What it is: shared authored data
- Good for: item definitions, upgrades, configs, ability definitions
- Not good for: storing per-run mutable state
- Input: inspector edits, authored content
- Output: reusable data and tuning
- Example use: item database entry, enemy archetype config

### `Prefab`

- What it is: reusable hierarchy blueprint
- Good for: repeated enemies, effects, props, UI widgets
- Not good for: one-off global state ownership
- Input: authored hierarchy
- Output: repeatable instances
- Example use: pooled projectile prefab, repeated enemy prefab

### `Collider2D` and `Collider`

- What they are: contact input surfaces
- Good for: triggers, overlaps, collision callbacks, sensing
- Not good for: owning the whole mechanic
- Input: trigger/collision events, layer filtering, queries
- Output: damage, pickup, aggro, interaction, feedback requests
- Example use: pickup trigger, hitbox, interaction volume

### `Rigidbody2D` and `Rigidbody`

- What they are: simulated motion bodies
- Good for: physics-driven movement, knockback, pushes
- Not good for: raw teleport authority unless intentionally designed
- Input: forces, velocities, collisions
- Output: simulated movement
- Example use: physics projectiles, knockback enemy, movable props

### `CharacterController`

- What it is: authored control movement helper
- Good for: responsive 3D locomotion with custom control
- Not good for: pretending it is a Rigidbody
- Input: move vectors, ground checks
- Output: controlled character motion
- Example use: third-person or top-down controlled movement

### `Animator`

- What it is: animation state machine
- Good for: state-driven visuals, parameterized animation
- Not good for: hidden gameplay authority
- Input: movement state, triggers, blend values
- Output: visible animation state
- Example use: attack combo states, locomotion blend tree

### UI Toolkit and uGUI

- What they are: UI presentation stacks
- Good for: menus, HUDs, settings, tools
- Not good for: owning gameplay logic
- Input: projected runtime data, user input
- Output: visible UI and UI events
- Example use: inventory screen, pause menu, settings menu

### `EditorWindow`, `Editor`, `CustomEditor`

- What they are: editor-only authoring surfaces
- Good for: workflow tools, inspectors, validation panels
- Not good for: runtime logic
- Input: assets, scene objects, authoring commands
- Output: tooling, batch operations, validation
- Example use: balancing tool, asset tagger, prefab audit tool

### `ObjectPool<T>`

- What it is: reuse helper for high-churn objects
- Good for: projectiles, VFX, repeated combat objects
- Not good for: objects that need unique lifecycle semantics without discipline
- Input: spawn requests, release requests
- Output: reused instance lifecycle
- Example use: pooled bullets, pooled hit VFX, pooled UI popups

## GPU and render-scale family

| Family | Runtime / render owner | Shared data owner | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| Buffer-driven rendering | `GraphicsBuffer` | `ScriptableObject` or plain model | instanced draws, structured render data | do not make buffers the gameplay owner |
| GPU compute | `ComputeShader` | `ScriptableObject` or plain model | parallel GPU work, culling, expansion | avoid readback-first designs |
| Repeated visuals | instanced indirect drawing | prefab or model data | dense repeated objects with one render path | do not keep one GameObject per repeated object |
| Visibility reduction | GPU occlusion culling | scene data / tuning assets | reduced GPU draw cost in dense scenes | do not use it before proving the frame is render-bound |

### Physics and query APIs

- What they are: direct contact and sensing tools
- Good for: hit checks, overlaps, line traces, cheap target queries
- Not good for: uncontrolled per-frame spam
- Input: query parameters
- Output: contact hits and overlaps
- Example use: aim ray, interaction sphere, pickup scan

## Common Unity mechanic patterns

| Mechanic | Likely owner | Example class pair | Common mistake |
| --- | --- | --- | --- |
| Movement | runtime behavior | `GameObject` + `MonoBehaviour` | making the `Transform` the whole state |
| Pickup | contact + data | `Collider2D` + `ScriptableObject` | collider owns item database state |
| HUD | UI stack | UI Toolkit / uGUI + view model | UI writes directly into gameplay authority |
| Upgrade choice | prefab + asset | `Prefab` + `ScriptableObject` | hardcoding every choice into one script |
| Enemy AI | behavior + data | `MonoBehaviour` + `ScriptableObject` | putting AI and tuning in the same monolith |
| Projectiles | pool + contact | `ObjectPool<T>` + `Collider2D` | instantiating every shot as a fresh object |

## Typical input/output contracts

- `GameObject` inputs composition, outputs a component host
- `MonoBehaviour` inputs lifecycle and events, outputs behavior
- `ScriptableObject` inputs authored data, outputs reusable tuning
- `Collider2D/Collider` inputs contact callbacks and queries, outputs gameplay triggers and feedback requests
- `EditorWindow` inputs authoring commands, outputs workflow improvements
- `ObjectPool<T>` inputs spawn/release, outputs reuse and lower churn

## Best first examples

- `GameObject` + `MonoBehaviour` for runtime logic
- `ScriptableObject` for items, upgrades, and enemy definitions
- `Collider2D` for detection that hands off to gameplay logic
- `Prefab` for repeated enemies and projectiles
- `EditorWindow` for batch authoring tools

## Example snippets

### Movement and contact

```csharp
using UnityEngine;

public class PlayerMover : MonoBehaviour
{
    [SerializeField] private float speed = 6f;
    private Vector2 moveInput;

    private void Update()
    {
        moveInput.x = Input.GetAxisRaw("Horizontal");
        moveInput.y = Input.GetAxisRaw("Vertical");
    }

    private void FixedUpdate()
    {
        transform.position += (Vector3)(moveInput.normalized * speed * Time.fixedDeltaTime);
    }
}
```

### Pickup detection

```csharp
using UnityEngine;

public class Pickup : MonoBehaviour
{
    [SerializeField] private string itemId;

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.TryGetComponent(out Inventory inventory))
        {
            inventory.Add(itemId);
            Destroy(gameObject);
        }
    }
}
```

### HUD projection

```csharp
using UnityEngine;
using UnityEngine.UI;

public class HealthHud : MonoBehaviour
{
    [SerializeField] private Text hpText;

    public void SetHp(int current, int max)
    {
        hpText.text = $"{current} / {max}";
    }
}
```

## Additional snippets

### Inventory model

```csharp
using System.Collections.Generic;
using UnityEngine;

public class Inventory : MonoBehaviour
{
    [SerializeField] private List<string> itemIds = new();

    public void Add(string itemId)
    {
        itemIds.Add(itemId);
    }
}
```

### Enemy chase

```csharp
using UnityEngine;
using UnityEngine.AI;

public class EnemyChase : MonoBehaviour
{
    [SerializeField] private Transform target;
    private NavMeshAgent agent;

    private void Awake()
    {
        agent = GetComponent<NavMeshAgent>();
    }

    private void Update()
    {
        if (target != null)
        {
            agent.SetDestination(target.position);
        }
    }
}
```

### Camera follow

```csharp
using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    [SerializeField] private Transform target;
    [SerializeField] private float followLerp = 0.15f;

    private void LateUpdate()
    {
        if (target == null) return;
        transform.position = Vector3.Lerp(transform.position, target.position, followLerp);
    }
}
```

### Save projection

```csharp
using System.IO;
using UnityEngine;

[System.Serializable]
public class SaveData
{
    public int hp;
    public List<string> itemIds = new();
}

public static class SaveSystem
{
    public static void Save(SaveData data)
    {
        File.WriteAllText(Application.persistentDataPath + "/save.json", JsonUtility.ToJson(data));
    }
}
```

### Skill tree choice

```csharp
using UnityEngine;

[CreateAssetMenu(menuName = "Game/Skill Node")]
public class SkillNodeData : ScriptableObject
{
    public string id;
    public string label;
    public int cost = 1;
}
```

### UI flow

```csharp
using UnityEngine;

public class UpgradePanel : MonoBehaviour
{
    public void Show()
    {
        gameObject.SetActive(true);
    }
}
```

### Animation trigger

```csharp
using UnityEngine;

public class PlayerCombatAnim : MonoBehaviour
{
    [SerializeField] private Animator animator;

    public void PlayAttack()
    {
        animator.SetTrigger("Attack");
    }
}
```

### Pathfinding intent

```csharp
using UnityEngine;
using UnityEngine.AI;

public class PatrolMove : MonoBehaviour
{
    [SerializeField] private Vector3 target;
    private NavMeshAgent agent;

    private void Awake()
    {
        agent = GetComponent<NavMeshAgent>();
    }

    private void Update()
    {
        agent.SetDestination(target);
    }
}
```

### Combat hook

```csharp
using UnityEngine;

public class DamageZone : MonoBehaviour
{
    [SerializeField] private int damage = 10;

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.TryGetComponent(out IDamageable damageable))
        {
            damageable.ApplyDamage(damage);
        }
    }
}
```

### Loot projection

```csharp
using UnityEngine;

[CreateAssetMenu(menuName = "Game/Item")]
public class ItemData : ScriptableObject
{
    public string id;
    public string title;
    public string rarity;
}
```

### Dialogue entry

```csharp
using UnityEngine;

[CreateAssetMenu(menuName = "Game/Dialogue Line")]
public class DialogueLine : ScriptableObject
{
    public string speaker;
    [TextArea] public string text;
}
```

### Quest state

```csharp
using System.Collections.Generic;
using UnityEngine;

public class QuestLog : MonoBehaviour
{
    [SerializeField] private List<string> activeQuests = new();

    public void AddQuest(string questId)
    {
        if (!activeQuests.Contains(questId))
        {
            activeQuests.Add(questId);
        }
    }
}
```

### Crafting flow

```csharp
using UnityEngine;

public class CraftingService : MonoBehaviour
{
    public bool CanCraft(string recipeId)
    {
        return true;
    }
}
```

### Input remap

```csharp
using UnityEngine;
using UnityEngine.InputSystem;

public class RebindMenu : MonoBehaviour
{
    public void Rebind(InputAction action, int bindingIndex, string path)
    {
        action.ApplyBindingOverride(bindingIndex, path);
    }
}
```

### UI menu flow

```csharp
using UnityEngine;

public class MenuPanel : MonoBehaviour
{
    public void Show()
    {
        gameObject.SetActive(true);
    }
}
```

### Status effects

```csharp
using System.Collections.Generic;
using UnityEngine;

public class StatusEffectState : MonoBehaviour
{
    [SerializeField] private List<string> effectIds = new();

    public void Add(string effectId)
    {
        effectIds.Add(effectId);
    }
}
```

### Inventory UI

```csharp
using UnityEngine;
using TMPro;

public class InventoryPanel : MonoBehaviour
{
    [SerializeField] private TMP_Text inventoryText;

    public void Render(IEnumerable<string> items)
    {
        inventoryText.text = string.Join(", ", items);
    }
}
```

### Boss phase state

```csharp
using UnityEngine;

public class BossPhaseState : MonoBehaviour
{
    [SerializeField] private int phase = 1;

    public void SetPhase(int nextPhase)
    {
        phase = nextPhase;
    }
}
```

### Camera shake

```csharp
using UnityEngine;

public class CameraShake : MonoBehaviour
{
    [SerializeField] private Transform cameraRoot;

    public void Shake(float amount)
    {
        cameraRoot.localPosition = new Vector3(Random.Range(-amount, amount), Random.Range(-amount, amount), cameraRoot.localPosition.z);
    }
}
```

### Interaction prompt

```csharp
using UnityEngine;
using TMPro;

public class PromptUI : MonoBehaviour
{
    [SerializeField] private TMP_Text label;

    public void ShowPrompt(string text)
    {
        gameObject.SetActive(true);
        label.text = text;
    }
}
```

### Tutorial gating

```csharp
using System.Collections.Generic;
using UnityEngine;

public class TutorialFlags : MonoBehaviour
{
    private readonly HashSet<string> flags = new();

    public void Unlock(string flag)
    {
        flags.Add(flag);
    }
}
```

### Network state

```csharp
using UnityEngine;

public class NetworkState : MonoBehaviour
{
    [SerializeField] private bool isAuthority;

    public void ApplyNetworkState(bool authority)
    {
        isAuthority = authority;
    }
}
```

### Save migration edge case

```csharp
using UnityEngine;

[System.Serializable]
public class SaveBlob
{
    public int version = 1;
}
```

### Accessibility hook

```csharp
using UnityEngine;
using TMPro;

public class AccessibilitySettings : MonoBehaviour
{
    [SerializeField] private TMP_Text label;

    public void SetLargeText(bool enabled)
    {
        label.fontSize = enabled ? 24f : 16f;
    }
}
```

### Economy / shop

```csharp
using UnityEngine;

public class ShopState : MonoBehaviour
{
    [SerializeField] private int coins;

    public bool CanBuy(int price)
    {
        return coins >= price;
    }
}
```

### Meta progression

```csharp
using System.Collections.Generic;
using UnityEngine;

public class MetaProgression : MonoBehaviour
{
    [SerializeField] private HashSet<string> unlocks = new();

    public void UnlockMeta(string id)
    {
        unlocks.Add(id);
    }
}
```

### Live ops / event flow

```csharp
using UnityEngine;

public class LiveEventState : MonoBehaviour
{
    [SerializeField] private string activeEvent = "";

    public void StartEvent(string eventId)
    {
        activeEvent = eventId;
    }
}
```

### Accessibility options

```csharp
using UnityEngine;
using TMPro;

public class AccessibilityOptions : MonoBehaviour
{
    [SerializeField] private TMP_Text label;
    [SerializeField] private bool subtitles = true;

    public void SetAccessibility(bool largeTextEnabled, bool subtitlesEnabled)
    {
        label.fontSize = largeTextEnabled ? 24f : 16f;
        subtitles = subtitlesEnabled;
    }
}
```

### Economy / shop projection

```csharp
using UnityEngine;

public class EconomyState : MonoBehaviour
{
    [SerializeField] private int coins;

    public bool CanBuy(int price)
    {
        return coins >= price;
    }
}
```

### Meta progression service

```csharp
using System.Collections.Generic;
using UnityEngine;

public class MetaUnlocks : MonoBehaviour
{
    [SerializeField] private HashSet<string> unlocks = new();

    public void UnlockMeta(string id)
    {
        unlocks.Add(id);
    }
}
```

### Live ops event flag

```csharp
using UnityEngine;

public class LiveEventState : MonoBehaviour
{
    [SerializeField] private string liveEventId = "";

    public void SetLiveEvent(string eventId)
    {
        liveEventId = eventId;
    }
}
```

## Common mistakes

- using `Transform` as a data model
- storing run state in `ScriptableObject`
- letting `Collider2D` or `Collider` own the business rule
- writing editor features inside runtime scripts
- using `ObjectPool<T>` without explicit reset rules

## Engine-specific deep dive

### Core runtime

- `GameObject` is the composition shell; `MonoBehaviour` is the behavior; `Transform` is the spatial structure
- scene state should live in components or models, not in the hierarchy shell
- repeated prefab instances should stay authored and predictable

### Editor and tooling

- `EditorWindow` is for workflows, scans, batch operations, and authoring tools
- `Editor` and `CustomEditor` are for object-specific inspector quality
- editor-only code should not leak into runtime assemblies

### Data and persistence

- `ScriptableObject` should own reusable tuning and definition data
- runtime state should live in plain models or services where possible
- persistence should be a projection layer, not a dump of live scene references

### Gameplay and interaction

- `Collider2D` / `Collider` should be the detection input, never the whole mechanic
- `Rigidbody2D` / `Rigidbody` should be used when simulated motion is actually the requirement
- `CharacterController` is a control-movement tool, not a physics body
- `ObjectPool<T>` should be used for high-churn objects with explicit reset rules

### UI

- UI Toolkit is better when the UI is data-heavy or tooling-oriented
- uGUI is still fine for straightforward runtime HUDs and menus
- the UI should project state, not own gameplay authority

### Visuals and animation

- `Animator` should encode visible state and transitions, not the full game rule set
- `ParticleSystem` should be effect feedback, not hidden gameplay ownership
- `SpriteRenderer` and `Prefab` should stay clearly separated from combat logic
- when object count rises, use pooling or instancing before pretending optimization is unnecessary

## What the agent should say

Before implementation, state:

1. which object owns the scene identity
2. which object owns reusable tuning
3. which object owns contact detection
4. which editor surface owns authoring
5. which objects should be pooled
6. what breaks first when the object count grows

## Related docs

- `docs/reference/gpu-guide.md`
- `docs/examples/gpu-example.md`
- `docs/reference/engine-map.md`
- `docs/reference/agent-guide.md`
- `docs/reference/engine-examples.md`
- the matching engine research notes in `docs/research/game-development/engines/`
