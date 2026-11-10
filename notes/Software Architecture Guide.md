---
title: "Software Architecture Guide"
url: https://martinfowler.com/architecture/
clipped: 2026-06-17 00:48:03
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - software architecture
  - mvc pattern
  - ui design patterns
  - design principles
related:
  - "[[Software Architecture]]"
  - "[[MVC Pattern]]"
  - "[[UI Design Patterns]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A brief summary of MVC and related user interface patterns, highlighting the separation of domain logic from presentation.
>
> **Key points:**
> - User interface complexity can be managed by dividing software into Model, View, and Controller components.
> - MVC has evolved into variants like MVVM, MVP, and Presentation Model, but all share core separation principles.
> - The key mechanisms are isolating domain logic from views and synchronizing presentation state via the observer pattern.
>
> **Concept links:** [[Software Architecture]], [[MVC Pattern]], [[UI Design Patterns]], [[Design Principles]]
>
> **Suggested connections:**
> - [[Domain Driven Design]] — separating business domains from presentation layers.
> - [[Design Patterns]] — the implementation of Observer and Presentation patterns.
<!-- ai-summary:end -->

# [Software Architecture Guide](https://martinfowler.com/architecture/)

## Digest Summary
Graphical user interfaces increase interaction complexity, requiring architectural strategies to contain it. Simple applications can use a Forms‑and‑Controls pattern, but as the flow grows, developers often adopt Model‑View‑Controller (MVC). MVC is frequently misunderstood and implemented under various names—Application Model, Model‑View‑Presenter, Presentation Model, MVVM—each reflecting nuances but sharing core ideas. The essential principles of MVC are: (1) strict separation of presentation (view) from domain logic (model), and (2) synchronization of presentation state via events, typically employing the observer pattern. This separation isolates UI concerns, facilitates testing, and allows independent evolution of business logic and user interface components.

## Discussion Summary
There is concern that poor software architecture persists and becomes more costly over time, especially when developers lack experience in system design. The prevailing “sort‑of‑works” approach—assembling disparate components without solid foundations—is seen as leading to ongoing, often ineffective, investment in incremental fixes. Additionally, the ease of combining elements using current AI tools is viewed as a factor that could worsen the tendency to adopt ad‑hoc, suboptimal architectures.

---

## Full Article

![](https://martinfowler.com/architecture/)

Graphical User Interfaces provide a rich interaction between the
user and a software system. Such richness is complex to manage, so it's
important to contain that complexity with a thoughtful architecture. The Forms
and Controls pattern works well for systems with a simple flow, but as it
breaks down under the weight of greater complexity, most people turn to
“Model-View-Controller” (MVC). Sadly MVC is one of the most misunderstood
architectural patterns around, and systems using that name display a range of
important differences, sometimes described under names like Application Model,
Model-View-Presenter, Presentation Model, MVVM, and the like. The best way to
think of MVC is as set of principles including the separation of presentation
from domain logic and synchronizing presentation state through events (the
observer pattern).