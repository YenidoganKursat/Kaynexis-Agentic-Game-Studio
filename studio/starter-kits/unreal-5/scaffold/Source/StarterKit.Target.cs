using UnrealBuildTool;
using System.Collections.Generic;

public class StarterKitTarget : TargetRules
{
    public StarterKitTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Game;
        DefaultBuildSettings = BuildSettingsVersion.V5;
        ExtraModuleNames.Add("StarterKit");
    }
}
