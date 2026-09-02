namespace InterestApi;
public static class RegistrationFormatter
{
    public static string ToStorageLine(Registration value) => $"{value.Name}\t{value.Email}\t{value.Course}";
}
