# Architecture

## Philosophy

Moon Onyx Labs follows a modular, feature-based architecture.

Every feature owns its own backend and frontend components.

---

# Backend

backend/

app/

core/

shared/

features/

prompts/

Each feature contains:

- routes.py
- service.py
- schemas.py

---

# Frontend

src/

components/

features/

lib/

styles/

assets/

Every feature contains:

- Tool Component
- Service
- Output Component

---

# Component Rules

Reusable UI belongs inside:

components/ui/

Reusable layouts belong inside:

components/layout/

Feature-specific UI belongs inside:

features/

---

# API

All backend requests go through:

lib/api.js

No component should directly call fetch().

---

# Git Workflow

Plan

↓

Code

↓

Test

↓

Commit

↓

Push

↓

Next Ticket

---

# Naming

Frontend

PascalCase.svelte

Backend

snake_case.py

Routes

feature_name/routes.py

Services

feature_name/service.py