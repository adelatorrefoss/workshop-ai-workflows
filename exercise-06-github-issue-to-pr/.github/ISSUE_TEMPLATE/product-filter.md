---
name: Product filter exercise
about: Feature request consumed by the coding agent
title: "Add category filtering to the product catalog"
labels: enhancement
---

## Feature

Add support for filtering products by category.

## Acceptance criteria

- `list_products` accepts an optional `category` argument.
- Omitting `category` preserves current behavior.
- A matching category returns only matching products.
- An unknown category returns an empty list.
- Automated tests cover the new behavior.
- `make validate` passes and architecture rules stay green.

