using InterestApi.Domain;

namespace InterestApi.Repository;

public interface IRegistrationRepository
{
    Task SaveAsync(Registration registration, CancellationToken cancellationToken);
}

