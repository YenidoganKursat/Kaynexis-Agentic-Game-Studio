#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "StarterKitCharacter.generated.h"

UCLASS()
class STARTERKIT_API AStarterKitCharacter : public ACharacter
{
    GENERATED_BODY()

public:
    AStarterKitCharacter();

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "StarterKit")
    float MoveSpeed = 650.0f;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "StarterKit")
    float DashDistance = 450.0f;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "StarterKit")
    float DashCooldown = 0.9f;
};
