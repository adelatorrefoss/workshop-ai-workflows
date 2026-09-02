# Student challenge — Design tests that kill every mutant

Strengthen `Checks/RegistrationCases.cs` so the suite independently protects these rules:

- name is required;
- email syntax is valid;
- course is offered.

For each rule, design a focused case in which only that rule is violated and all unrelated fields remain valid. Every supplied behavioral mutant must be killed while the intended validator continues to pass.

Do not change the production validator, mutation runner, Make targets, or validation requirements. Explain which test kills each mutant and why.
