#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "StarterKitGameModeBase.generated.h"

class AStarterKitCharacter;
class AStarterKitEnemyActor;

UCLASS()
class STARTERKIT_API AStarterKitGameModeBase : public AGameModeBase
{
    GENERATED_BODY()

public:
    AStarterKitGameModeBase();

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "StarterKit")
    int32 TargetWaveCount = 1;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "StarterKit")
    TSubclassOf<AStarterKitCharacter> DefaultPlayerClass;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "StarterKit")
    TSubclassOf<AStarterKitEnemyActor> DefaultEnemyClass;
};
