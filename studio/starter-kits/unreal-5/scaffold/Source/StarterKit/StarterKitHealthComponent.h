#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "StarterKitHealthComponent.generated.h"

UCLASS(ClassGroup=(StarterKit), meta=(BlueprintSpawnableComponent))
class STARTERKIT_API UStarterKitHealthComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UStarterKitHealthComponent();

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "StarterKit")
    float MaxHealth = 30.0f;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "StarterKit")
    float CurrentHealth = 30.0f;

    UFUNCTION(BlueprintCallable, Category = "StarterKit")
    void ResetHealth(float NewMaxHealth);

    UFUNCTION(BlueprintCallable, Category = "StarterKit")
    void ApplyDamage(float Damage);

    UFUNCTION(BlueprintPure, Category = "StarterKit")
    bool IsAlive() const;
};
