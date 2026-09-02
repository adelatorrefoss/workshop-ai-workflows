using Microsoft.AspNetCore.Mvc;
namespace InterestApi.Controllers;
[ApiController, Route("api")]
public sealed class RegistrationController : ControllerBase
{
    private readonly FileRegistrationRepository _repository = new();
    [HttpPost("register")]
    public async Task<IActionResult> Register(Registration value) { await _repository.SaveAsync(value); return Created("/api/register", new { status = "ok" }); }
}
