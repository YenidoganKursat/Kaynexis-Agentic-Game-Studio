# Engine Tool Stubs

These stub executables exist so local evals and CI can verify adapter command contracts
without pretending that a real Unity or Unreal installation is present on the runner.

- `tools/engine-stubs/unity/Unity` is only for Unity adapter dry-run contract checks.
- `tools/engine-stubs/unreal/RunUAT.sh` is only for Unreal adapter dry-run contract checks.

Do not treat these files as real editor integration. Real engine validation still requires:

- `UNITY_CLI` or `tools.unity_cli`
- `UNREAL_UAT` or `UNREAL_EDITOR`
