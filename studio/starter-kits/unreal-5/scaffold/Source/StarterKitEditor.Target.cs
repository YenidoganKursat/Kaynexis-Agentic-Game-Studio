using UnrealBuildTool;
using System.Collections.Generic;

public class StarterKitEditorTarget : TargetRules
{
    public StarterKitEditorTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Editor;
        DefaultBuildSettings = BuildSettingsVersion.V5;
        ExtraModuleNames.Add("StarterKit");
    }
}
