using InterestApi;
if (!RegistrationValidator.IsValid(new Registration("Ada", "ada@example.com", "Advanced"))) return 1;
if (RegistrationValidator.IsValid(new Registration("", "bad", ""))) return 1;
Console.WriteLine("examples: green"); return 0;
