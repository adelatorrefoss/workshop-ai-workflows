using InterestApi;

namespace RegistrationChecks;

public sealed record RegistrationCase(Registration Value, bool Expected, string Name);

public static class RegistrationCases
{
    public static IReadOnlyList<RegistrationCase> All { get; } =
    [
        new(new Registration("Ada", "ada@example.com", "Advanced"), true, "complete registration"),
        new(new Registration("", "invalid", ""), false, "completely empty registration")
    ];
}
