#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "StarterKitGameModeBase.generated.h"

UCLASS()
class STARTERKIT_API AStarterKitGameModeBase : public AGameModeBase
{
    GENERATED_BODY()

public:
    AStarterKitGameModeBase();

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "StarterKit")
    int32 TargetWaveCount = 1;
};
