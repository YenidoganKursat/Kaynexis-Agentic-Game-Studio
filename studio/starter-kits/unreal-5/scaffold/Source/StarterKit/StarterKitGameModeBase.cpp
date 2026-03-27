#include "StarterKitGameModeBase.h"

#include "StarterKitCharacter.h"
#include "StarterKitEnemyActor.h"

AStarterKitGameModeBase::AStarterKitGameModeBase()
{
    TargetWaveCount = 1;
    DefaultPawnClass = AStarterKitCharacter::StaticClass();
    DefaultPlayerClass = AStarterKitCharacter::StaticClass();
    DefaultEnemyClass = AStarterKitEnemyActor::StaticClass();
}
