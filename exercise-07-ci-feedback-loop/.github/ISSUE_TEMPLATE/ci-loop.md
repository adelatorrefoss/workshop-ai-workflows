---
name: CI feedback-loop exercise
about: Candidate change whose full contract is checked in CI
title: "Finish robust category filtering"
labels: enhancement
---

## Feature

Finish product filtering by category.

## Acceptance criteria

- Filtering is case-insensitive.
- Missing filters still return all products.
- Unknown categories return an empty list.
- Local validation passes before a pull request is opened.
- Full CI passes without weakening any check.

