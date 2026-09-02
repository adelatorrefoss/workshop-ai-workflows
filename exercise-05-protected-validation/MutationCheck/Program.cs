using InterestApi;
using RegistrationChecks;

var mutants = new Dictionary<string, Func<Registration, bool>>
{
    ["name validation removed"] = value => value.Email.Contains('@') && !string.IsNullOrWhiteSpace(value.Course),
    ["email validation removed"] = value => !string.IsNullOrWhiteSpace(value.Name) && !string.IsNullOrWhiteSpace(value.Course),
    ["course validation removed"] = value => !string.IsNullOrWhiteSpace(value.Name) && value.Email.Contains('@')
};

var survivors = mutants
    .Where(mutant => RegistrationCases.All.All(testCase => mutant.Value(testCase.Value) == testCase.Expected))
    .Select(mutant => mutant.Key)
    .ToArray();

if (survivors.Length > 0)
{
    Console.Error.WriteLine("MUTATION FAILURE: tests did not detect: " + string.Join(", ", survivors));
    return 1;
}

Console.WriteLine("mutation protection: all validation mutants detected");
return 0;
