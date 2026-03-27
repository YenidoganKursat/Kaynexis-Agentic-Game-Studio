#include "StarterKitEnemyActor.h"

#include "StarterKitHealthComponent.h"

AStarterKitEnemyActor::AStarterKitEnemyActor()
{
    PrimaryActorTick.bCanEverTick = false;
    HealthComponent = CreateDefaultSubobject<UStarterKitHealthComponent>(TEXT("HealthComponent"));
}
