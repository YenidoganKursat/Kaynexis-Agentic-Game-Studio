# Unreal Atlas

This page is the deeper Unreal companion to `engine-map.md` and `engine-atlas.md`.

Use it when an agent needs to know which Unreal class family should own runtime gameplay, shared data, UI, animation, or scalable systems.

This is a core atlas, not every Unreal class.

## Read this with

- `docs/reference/engine-map.md`
- `docs/reference/engine-atlas.md`
- `docs/research/game-development/engines/unreal-map.md`
- `docs/research/game-development/engines/unreal-classes.md`
- `docs/research/game-development/engines/unreal-systems.md`

## Core ownership model

| Family | Runtime owner | Shared data owner | Editor owner | Example use |
| --- | --- | --- | --- | --- |
| Base object | `UObject` | `UDataAsset` / `UPrimaryDataAsset` | Details panel / asset editor | reusable logic, data definitions |
| World entity | `AActor` | asset-backed data | Details panel / Blueprint editor | spawned entities, props, interactables |
| Controlled body | `APawn` / `ACharacter` | data asset / component config | Blueprint editor | controllable units, embodied movement |
| Reusable behavior | `UActorComponent` | config asset | Details panel | health, targeting, sensing, helpers |
| UI | `UUserWidget` | data model / asset | UMG / widget editor | HUD, menus, overlays |
| Match state | `AGameModeBase`, `AGameStateBase`, `APlayerState` | session model | Blueprint / C++ | rules, replicated state, player state |
| Editor flow | Blueprint editor / Details panel | data assets | Editor UI | design-time assembly and tuning |

## Core classes and what they are for

### `UObject`

- What it is: the base Unreal object family
- Good for: reusable runtime logic, data-backed helpers, asset-backed models
- Not good for: acting as the one place everything lives
- Input: asset references, system references, config data
- Output: reusable object behavior or data containers
- Example use: helper object, lightweight model, subsystem-adjacent asset logic

### `AActor`

- What it is: world entity
- Good for: enemies, props, interactables, pickups, spawners
- Not good for: UI ownership or global persistence ownership
- Input: world placement, gameplay events, component events
- Output: world presence, interaction, spawned behavior
- Example use: enemy actor, pickup actor, door actor, hazard actor

### `APawn`

- What it is: possession-capable controllable entity
- Good for: custom player bodies, vehicles, drones, special control units
- Not good for: every actor type
- Input: possession, control input, AI controller behavior
- Output: controllable embodied presence
- Example use: vehicle pawn, drone pawn, special boss-controlled pawn

### `ACharacter`

- What it is: the standard embodied movement actor
- Good for: player movement, humanoid enemies, locomotion-heavy gameplay
- Not good for: UI logic or pure data ownership
- Input: movement, animation state, controller input
- Output: locomotion, collision-aware body, gameplay presence
- Example use: action game player, humanoid enemy, enemy champion

### `UActorComponent`

- What it is: reusable behavior module attached to an actor
- Good for: health, damage, targeting, sensing, inventory helpers, interaction logic
- Not good for: huge monolithic gameplay blobs
- Input: owner actor state, events, tuning
- Output: reusable behavior and state transitions
- Example use: health component, target lock component, interaction component

### `USceneComponent`

- What it is: transform-bearing component
- Good for: attachments, sockets, scene hierarchy within an actor
- Not good for: pure business logic
- Input: parent transform, attachment rules
- Output: spatial placement and attachment
- Example use: weapon socket, camera boom, child visual anchor

### `UWorld`

- What it is: the active runtime world context
- Good for: world-level context and querying subsystems
- Not good for: turning into a hidden global object bag
- Input: level load, gameplay systems
- Output: active world state and context
- Example use: world queries, gameplay subsystem access

### `APlayerController`

- What it is: input and possession routing
- Good for: player input, cursor/UI routing, pawn control
- Not good for: embodying the whole character state
- Input: input device, UI commands, possession changes
- Output: pawn control and player-facing routing
- Example use: menu interaction, possession, camera/input handoff

### `UGameInstance`

- What it is: cross-level runtime context
- Good for: session services, persistent runtime systems
- Not good for: feature-specific state dumping
- Input: startup flow, session data
- Output: cross-level runtime context
- Example use: session service, persistent bootstrapping

### `AGameModeBase`, `AGameStateBase`, `APlayerState`

- What they are: match rules and match state separation
- Good for: authority rules, replicated state, player-specific replicated data
- Not good for: UI ownership or arbitrary game logic dumping
- Input: startup rules, replication, match events
- Output: game rules, match state, player state
- Example use: combat round rules, score state, player status replication

### `UDataAsset` / `UPrimaryDataAsset`

- What they are: shared authored data containers
- Good for: items, abilities, enemies, encounters, tuning packs
- Not good for: live mutable per-run state
- Input: designer-authored content
- Output: reusable tuning and definitions
- Example use: enemy archetype data, item definition, ability data

### `USaveGame`

- What it is: save projection object
- Good for: persistence snapshots, migration data
- Not good for: full runtime authority
- Input: runtime snapshot, migration rules
- Output: serialized save state
- Example use: profile save, checkpoint save, run meta save

### `UUserWidget`

- What it is: runtime UI widget
- Good for: HUD, menus, overlays, prompts
- Not good for: gameplay authority
- Input: projected data, input events, focus state
- Output: visible UI and commands
- Example use: health bar, pause menu, inventory menu, upgrade picker

### Blueprint

- What it is: designer-facing assembly surface
- Good for: prototyping, assembly, reusable content logic
- Not good for: hiding rules so deeply that no one can maintain them
- Input: graph edits, exposed variables, events
- Output: gameplay assembly and authoring-time behavior
- Example use: enemy assembly, interactable setup, UI hookup

### `AnimInstance` and animation blueprints

- What they are: animation logic layer
- Good for: locomotion blends, state-driven animation, pose control
- Not good for: hiding game rules inside animation graphs
- Input: movement parameters, state flags
- Output: visible animation state
- Example use: locomotion blend, hurt reaction, attack montage state

### `SkeletalMeshComponent`

- What it is: animated visible body
- Good for: skinned meshes, attached visuals, animation output
- Not good for: core gameplay rules
- Input: animation data, mesh assets
- Output: visible character body
- Example use: player character mesh, enemy body mesh

### `Niagara`

- What it is: scalable VFX system
- Good for: combat feedback, ambiance, impact effects
- Not good for: gameplay logic authority
- Input: effect triggers, parameter data
- Output: scalable VFX
- Example use: dash trail, damage burst, impact sparks

## GPU and render-scale family

| Family | Runtime / render owner | Shared data owner | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| Instanced geometry | `Instanced Static Mesh Component` | Data Asset | repeated geometry at lower CPU cost | do not use Actor-per-instance scale when instancing is enough |
| Virtualized detail | Nanite | Data Asset / content settings | high-count geometry without manual draw-call management | do not assume Nanite removes all render pressure |
| Visibility reduction | HLOD | world/content data | distant aggregation and scale reduction | do not use it when the scene is not large enough to need it |
| GPU proof path | RenderDoc / GPU profiling tools | session notes / profiling capture | measured render bottleneck evidence | do not optimize GPU systems without a capture or trace |

## Systems that matter when the project scales

- Gameplay Ability System for ability/status-heavy projects
- StateTree for structured state control
- Behavior Tree for AI structure
- EQS for tactical queries
- AI Perception for sensing
- Navmesh for pathing

## Common Unreal mechanic patterns

| Mechanic | Likely owner | Example class pair | Common mistake |
| --- | --- | --- | --- |
| Movement | embodiment class | `ACharacter` + `UCharacterMovementComponent` | mixing UI and gameplay authority into the character |
| Pickup | actor + component + data asset | `AActor` + `UActorComponent` + `UPrimaryDataAsset` | letting the actor own the entire inventory model |
| HUD | widget | `UUserWidget` + game state | widget owns combat authority |
| Enemy behavior | actor + component + AI system | `AActor` + `UActorComponent` + Behavior Tree | stuffing all behavior into one blueprint |
| Ability-heavy gameplay | ability framework | GAS + `UPrimaryDataAsset` | building parallel custom logic and GAS without a plan |
| VFX | Niagara + animation | `Niagara` + `AnimInstance` | using VFX as hidden gameplay state |

## Typical input/output contracts

- `AActor` inputs world events and component events, outputs world presence
- `UActorComponent` inputs owner state and tuning, outputs reusable behavior
- `ACharacter` inputs control/movement, outputs locomotion and combat presence
- `UDataAsset` inputs authored tuning, outputs reusable definitions
- `UUserWidget` inputs projected data and UI events, outputs UI and commands

## Best first examples

- `ACharacter` + `UActorComponent` for movement and health
- `UPrimaryDataAsset` for item/enemy/ability definitions
- `UUserWidget` for HUD and menus
- Blueprint for designer-friendly assembly
- GAS only when the mechanics need rich effects/status handling

## Example snippets

### Movement and contact

```cpp
void AMyCharacter::MoveForward(float Value)
{
    if (Controller && Value != 0.0f)
    {
        AddMovementInput(GetActorForwardVector(), Value);
    }
}
```

### Pickup detection

```cpp
void APickupActor::NotifyActorBeginOverlap(AActor* OtherActor)
{
    if (UInventoryComponent* Inventory = OtherActor->FindComponentByClass<UInventoryComponent>())
    {
        Inventory->AddItem(ItemData);
        Destroy();
    }
}
```

### HUD projection

```cpp
void UHealthWidget::SetHealth(int32 Current, int32 Max)
{
    HealthText->SetText(FText::Format(
        FText::FromString(TEXT("{0} / {1}")),
        FText::AsNumber(Current),
        FText::AsNumber(Max)
    ));
}
```

## Additional snippets

### Inventory model

```cpp
UCLASS(ClassGroup=(Custom), meta=(BlueprintSpawnableComponent))
class UInventoryComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    TArray<FName> ItemIds;

    void AddItem(FName ItemId)
    {
        ItemIds.Add(ItemId);
    }
};
```

### Enemy chase

```cpp
void AEnemyCharacter::Tick(float DeltaSeconds)
{
    Super::Tick(DeltaSeconds);

    if (TargetActor)
    {
        const FVector Direction = (TargetActor->GetActorLocation() - GetActorLocation()).GetSafeNormal();
        AddMovementInput(Direction);
    }
}
```

### Camera follow

```cpp
void AMyPlayerCameraManager::UpdateViewTarget(FTViewTarget& OutVT, float DeltaTime)
{
    Super::UpdateViewTarget(OutVT, DeltaTime);
    // Keep camera behavior explicit and separate from character authority.
}
```

### Save projection

```cpp
UCLASS()
class UMySaveGame : public USaveGame
{
    GENERATED_BODY()

public:
    UPROPERTY()
    int32 HP = 100;

    UPROPERTY()
    TArray<FName> ItemIds;
};
```

### Skill tree choice

```cpp
UCLASS(BlueprintType)
class USkillNodeData : public UPrimaryDataAsset
{
    GENERATED_BODY()

public:
    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    FName Id;

    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    FText Label;
};
```

### UI flow

```cpp
void UUpgradeWidget::ShowPanel()
{
    SetVisibility(ESlateVisibility::Visible);
}
```

### Animation trigger

```cpp
void UMyAnimInstance::TriggerAttack()
{
    Montage_Play(AttackMontage);
}
```

### Pathfinding intent

```cpp
void AEnemyAIController::ChaseTarget(APawn* TargetPawn)
{
    if (TargetPawn)
    {
        MoveToActor(TargetPawn);
    }
}
```

### Combat hook

```cpp
void ADamageZone::NotifyActorBeginOverlap(AActor* OtherActor)
{
    if (UHealthComponent* Health = OtherActor->FindComponentByClass<UHealthComponent>())
    {
        Health->ApplyDamage(10);
    }
}
```

### Loot projection

```cpp
UCLASS(BlueprintType)
class UItemData : public UPrimaryDataAsset
{
    GENERATED_BODY()

public:
    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    FName Id;

    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    FText Title;
};
```

### Dialogue entry

```cpp
UCLASS(BlueprintType)
class UDialogueLine : public UPrimaryDataAsset
{
    GENERATED_BODY()

public:
    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    FText Speaker;

    UPROPERTY(EditAnywhere, BlueprintReadOnly)
    FText Text;
};
```

### Quest state

```cpp
UCLASS()
class UQuestLogComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    TArray<FName> ActiveQuests;
};
```

### Crafting flow

```cpp
UCLASS()
class UCraftingComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    bool CanCraft(FName RecipeId) const
    {
        return true;
    }
};
```

### Input remap

```cpp
void URebindWidget::SetInputMapping(const FName ActionName, const FKey NewKey)
{
    // Keep remap state explicit and persistent.
}
```

### UI menu flow

```cpp
void UMenuWidget::ShowMenu()
{
    SetVisibility(ESlateVisibility::Visible);
}
```

### Status effects

```cpp
UCLASS()
class UStatusEffectComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    TArray<FName> EffectIds;
};
```

### Inventory UI

```cpp
void UInventoryWidget::RenderInventory(const TArray<FName>& ItemIds)
{
    // Project inventory data into the UI only.
}
```

### Boss phase state

```cpp
UCLASS()
class ABossActor : public AActor
{
    GENERATED_BODY()

public:
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    int32 Phase = 1;
};
```

### Camera shake

```cpp
void AMyPlayerCameraManager::TriggerShake(float Amount)
{
    // Keep shake ownership in camera/presentation, not combat core.
}
```

### Interaction prompt

```cpp
void UInteractionWidget::ShowPrompt(const FText& Text)
{
    // Update prompt projection only.
}
```

### Tutorial gating

```cpp
UCLASS()
class UTutorialStateComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    TSet<FName> UnlockedFlags;
};
```

### Network state

```cpp
UCLASS()
class UNetworkStateComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    bool bIsAuthority = false;
};
```

### Save migration edge case

```cpp
UCLASS()
class UMySaveBlob : public USaveGame
{
    GENERATED_BODY()

public:
    UPROPERTY()
    int32 Version = 1;
};
```

### Accessibility hook

```cpp
void UAccessibilityWidget::SetLargeText(bool bEnabled)
{
    // Adjust presentation only.
}
```

### Economy / shop

```cpp
UCLASS()
class UShopComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    int32 Coins = 0;
};
```

### Meta progression

```cpp
UCLASS()
class UMetaProgressionComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    TSet<FName> Unlocks;
};
```

### Live ops / event flow

```cpp
UCLASS()
class ULiveEventStateComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    FName ActiveEvent;
};
```

### Accessibility options

```cpp
UCLASS()
class UAccessibilityStateComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    bool bLargeText = false;

    UPROPERTY()
    bool bSubtitles = true;
};
```

### Economy / shop projection

```cpp
UCLASS()
class UEconomyComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    int32 Coins = 0;
};
```

### Meta progression service

```cpp
UCLASS()
class UMetaProgressionComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    TSet<FName> Unlocks;
};
```

### Live ops event flag

```cpp
UCLASS()
class ULiveEventStateComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UPROPERTY()
    FName LiveEventId;
};
```

## Common mistakes

- using `UObject` as a trash can for unrelated state
- putting save data directly into live world actors
- letting widgets own gameplay authority
- hiding too much logic in Blueprint graphs without a maintenance plan
- using GAS when the mechanic is simple enough to stay simple

## Engine-specific deep dive

### Core runtime

- `AActor` owns world presence; `UActorComponent` owns reusable behavior; `ACharacter` owns standard embodied movement
- `APawn` is for possession-based control when the standard character path is not the right fit
- `UWorld` and `UGameInstance` are context layers, not places to dump every feature

### Editor and tooling

- Blueprint should stay designer-friendly and readable, not a hidden architecture maze
- Details panel configuration should be used for the values that designers actually need to tune
- if a task is about authoring or review, prefer asset editing or Blueprint assembly over writing more runtime state

### Data and persistence

- `UDataAsset` and `UPrimaryDataAsset` should hold reusable tuning and definitions
- `USaveGame` should represent projection, migration, and persistence boundaries
- live world actors should not become the save system itself

### Gameplay and interaction

- `UActorComponent` should own health, targeting, sensing, interaction, and similar reusable behavior
- AI choice should be explicit about whether it uses Behavior Tree, StateTree, EQS, or a justified custom graph
- `APlayerController` should manage input and possession, not the full character state

### UI

- `UUserWidget` should own screen projection and menu interaction
- HUD should read from game state and never become the combat authority
- if a flow needs player control, say whether it lives in controller, pawn, or widget

### Visuals and animation

- `AnimInstance` and animation blueprints should handle pose and visible state
- `SkeletalMeshComponent` should be visual embodiment, not a rule engine
- `Niagara` should be used for high-quality feedback and scale, not gameplay logic
- if a feature becomes crowded, consider whether Actor-based ownership is still the right scale lever

## What the agent should say

Before implementation, state:

1. which actor or component owns runtime state
2. which asset owns reusable tuning
3. which widget owns presentation
4. which class owns possession or control
5. which system owns AI or effects
6. what breaks first when the world scales

## Related docs

- `docs/reference/gpu-guide.md`
- `docs/examples/gpu-example.md`
- `docs/reference/engine-map.md`
- `docs/reference/agent-guide.md`
- `docs/reference/engine-examples.md`
- the matching engine research notes in `docs/research/game-development/engines/`
