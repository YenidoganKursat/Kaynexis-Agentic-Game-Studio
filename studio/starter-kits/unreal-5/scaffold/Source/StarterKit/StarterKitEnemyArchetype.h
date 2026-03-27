#pragma once

#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "StarterKitEnemyArchetype.generated.h"

UCLASS(BlueprintType)
class STARTERKIT_API UStarterKitEnemyArchetype : public UDataAsset
{
    GENERATED_BODY()

public:
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "StarterKit")
    FText DisplayName;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "StarterKit")
    float BaseHealth = 30.0f;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "StarterKit")
    float ContactDamage = 10.0f;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "StarterKit")
    float PulseWindupSeconds = 1.2f;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "StarterKit")
    float PulseRadius = 300.0f;
};
