.PHONY: build test mutation-test validate
build:
	dotnet build Checks/Checks.csproj --nologo
test: build
	dotnet run --project Checks/Checks.csproj --no-build
mutation-test:
	dotnet run --project MutationCheck/MutationCheck.csproj
validate: test mutation-test
