namespace InterestApi;
public static class RegistrationValidator
{
    public static bool IsValid(Registration value) => !string.IsNullOrWhiteSpace(value.Name) && value.Email.Contains('@') && value.Course == "Introduction";
}
