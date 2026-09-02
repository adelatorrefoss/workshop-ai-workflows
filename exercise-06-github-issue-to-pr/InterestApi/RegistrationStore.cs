namespace InterestApi;
public sealed class RegistrationStore(IWebHostEnvironment environment)
{
    private readonly string _path = Path.Combine(environment.ContentRootPath, "interests.txt");
    public Task SaveAsync(Registration value) => File.AppendAllTextAsync(_path, $"{DateTime.UtcNow:O}\t{value.Name}\t{value.Email}\t{value.Course}{Environment.NewLine}");
}
