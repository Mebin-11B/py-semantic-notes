---
title: "Show HN: Oxyde – Pydantic-native async ORM with a Rust core"
url: https://github.com/mr-fatalyst/oxyde
clipped: 2026-06-17 01:31:53
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Show HN: Oxyde – Pydantic-native async ORM with a Rust core](https://github.com/mr-fatalyst/oxyde)

## Digest Summary
Oxyde ORM is an asynchronous, type‑safe ORM built around Pydantic v2 models and a Rust‑based SQL engine. It offers a Django‑style API (e.g., Model.objects.filter()), strong typing, full validation, and serialization. The core generates and executes queries in native Rust for high performance and supports PostgreSQL, SQLite, and MySQL. Features include async‑first operation with asyncio, transaction management via a transaction.atomic() context manager with savepoints, and Django‑style makemigrations/migrate CLI for schema migrations. Example usage demonstrates initializing the database, creating, reading, updating, and deleting records, and integrating with FastAPI via a lifespan hook. An auto‑generated admin panel provides CRUD, search, filters, and export for frameworks such as FastAPI, Litestar, Sanic, Quart, and Falcon. Benchmarks compare Oxyde’s operations per second against other Python ORMs. The project is under active development, MIT‑licensed, and welcomes contributions through GitHub issues and pull requests.

## Discussion Summary
The discussion centers on separating API models from database schemas, with many expressing confusion over perceived duplication but acknowledging they serve distinct roles. Participants highlight enthusiasm for a Rust‑backed solution that generates type‑safe SQL, noting speed as a side effect and appreciating built‑in Pydantic integration and admin features. There is optimism about filling a gap in Python’s ORM ecosystem, comparisons to Prisma, and hopes it could rival Django’s ORM, while some raise concerns about naming, production readiness, and limitations of existing tools like SQLModel.

---

## Full Article

[![Logo](https://raw.githubusercontent.com/mr-fatalyst/oxyde/master/logo.png)](https://raw.githubusercontent.com/mr-fatalyst/oxyde/master/logo.png)

**Oxyde ORM** is a type-safe, Pydantic-centric asynchronous ORM with a high-performance Rust core designed for clarity, speed, and reliability.

Inspired by the elegance of [Django's ORM](https://www.djangoproject.com/), Oxyde focuses on explicitness over magic, providing a modern developer-friendly workflow with predictable behavior and strong typing throughout.

[![](https://camo.githubusercontent.com/c3285ef5aed0ce9efcac90de4ffbaf1c7e2d0d0e8b1efd5f7deac69d461ef419/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6d722d666174616c7973742f6f78796465)](https://camo.githubusercontent.com/c3285ef5aed0ce9efcac90de4ffbaf1c7e2d0d0e8b1efd5f7deac69d461ef419/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6d722d666174616c7973742f6f78796465)
[![](https://github.com/mr-fatalyst/oxyde/actions/workflows/test.yml/badge.svg)](https://github.com/mr-fatalyst/oxyde/actions/workflows/test.yml/badge.svg)
[![](https://camo.githubusercontent.com/426d21a29c419b6c8c2bf978745b9537236ecf6479276f781f91f47fcd42c17b/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f6f78796465)](https://camo.githubusercontent.com/426d21a29c419b6c8c2bf978745b9537236ecf6479276f781f91f47fcd42c17b/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f6f78796465)
[![](https://camo.githubusercontent.com/8519e1babfc867a542918eb31c4d492bd67898840e26d6594c2c93ab5f682651/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6f78796465)](https://camo.githubusercontent.com/8519e1babfc867a542918eb31c4d492bd67898840e26d6594c2c93ab5f682651/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6f78796465)
[![PyPI Downloads](https://camo.githubusercontent.com/e0cf7923dc46af8ca647a5b6e1fb57eccbe30b025b219fc614fa557ffe8eb3b1/68747470733a2f2f7374617469632e706570792e746563682f62616467652f6f78796465)](https://camo.githubusercontent.com/e0cf7923dc46af8ca647a5b6e1fb57eccbe30b025b219fc614fa557ffe8eb3b1/68747470733a2f2f7374617469632e706570792e746563682f62616467652f6f78796465)

---

> **Heads up!** Oxyde is a young project under active development. The API may evolve between minor versions. Feedback, bug reports, and ideas are very welcome. Feel free to [open an issue](https://github.com/mr-fatalyst/oxyde/issues)!

* **Django-style API** — Familiar `Model.objects.filter()` syntax
* **Pydantic v2 models** — Full validation, type hints, serialization
* **Async-first** — Built for modern async Python with `asyncio`
* **Rust performance** — SQL generation and execution in native Rust
* **Multi-database** — PostgreSQL, SQLite, MySQL support
* **Transactions** — `transaction.atomic()` context manager with savepoints
* **Migrations** — Django-style `makemigrations` and `migrate` CLI

Benchmarks vs popular Python ORMs (avg ops/sec, higher is better):

| Database | Oxyde | Tortoise | Piccolo | Django | SQLAlchemy | SQLModel | Peewee |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PostgreSQL | 1,475 | 888 | 932 | 736 | 445 | 431 | 80 |
| MySQL | 1,239 | 794 | — | 714 | 536 | 505 | 461 |
| SQLite | 2,525 | 1,882 | 469 | 1,294 | 588 | 567 | 548 |

Full benchmark report: **[Documentation](https://oxyde.fatalyst.dev/latest/advanced/benchmarks/)**

This creates `oxyde_config.py` with your database settings and model paths.

```
# models.py
from oxyde import Model, Field

class User(Model):
    id: int | None = Field(default=None, db_pk=True)
    name: str
    email: str = Field(db_unique=True)
    age: int | None = Field(default=None)

    class Meta:
        is_table = True
```

```
oxyde makemigrations
oxyde migrate
```

```
import asyncio
from oxyde import db
from models import User

async def main():
    await db.init(default="sqlite:///app.db")

    # Create
    user = await User.objects.create(name="Alice", email="alice@example.com", age=30)

    # Read
    users = await User.objects.filter(age__gte=18).all()
    user = await User.objects.get(id=1)

    # Update
    user.age = 31
    await user.save()

    # Delete
    await user.delete()

    await db.close()

asyncio.run(main())
```

```
from oxyde.db import transaction

async with transaction.atomic():
    user = await User.objects.create(name="Alice", email="alice@example.com")
    await Profile.objects.create(user_id=user.id)
    # Auto-commits on success, rolls back on exception
```

```
from fastapi import FastAPI
from oxyde import db

app = FastAPI(
    lifespan=db.lifespan(
        default="postgresql://localhost/mydb",
    )
)

@app.get("/users")
async def get_users():
    return await User.objects.filter(is_active=True).all()
```

| Database | Min Version | Status | Notes |
| --- | --- | --- | --- |
| PostgreSQL | 12+ | Full | RETURNING, UPSERT, FOR UPDATE/SHARE, JSON, Arrays |
| SQLite | 3.35+ | Full | RETURNING, UPSERT, WAL mode by default |
| MySQL | 8.0+ | Full | UPSERT via ON DUPLICATE KEY, FOR UPDATE/SHARE |

**Connection URLs:**

```
postgresql://user:password@localhost:5432/database
sqlite:///path/to/database.db
sqlite:///:memory:
mysql://user:password@localhost:3306/database
```

Auto-generated admin panel for Oxyde ORM with zero boilerplate.

* Automatic CRUD, search, filters, export
* FastAPI, Litestar, Sanic, Quart, Falcon
* Theming, authentication, bulk operations

[GitHub →](https://github.com/mr-fatalyst/oxyde-admin)

Full documentation: **<https://oxyde.fatalyst.dev/>**

If you have suggestions or find a bug, please open an issue or create a pull request on GitHub.

This project is licensed under the terms of the MIT license.