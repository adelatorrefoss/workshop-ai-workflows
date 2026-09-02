---
name: CI feedback-loop exercise
about: Normalize course-interest data at the storage boundary
title: "Normalize registration fields before persistence"
labels: enhancement
---

## Acceptance criteria

- Trim Name, Email, and Course before producing the storage line.
- Store Email in lowercase.
- Keep the tab-separated storage format.
- Local validation and full CI must pass without weakening checks.
