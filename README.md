# MCP Student Sandbox

## Overview

This repository contains several Python modules for demonstration and practice purposes.

## Module Descriptions

### `mystery_module.py`
This module implements a **quadratic equation solver**. The function `fn_x(a, b, c)` computes the real roots of the quadratic equation $ax^2 + bx + c = 0$. If the equation has no real roots, it returns `None`.

---

## Summary of Improvements

### Clean Code Refactoring

- **`spaghetti_logic.py`** was refactored to follow clean code principles:
  - Functions now have single responsibilities.
  - Improved naming for clarity.
  - Output, logging, and calculation logic are separated for better maintainability and testability.

### Bug Fixes

- **`failing_calculator.py`**:
  - Fixed a bug where dividing by zero would cause a crash.
  - Now, zero values are skipped with a warning, and an error is raised if all values are zero.
  - Added logging for skipped divisions.

### Security Issue

- **`secret_leak.py`**:
  - Identified a hardcoded AWS secret key, which is a security risk.
  - Recommendation: Remove secrets from source code and use environment variables or a secrets manager instead.

---

## Best Practices

- Avoid hardcoding secrets in code.
- Handle potential runtime errors (like division by zero) gracefully.
- Write modular, testable, and readable code by following clean code principles.
