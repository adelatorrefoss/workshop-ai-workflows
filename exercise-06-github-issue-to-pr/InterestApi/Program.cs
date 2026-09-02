using InterestApi;
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSingleton<RegistrationStore>();
var app = builder.Build();
app.MapPost("/api/register", async (Registration registration, RegistrationStore store) =>
{
    await store.SaveAsync(registration);
    return Results.Created("/api/register", new { status = "ok" });
});
app.Run();
public partial class Program;
