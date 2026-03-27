#include "StarterKitHealthComponent.h"

UStarterKitHealthComponent::UStarterKitHealthComponent()
{
    PrimaryComponentTick.bCanEverTick = false;
}

void UStarterKitHealthComponent::ResetHealth(float NewMaxHealth)
{
    MaxHealth = FMath::Max(1.0f, NewMaxHealth);
    CurrentHealth = MaxHealth;
}

void UStarterKitHealthComponent::ApplyDamage(float Damage)
{
    CurrentHealth = FMath::Max(0.0f, CurrentHealth - FMath::Max(0.0f, Damage));
}

bool UStarterKitHealthComponent::IsAlive() const
{
    return CurrentHealth > 0.0f;
}
