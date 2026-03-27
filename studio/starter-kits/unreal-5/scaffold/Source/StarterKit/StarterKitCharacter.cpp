#include "StarterKitCharacter.h"

#include "GameFramework/CharacterMovementComponent.h"

AStarterKitCharacter::AStarterKitCharacter()
{
    if (GetCharacterMovement())
    {
        GetCharacterMovement()->MaxWalkSpeed = MoveSpeed;
    }
}
