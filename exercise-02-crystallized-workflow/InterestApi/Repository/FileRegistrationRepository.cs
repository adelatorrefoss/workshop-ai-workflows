using InterestApi.Domain;
namespace InterestApi.Repository;
public sealed class FileRegistrationRepository(IWebHostEnvironment environment) : IRegistrationRepository
{
    private readonly string _path = Path.Combine(environment.ContentRootPath, "interests.txt");
    public Task SaveAsync(Registration registration, CancellationToken cancellationToken) =>
        File.AppendAllTextAsync(_path, $"{DateTime.UtcNow:O}\t{registration.Name}\t{registration.Email}\t{registration.Course}{Environment.NewLine}", cancellationToken);
}
