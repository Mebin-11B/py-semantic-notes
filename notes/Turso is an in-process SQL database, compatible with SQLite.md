---
title: "Turso is an in-process SQL database, compatible with SQLite"
url: https://github.com/tursodatabase/turso
clipped: 2026-06-17 01:54:53
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Turso is an in-process SQL database, compatible with SQLite](https://github.com/tursodatabase/turso)

## Digest Summary
The repository “tursodatabase/turso” on GitHub provides Turso, an in‑process SQL database that is compatible with SQLite. The page displays a notice stating “You can’t perform that action at this time,” indicating a temporary access restriction. Visual assets referenced include: Turso Database logo, a crate icon (likely for Rust packaging), NPM badge (JavaScript/Node.js), PyPI badge (Python), Maven Central badge (Java), and two Discord community links—one for chatting with core developers and another for broader user discussions. No additional technical documentation, code examples, or usage instructions are present in the provided excerpt.

## Discussion Summary
The comments express mixed reactions, noting that the project still lacks key SQLite features such as savepoints, window functions, and database attachment, which raises doubts about its readiness. Some view a focus on unique capabilities—like supporting multiple writers or targeting OLAP scenarios—as more marketable than simply branding it as a SQLite successor. Praise is directed toward SQLite’s long‑standing impact and its creator, while interest is shown in the Rust‑based rewrite and its active development. Skepticism remains about its necessity and language‑specific suitability.

---

## Full Article

[![Turso Database](https://github.com/tursodatabase/turso/raw/main/assets/turso.png)](https://github.com/tursodatabase/turso/blob/main/assets/turso.png)

An in-process SQL database, compatible with SQLite.

[![](https://camo.githubusercontent.com/ff712fe49214bd1cf4dd85034a36e6e7423aa21656efda1563b6c48afcf8aec4/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f747572736f64617461626173652f747572736f2f727573742e796d6c3f7374796c653d666c61742d737175617265)](https://github.com/tursodatabase/turso/actions/workflows/rust.yml "Build Status")
[![](https://camo.githubusercontent.com/ab68bfccd640e62f2b215dc54144c5835c3b95ca982aeef2dbf097645cba7b3b/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f747572736f64617461626173652f747572736f3f7374796c653d666c61742d73717561726526636f6c6f723d394346)](https://github.com/tursodatabase/turso/releases "Releases")
[![Crate](https://camo.githubusercontent.com/a4563e7545f96f3e9571677eb66a88bcdfaff5260cd36cd0c7907f524c4197a1/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f762f747572736f)](https://crates.io/crates/turso "Rust")
[![NPM](https://camo.githubusercontent.com/176933117f1c7284c86cd5e4261ace72eef769e20cdaca8ece2019cb959dc96f/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f40747572736f64617461626173652f6461746162617365)](https://www.npmjs.com/package/@tursodatabase/database "JavaScript")
[![PyPI](https://camo.githubusercontent.com/51b52c3d438bd66c4b93a04fcbac22c8f51485c425d9b5de23abf0641ed35574/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f7079747572736f)](https://pypi.org/project/pyturso/ "Python")
[![Maven Central](https://camo.githubusercontent.com/2970c51924b29ff639a6f2d99955de3d1ea9ea714b4540550970e9d701a774a8/68747470733a2f2f696d672e736869656c64732e696f2f6d6176656e2d63656e7472616c2f762f746563682e747572736f2f747572736f)](https://central.sonatype.com/artifact/tech.turso/turso "Java")
[![](https://camo.githubusercontent.com/9ee8e115515de98f82b9fbadb064301b9f24c1fe008ce54c66cecf15d69b23eb/687474703a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d6f72616e67652e7376673f7374796c653d666c61742d737175617265)](https://github.com/tursodatabase/turso/blob/main/LICENSE.md "MIT")
  
[![](https://camo.githubusercontent.com/bc1cc04bf972e3e3aee415d4eef1c159127972c7a1645a990055ecae5500a6ee/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d70722d636c6f7365642f747572736f64617461626173652f747572736f2e7376673f7374796c653d666c61742d73717561726526636f6c6f723d464639393636)](https://github.com/tursodatabase/turso/pulls "GitHub Pull Requests")
[![](https://camo.githubusercontent.com/aa3464fa37f57d6c4b2e261be6946338a5a5b63c1528afd7edfea9182dfb7a10/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6d6d69742d61637469766974792f6d2f747572736f64617461626173652f747572736f2e7376673f7374796c653d666c61742d737175617265)](https://github.com/tursodatabase/turso/commits/main "GitHub Commits")
[![](https://camo.githubusercontent.com/856a7f3112cc451695a9393627a2f71e3aa97b0e1cde57846e857dd37566f684/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f747572736f64617461626173652f747572736f2e7376673f7374796c653d666c61742d73717561726526636f6c6f723d464639393030)](https://github.com/tursodatabase/turso/commits/main "Last Commit")

[![Chat with the Core Developers on Discord](https://camo.githubusercontent.com/ee5f773bfe0bf3cce2f8cbf7ada150778ced9b4ed68520aefedb2a1d3fe66e74/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f313235383635383832363235373936313032303f6c6162656c3d446973636f7264266c6f676f3d446973636f7264267374796c653d736f6369616c266c6162656c3d436f7265253230446576656c6f70657273)](https://discord.gg/jgjmyYgHwB "Developer's Discord")

[![Chat with other users of Turso (and Turso Cloud) on Discord](https://camo.githubusercontent.com/1ac5a7dfb08496ea5a6fffdaab732c2f7e9415fc67f29942d159dac45a4f4304/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3933333037313136323638303935383938363f6c6162656c3d446973636f7264266c6f676f3d446973636f7264267374796c653d736f6369616c266c6162656c3d5573657273)](https://tur.so/discord "Users's Discord")

---

Turso Database is an in-process SQL database written in Rust, compatible with SQLite.

> **⚠️ Warning:** This software is in BETA. It may still contain bugs and unexpected behavior. Use caution with production data and ensure you have backups.

* **SQLite compatibility** for SQL dialect, file formats, and the C API [see [document](https://github.com/tursodatabase/turso/blob/main/COMPAT.md) for details]
* **`BEGIN CONCURRENT`** for improved write throughput using multi-version concurrency control (MVCC).
* **Change data capture (CDC)** for real-time tracking of database changes.
* **Multi-language support** for
* **Asynchronous I/O** support on Linux with `io_uring`
* **Cross-platform** support for Linux, macOS, Windows and browsers (through WebAssembly)
* **Vector support** support including exact search and vector manipulation
* **Improved schema management** including extended `ALTER` support and faster schema changes.

The database has the following experimental features:

* **Encryption at rest** for protecting the data locally.
* **Incremental computation** using DBSP for incremental view maintenance and query subscriptions.
* **Full-Text-Search** powered by the awesome [tantivy](https://github.com/quickwit-oss/tantivy) library
* **Multi-process WAL coordination** via the `.tshm` sidecar for cross-process WAL readers and writers.

The following features are on our current roadmap:

Please see the [Turso Database Manual](https://github.com/tursodatabase/turso/blob/main/docs/manual.md) for more information.

💻 Command Line
  
You can install the latest `turso` release with:

```
curl --proto '=https' --tlsv1.2 -LsSf \
  https://github.com/tursodatabase/turso/releases/latest/download/turso_cli-installer.sh | sh
```

Then launch the interactive shell:

This will start the Turso interactive shell where you can execute SQL statements:

```
Turso
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database
turso> CREATE TABLE users (id INT, username TEXT);
turso> INSERT INTO users VALUES (1, 'alice');
turso> INSERT INTO users VALUES (2, 'bob');
turso> SELECT * FROM users;
1|alice
2|bob
```

You can also build and run the latest development version with:

If you like docker, we got you covered. Simply run this in the root folder:

```
make docker-cli-build && \
make docker-cli-run
```


🦀 Rust
  

Example usage:

```
let db = Builder::new_local("sqlite.db").build().await?;
let conn = db.connect()?;

let res = conn.query("SELECT * FROM users", ()).await?;
```


✨ JavaScript
  

```
npm i @tursodatabase/database
```

Example usage:

```
import { connect } from '@tursodatabase/database';

const db = await connect('sqlite.db');
const stmt = db.prepare('SELECT * FROM users');
const users = stmt.all();
console.log(users);
```


🐍 Python
  

Example usage:

```
import turso

con = turso.connect("sqlite.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM users")
print(res.fetchone())
```


🦫 Go
  

```
go get turso.tech/database/tursogo
go install turso.tech/database/tursogo
```

Example usage:

```
import (
    "database/sql"
    _ "turso.tech/database/tursogo"
)

conn, _ = sql.Open("turso", "sqlite.db")
defer conn.Close()

stmt, _ := conn.Prepare("select * from users")
defer stmt.Close()

rows, _ = stmt.Query()
for rows.Next() {
    var id int
    var username string
    _ := rows.Scan(&id, &username)
    fmt.Printf("User: ID: %d, Username: %s\n", id, username)
}
```


️#️⃣ .NET
  

Example usage:

```
using Turso;

using var connection = new TursoConnection("Data Source=:memory:");
connection.Open();

connection.ExecuteNonQuery("CREATE TABLE t(a, b)");
var rowsAffected = connection.ExecuteNonQuery("INSERT INTO t(a, b) VALUES (1, 2), (3, 4)");
Console.WriteLine($"RowsAffected: {rowsAffected}");

using var command = connection.CreateCommand();
command.CommandText = "SELECT * FROM t";
using var reader = command.ExecuteReader();
while (reader.Read())
{
    var a = reader.GetInt32(0);
    var b = reader.GetInt32(1);
    Console.WriteLine($"Value1: {a}, Value2: {b}");
}
```


☕️ Java
  

We integrated Turso Database into JDBC. For detailed instructions on how to use Turso Database with java, please refer to
the [README.md under bindings/java](https://github.com/tursodatabase/turso/blob/main/bindings/java/README.md).


🤖 MCP Server Mode
  

The Turso CLI includes a built-in [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that allows AI assistants to interact with your databases.

Start the MCP server with:

```
tursodb your_database.db --mcp
```

Add Turso to your MCP client configuration:

```
{
  "mcpServers": {
    "turso": {
      "command": "/path/to/.turso/tursodb",
      "args": ["/path/to/your/database.db", "--mcp"]
    }
  }
}
```

The MCP server provides nine tools for database interaction:

1. **`open_database`** - Open a new database
2. **`current_database`** - Describe the current database
3. **`list_tables`** - List all tables in the database
4. **`describe_table`** - Describe the structure of a specific table
5. **`execute_query`** - Execute read-only SELECT queries
6. **`insert_data`** - Insert new data into tables
7. **`update_data`** - Update existing data in tables
8. **`delete_data`** - Delete data from tables
9. **`schema_change`** - Execute schema modification statements (CREATE TABLE, ALTER TABLE, DROP TABLE)

Once connected, you can ask your AI assistant:

* "Show me all tables in the database"
* "What's the schema for the users table?"
* "Find all posts with more than 100 upvotes"
* "Insert a new user with name 'Alice' and email '[alice@example.com](mailto:alice@example.com)'"

Claude Code

If you're using [Claude Code](https://claude.ai/code), you can easily connect to your Turso MCP server using the built-in MCP management commands:

1. **Add the MCP server** to Claude Code:

   ```
   claude mcp add my-database -- tursodb ./path/to/your/database.db --mcp
   ```
2. **Restart Claude Code** to activate the connection
3. **Start querying** your database through natural language!

```
claude mcp add my-database -- tursodb ./path/to/your/database.db --mcp
#              ↑            ↑       ↑                           ↑
#              |            |       |                           |
#              Name         |       Database path               MCP flag
#                          Separator
```

* **`my-database`** - Choose any name for your MCP server
* **`--`** - Required separator between Claude options and your command
* **`tursodb`** - The Turso database CLI
* **`./path/to/your/database.db`** - Path to your SQLite database file
* **`--mcp`** - Enables MCP server mode

```
# For a local project database
cd /your/project
claude mcp add my-project-db -- tursodb ./data/app.db --mcp

# For an absolute path
claude mcp add analytics-db -- tursodb /Users/you/databases/analytics.db --mcp

# For a specific project (local scope)
claude mcp add project-db --local -- tursodb ./database.db --mcp
```

```
# List all configured MCP servers
claude mcp list

# Get details about a specific server
claude mcp get my-database

# Remove an MCP server
claude mcp remove my-database
```


Claude Desktop

For Claude Desktop, add the configuration to your `claude_desktop_config.json` file:

```
{
  "mcpServers": {
    "turso": {
      "command": "/path/to/.turso/tursodb",
      "args": ["./path/to/your/database.db.db", "--mcp"]
    }
  }
}
```


Cursor

For Cursor, configure MCP in your settings:

1. Open Cursor settings
2. Navigate to Extensions → MCP
3. Add a new server with:
   * **Name**: `turso`
   * **Command**: `/path/to/.turso/tursodb`
   * **Args**: `["./path/to/your/database.db.db", "--mcp"]`

Alternatively, you can add it to your Cursor configuration file directly.

The MCP server runs as a single process that handles multiple JSON-RPC requests over stdin/stdout. Here's how to interact with it directly:

#### Example with In-Memory Database

```
cat << 'EOF' | tursodb --mcp
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}
{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "schema_change", "arguments": {"query": "CREATE TABLE users (id INTEGER, name TEXT, email TEXT)"}}}
{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_tables", "arguments": {}}}
{"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "insert_data", "arguments": {"query": "INSERT INTO users VALUES (1, 'Alice', 'alice@example.com')"}}}
{"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "execute_query", "arguments": {"query": "SELECT * FROM users"}}}
EOF
```

#### Example with Existing Database

```
# Working with an existing database file
cat << 'EOF' | tursodb mydb.db --mcp
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "client", "version": "1.0"}}}
{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "list_tables", "arguments": {}}}
EOF
```

We'd love to have you contribute to Turso Database! Please check out the [contribution guide](https://github.com/tursodatabase/turso/blob/main/CONTRIBUTING.md) to get started.

### Is Turso Database ready for production use?

Turso powers production apps today. That includes [Turso Cloud](https://turso.tech/signup), the [Kin AI assistant](https://mykin.ai/), and [Spice.ai](https://github.com/spiceai/spiceai). However, it is still under active development and for mission-critical applications, caution is advised. Independent backups are encouraged. Turso is extensively tested by a collection of tools including a native Deterministic Simulation Testing suite and [Antithesis](https://antithesis.com), so we are generally confident in the end result. But our bar is SQLite-level reliability, and we will still recommend caution until we are confident it meets that bar.

### How is Turso Database different from Turso's libSQL?

Turso Database is a project to build the next evolution of SQLite in Rust, with a strong open contribution focus and features like native async support, vector search, and more. The libSQL project is also an attempt to evolve SQLite in a similar direction, but through a fork rather than a rewrite.

Rewriting SQLite in Rust started as an unassuming experiment, and due to its incredible success, replaces libSQL as our intended direction. At this point, libSQL is production ready, Turso Database is not - although it is evolving rapidly. More details [here](https://turso.tech/blog/we-will-rewrite-sqlite-and-we-are-going-all-in).

* Pekka Enberg, Sasu Tarkoma, Jon Crowcroft Ashwin Rao (2024). Serverless Runtime / Database Co-Design With Asynchronous I/O. In *EdgeSys ‘24*. [[PDF]](https://penberg.org/papers/penberg-edgesys24.pdf)
* Pekka Enberg, Sasu Tarkoma, and Ashwin Rao (2023). Towards Database and Serverless Runtime Co-Design. In *CoNEXT-SW ’23*. [[PDF](https://penberg.org/papers/penberg-conext-sw-23.pdf)] [[Slides](https://penberg.org/papers/penberg-conext-sw-23-slides.pdf)]
* Alperen Keles, Ethan Chou, Harrison Goldstein, Leonidas Lampropoulos (2026). DIRT: Database-Integrated Random Testing. In *DBTest '26*. [[PDF]](https://arxiv.org/pdf/2604.16373)

This project is licensed under the [MIT license](https://github.com/tursodatabase/turso/blob/main/LICENSE.md).

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in Turso Database by you, shall be licensed as MIT, without any additional
terms or conditions.

Thanks to all the partners of Turso!

[![](https://github.com/tursodatabase/turso/raw/main/assets/antithesis.jpg)](https://antithesis.com/)

[![](https://github.com/tursodatabase/turso/raw/main/assets/blacksmith.svg)](https://blacksmith.sh)

[![](https://github.com/tursodatabase/turso/raw/main/assets/turso-nyrkio.png)](https://nyrkio.com/)

Thanks to all the contributors to Turso Database!

[![](https://camo.githubusercontent.com/d199d63b18a5a9120d300568d993c534e2cbefb6e7bbfc4b45e0121d080f4f6e/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d747572736f64617461626173652f747572736f)](https://github.com/tursodatabase/turso/graphs/contributors)