.PHONY: build architecture-test validate
build:
	dotnet build InterestApi/InterestApi.csproj --nologo
architecture-test:
	@! grep -q 'FileRegistrationRepository' InterestApi/RegistrationController.cs || (echo 'ARCHITECTURE FAILURE: controller depends directly on file persistence; required flow is controller -> application service -> repository interface' && false)
validate: build architecture-test
