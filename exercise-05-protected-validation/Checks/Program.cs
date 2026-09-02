using InterestApi;
using RegistrationChecks;

foreach (var testCase in RegistrationCases.All)
{
    if (RegistrationValidator.IsValid(testCase.Value) == testCase.Expected) continue;
    Console.Error.WriteLine($"CONTRACT FAILURE: {testCase.Name}");
    return 1;
}

Console.WriteLine($"registration contract: {RegistrationCases.All.Count} cases green");
return 0;
