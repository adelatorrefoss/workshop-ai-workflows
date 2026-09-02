namespace InterestApi;
public static class RegistrationValidator { public static bool IsValid(Registration r) => !string.IsNullOrWhiteSpace(r.Name) && r.Email.Contains('@') && !string.IsNullOrWhiteSpace(r.Course); }
