namespace InterestApi;
public static class RegistrationFormatter
{
    public static string ToStorageLine(Registration value) => $"{value.Name.Trim()}\t{value.Email.Trim()}\t{value.Course.Trim()}";
}
