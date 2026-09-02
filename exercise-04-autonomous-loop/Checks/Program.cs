using InterestApi;
var cases = new[] {
    (new Registration("Ada", "ada@example.com", "Introduction"), true, "intro registration"),
    (new Registration("Lin", "lin@example.com", "Advanced"), true, "advanced registration"),
    (new Registration("", "ada@example.com", "Introduction"), false, "blank name"),
    (new Registration("Ada", "not-an-email", "Introduction"), false, "invalid email"),
    (new Registration("Ada", "ada@example.com", "Unknown"), false, "unknown course")
};
foreach (var (value, expected, name) in cases) if (RegistrationValidator.IsValid(value) != expected) { Console.Error.WriteLine($"VALIDATION FAILURE: {name}"); return 1; }
Console.WriteLine("registration contract: green"); return 0;
