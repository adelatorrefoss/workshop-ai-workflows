.PHONY: build validate ci-validate
build:
	dotnet build LocalChecks/LocalChecks.csproj --nologo
validate: build
	dotnet run --project LocalChecks/LocalChecks.csproj --no-build
ci-validate: validate
	dotnet run --project CiChecks/CiChecks.csproj
