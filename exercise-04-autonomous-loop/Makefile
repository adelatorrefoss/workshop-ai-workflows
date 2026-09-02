.PHONY: build contract-test validate
build:
	dotnet build Checks/Checks.csproj --nologo
contract-test:
	dotnet run --project Checks/Checks.csproj --no-build
validate: build contract-test
