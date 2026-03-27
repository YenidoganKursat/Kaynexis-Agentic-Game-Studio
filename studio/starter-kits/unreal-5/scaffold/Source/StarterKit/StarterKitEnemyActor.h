#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "StarterKitEnemyActor.generated.h"

class UStarterKitEnemyArchetype;
class UStarterKitHealthComponent;

UCLASS()
class STARTERKIT_API AStarterKitEnemyActor : public AActor
{
    GENERATED_BODY()

public:
    AStarterKitEnemyActor();

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "StarterKit")
    TObjectPtr<UStarterKitEnemyArchetype> Archetype;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "StarterKit")
    TObjectPtr<UStarterKitHealthComponent> HealthComponent;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "StarterKit")
    float PulseWindupSeconds = 1.2f;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "StarterKit")
    float PulseRadius = 300.0f;
};
