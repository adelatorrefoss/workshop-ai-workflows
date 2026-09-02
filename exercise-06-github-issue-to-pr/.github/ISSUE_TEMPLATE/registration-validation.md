---
name: Registration validation exercise
about: Add an application boundary to interest registration
title: "Validate interest registrations before persistence"
labels: enhancement
---

## Feature

Reject invalid course-interest registrations before writing to `interests.txt`.

## Acceptance criteria

- Name and Course are required after trimming.
- Email must contain one `@` with text on both sides.
- Valid registrations still return HTTP 201 and are saved.
- Invalid registrations return HTTP 400 and are not saved.
- Add executable automated checks.
- `make validate` passes.
