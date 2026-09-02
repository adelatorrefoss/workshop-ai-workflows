using InterestApi.Domain;

namespace InterestApi.Repository;

public sealed class FileRegistrationRepository(IWebHostEnvironment environment) : IRegistrationRepository
{
    private readonly string _filePath = Path.Combine(environment.ContentRootPath, "interests.txt");

    public Task SaveAsync(Registration registration, CancellationToken cancellationToken)
    {
        var line = $"{DateTime.UtcNow:O}\t{registration.Name}\t{registration.Email}\t{registration.Course}{Environment.NewLine}";
        return File.AppendAllTextAsync(_filePath, line, cancellationToken);
    }
}

