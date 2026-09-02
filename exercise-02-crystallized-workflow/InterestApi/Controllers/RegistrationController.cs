using InterestApi.Domain;
using InterestApi.Repository;
using Microsoft.AspNetCore.Mvc;
namespace InterestApi.Controllers;
[ApiController, Route("api")]
public sealed class RegistrationController(IRegistrationRepository repository) : ControllerBase
{
    [HttpPost("register")]
    public async Task<IActionResult> Register(Registration registration, CancellationToken cancellationToken)
    {
        await repository.SaveAsync(registration, cancellationToken);
        return Created("/api/register", new { status = "ok" });
    }
}
