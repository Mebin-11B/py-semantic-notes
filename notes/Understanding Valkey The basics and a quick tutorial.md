---
title: "Understanding Valkey: The basics and a quick tutorial"
source: "https://www.instaclustr.com/education/valkey/understanding-valkey-the-basics-and-a-quick-tutorial/"
author:
published: 2025-03-22
created: 2026-05-31
description: "Valkey is an open-source, in-memory data structure store that functions as a database, cache, message broker, and streaming engine."
tags:
  - "clippings"
processed: true
processed_at: 2026-05-31
summary_status: done
concepts:
  - valkey database
  - redis fork
  - in-memory databases
  - open source licensing
  - database caching
related:
  - "[[Valkey Database]]"
  - "[[Redis Fork]]"
  - "[[In-Memory Databases]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** This article provides an overview of Valkey, an open-source, in-memory database fork of Redis, highlighting its architecture, benefits, differences from Redis, and setup process.
>
> **Key points:**
> - Valkey was created as a fully open-source fork of Redis 7.2.4 after Redis Inc. adopted a proprietary, source-available license.
> - Key improvements over Redis include native multi-threading for higher write throughput and asynchronous I/O for lower latencies.
> - The store supports diverse data types and serves as a cache, session store, message broker, or real-time streaming engine.
> - Best practices recommend restricting access via local bindings, setting memory thresholds, configuring RDB/AOF persistence, and using connection pooling.
> - Managed hosting and migration services are supported by cloud platforms like Instaclustr to ease transition from Redis.
>
> **Concept links:** [[Valkey Database]], [[Redis Fork]], [[In-Memory Databases]], [[Open Source Licensing]], [[Database Caching]]
>
> **Suggested connections:**
> - [[Valkey Database]] — key features and implementation details of the Valkey project.
> - [[Redis Fork]] — licensing differences and history of the Valkey fork.
> - [[In-Memory Databases]] — caching, message queue, and session store architectures using in-memory databases.
<!-- ai-summary:end -->

## What is Valkey?

Valkey is an [open source database](https://www.instaclustr.com/education/managed-database/top-10-open-source-databases-detailed-feature-comparison/). It is an in-memory data store that functions as a database, cache, message broker, and streaming engine. It supports various data types, including strings, hashes, lists, sets, sorted sets, bitmaps, hyperloglogs, geospatial indexes, and streams. Valkey offers features such as replication, Lua scripting, transactions, and multiple persistence options.

Valkey originated as a fork of Redis version 7.2.4, initiated by former Redis contributors and maintainers. This fork was prompted by Redis Inc.’s transition to proprietary licensing, leading the community to continue development under the open-source BSD 3-clause license. The project is supported by industry participants, including AWS, Google Cloud, Oracle, and Ericsson, and follows an open governance model under the Linux Foundation.

Valkey can operate as a standalone server or within a cluster, providing scalability and high availability. It is compatible with various operating systems, including Linux, macOS, OpenBSD, NetBSD, and FreeBSD. It is written in ANSI C and works on most POSIX systems without external dependencies.

You can get Valkey from the official GitHub repo [here](https://github.com/valkey-io/valkey).

## Benefits of Valkey

Valkey offers several benefits that improve application performance and development flexibility:

- **High performance and low latency:** Stores all data in memory, enabling microsecond response times and support for millions of operations per second.
- **Flexible data types:** Supports a range of data types like sorted sets, hashes, bitmaps, hyperloglogs, and geospatial indexes, giving developers options to match application needs.
- **Developer-friendly and compatible:** Offers support for multiple programming languages (e.g., Java, Python, JavaScript) with access to over a hundred open-source clients, simplifying integration.
- **Reliable replication and persistence:** Uses a primary-replica architecture with asynchronous replication for improved read performance and point-in-time backups for persistent data storage.
- **Open source and community-supported:** Freely available under the BSD 3-clause license, benefiting from a large community of contributors for continuous improvements and security.
- **High availability and scalability:** Supports multi-node clusters to maintain availability and allows for horizontal scaling, ensuring reliability for high-demand applications.

## Valkey vs. Redis

Valkey and Redis are both in-memory data type stores, but they differ in several key areas:

### Licensing

Redis transitioned to a source-available license in 2024, which imposes certain restrictions on usage, particularly for commercial purposes. Valkey maintains the BSD 3-clause license, ensuring it remains fully open-source and free for all use cases.

### Performance

Valkey offers performance enhancements over Redis:

- **Multi-threading:** Unlike Redis’s predominantly single-threaded architecture, Valkey incorporates multi-threading to better utilize modern multi-core processors, leading to significant improvements in throughput, especially for write-heavy workloads.
- **Asynchronous I/O:** Valkey’s improved asynchronous I/O threading reduces latency and improves overall responsiveness, making it well-suited for real-time applications.

### Scalability

Valkey provides improved clustering capabilities:

- **Automatic failover:** In the event of a node failure, Valkey’s automatic failover mechanism ensures that another node takes over without friction, minimizing downtime and maintaining data availability.
- **Improved slot migration:** Valkey improves the process of slot migration, making it more reliable and reducing the risk of data loss or inconsistencies during cluster rebalancing.

## Tips from the expert

Suresh Vasanthakumar

Site Reliability Engineer

Suresh is a seasoned database engineer with over a decade of experience in designing, deploying and optimizing high-performance distributed systems. Specializing in in-memory data stores, Suresh has deep expertise in managing Redis and Valkey clusters for enterprise-scale applications.

In my experience, here are tips that can help you better leverage Valkey in high-performance, real-world applications:

- **Optimize data type selection for workloads:** Use Valkey’s diverse data types strategically based on the application’s needs. For example, use hyperloglogs for approximate counts to save memory in analytics applications, or sorted sets for leaderboard-style functionalities in gaming apps.
- **Leverage Lua scripting to reduce network overhead:** Write custom Lua scripts to execute complex logic server-side within Valkey. This reduces network traffic by bundling multiple commands in a script, and it minimizes latency for functions requiring multi-step processing on the same data set.
- **Use data partitioning with tags for cluster efficiency:** For even data distribution in clustered environments, use hash tags (like {tag} in key names) for keys related to similar data to ensure that they’re stored on the same node. This reduces cross-node traffic and improves performance for operations on related data.
- **Use replication to isolate read and write workloads:** Designate replica nodes as read-only to balance read and write loads effectively. This way, primary nodes focus on writes, reducing latency, while replica nodes handle heavy read loads.
- **Enable lazy eviction policies for dynamic caching:** For caching scenarios where data is only accessed infrequently, configure the `lazyfree-lazy-eviction` option. This prevents eviction from blocking active operations and is especially useful for time-sensitive, read-heavy workloads.

## Common use cases for Valkey

Valkey’s versatility and performance make it suitable for a range of use cases in application development and data management.

### Caching

Valkey’s in-memory caching capabilities significantly improve application performance by reducing data access latency and alleviating the load on backend databases. Acting as a high-speed, scalable cache, Valkey can store frequently requested data such as database query results, user sessions, static web content, and application metadata.

By handling these requests directly in memory, Valkey enables response times in the microsecond range, which is particularly useful for applications with heavy read demands. Examples include caching query results for databases, storing persistent sessions for high-traffic websites, caching rendered web pages, and storing frequently accessed files.

### Real-time messaging and queues

Valkey’s support for the Pub/Sub model, along with data types such as lists, sorted sets, and hashes, makes it suitable for building real-time messaging and queuing systems. Applications that require live updates, like chat applications, social media feeds, live comment streams, and inter-server communication, benefit from Valkey’s low-latency message handling.

The List data type, which includes atomic operations and blocking capabilities, allows Valkey to act as a reliable message broker or lightweight queue system. For example, in a chat application, Valkey can manage message queues and ensure message delivery with minimal delay.

### Session storage

As an in-memory data store with persistence options, Valkey is a popular choice for managing user sessions in internet-scale applications. Applications with high volumes of user traffic, such as eCommerce platforms, social media networks, and large-scale web applications, need to store session data quickly and reliably to maintain a seamless user experience.

Valkey provides the low-latency response and high availability required for storing session details like user profiles, login credentials, personalized settings, and session state. It supports data replication and persistence, ensuring session data remains available across server outages and allows fast recovery.

### Rich media streaming

In live media streaming, Valkey supports applications by storing metadata and user-related information in-memory for quick access. Valkey can manage data such as user profiles, authentication tokens, viewing history, and manifest files for live-streamed content. This data enables content delivery networks (CDNs) to retrieve information in real time to deliver media content to users.

For example, Valkey can quickly provide authentication and user profile information for millions of users accessing a streaming platform simultaneously. Additionally, it can support functions such as recommendations based on viewing history and personalized playlists, creating a responsive experience for end-users.

## Quick tutorial: Getting started with Valkey

This guide will walk you through the steps to install and configure Valkey on different platforms. These instructions are adapted from the [Valkey documentation](https://valkey.io/topics/installation/).

### Step 1: Download Valkey

Start by downloading the latest release from [valkey.io/download](https://valkey.io/download) or directly from Valkey’s GitHub releases.

![Valkey tutorial terminal screenshot](https://www.instaclustr.com/wp-content/uploads/IR1024-4-1.jpg)

### Step 2: Install Valkey

There are various methods to install Valkey depending on your environment:

From source: Download and unpack the source code tarball. For example:

| 1 | tar -xzvf valkey-8.0.1.tar.gz |
| --- | --- |

| 1 | cd valkey-8.0.1 |
| --- | --- |

Follow the `README.md` file included in the package for detailed instructions on building and installing.

- **Containers:** If you use Docker, you can pull a Valkey image directly from Docker Hub.
- **Package manager – Fedora:** Install using the package name `valkey`.

macOS: Use Homebrew with:

| 1  2  3  4 | brew install valkey  brew services start valkey # Run Valkey as a service  brew services info valkey # Check status  brew services stop valkey # Stop service |
| --- | --- |

**Windows:** Valkey is not officially supported on Windows. However, you can run it in a Windows environment using the Windows Subsystem for Linux (WSL).

### Step 3: Run Valkey

To start Valkey in the foreground, use the following command:

| 1 | valkey-server |
| --- | --- |

To stop it, press Ctrl-C. Alternatively, you can run it as a background service by configuring init scripts or using `screen` on Linux.

### Step 4: Test the installation with the CLI

Once Valkey is running, test the connection using `valkey-cli`:

| 1 | valkey-cli ping |
| --- | --- |

This should return `PONG`, confirming that Valkey is active and accepting commands. You can also launch `valkey-cli` in interactive mode by running it without arguments:

| 1 | valkey-cli |
| --- | --- |

In this mode, you can send commands to your Valkey instance interactively.

### Step 5: Secure Valkey

If you’re deploying Valkey in a networked environment, apply these security measures:

- **Firewall:** Ensure that Valkey’s default ports (6379, and others in cluster mode) are protected by a firewall.
- **Bind address:** Set Valkey to listen only on trusted interfaces by configuring the bind directive in its configuration file.
- **Password authentication:** Use the `requirepass` option in the configuration file to add a password layer.

Example for adding authentication:

| 1  2 | \# In Valkey configuration file  requirepass YOURPASSWORD |
| --- | --- |

### Step 6: Configure persistence

To save data to disk, Valkey allows you to manually save the database with the `SAVE` command, or you can use the `SHUTDOWN` command to save before exit:

| 1 | valkey-cli save # Save data to disk |
| --- | --- |

| 1 | valkey-cli shutdown # Save and shutdown the server |
| --- | --- |

### Step 7: Verify persistence

Check that Valkey saves data as expected by running the following in valkey-cli:

| 1 | valkey-cli save |
| --- | --- |

Then, verify that the dump file is saved in the configured directory (e.g., `/var/valkey/6379/dump.rdb`).

Note: If you didn’t set a directory, output will be stored in the same directory:

After following these steps, Valkey should be properly installed, running, and configured securely. You can now integrate it with your application by using the appropriate client library for your programming language.

## Best practices for using Valkey

Here are some best practices to consider for making the best use of Valkey.

### Secure configuration

To configure Valkey securely, start by binding the server to `127.0.0.1` and `::1` to restrict access to localhost, reducing the risk of unauthorized connections. Avoid exposing Valkey to all interfaces unless absolutely necessary, and make sure to implement strict firewall rules to block untrusted network access.

Enabling password authentication with the `requirepass` directive adds an extra layer of security; for applications requiring user-specific access, define individual users with tailored permissions using the `user` directive.

For data security during transmission, enable TLS/SSL, especially when Valkey is accessed over the internet or in untrusted networks. Configure `tls-cert-file`, `tls-key-file`, and `tls-ca-cert-file` directives to provide trusted certificates, ensuring encrypted connections and protecting sensitive data from interception.

### Memory management

Valkey’s performance relies heavily on efficient memory management. Set memory limits using the `maxmemory` directive to control resource usage and prevent system-wide memory exhaustion, which could impact other applications running on the same server.

Choosing the right eviction policy, such as `allkeys-lru` (Least Recently Used for all keys) or `volatile-lru` (for expiring keys only), helps Valkey manage its memory efficiently based on application needs. Monitoring memory usage regularly allows developers to make proactive adjustments as data volumes change, helping to maintain system responsiveness.

### Persistence configuration

Configuring Valkey for data persistence ensures that data remains available even in the event of a system restart or failure. For snapshot-based backups, use the `save` directive to configure automatic periodic snapshots, storing these files in a secure location specified by the `dir` directive.

The snapshots provide a point-in-time backup, capturing the state of the data at regular intervals. For more continuous data durability, enable the append-only file (AOF) persistence mode by setting `appendonly yes`, which logs every write operation to disk.

Choosing the right `appendfsync` policy (such as `always`, `everysec`, or `no`) allows developers to control the balance between performance and data safety. Regularly review persistence configurations to ensure they align with the application’s data retention and recovery requirements.

### Command usage

Efficient command usage can prevent server slowdowns and maintain Valkey’s responsiveness. Commands like `KEYS` or `SCAN` can be particularly resource-intensive, especially on large datasets, as they require Valkey to scan through all keys or iterate over data types, potentially blocking other operations.

Instead, use `SCAN` with careful limits on large datasets, or consider restructuring data access patterns if frequent full scans are necessary. To improve performance on high-volume applications, use pipelining to batch multiple commands together in a single request, reducing the number of round-trips and lowering latency.

### Client configuration

When using Valkey in a clustered environment, it is essential to ensure that clients are cluster-aware. This enables clients to manage redirections, handle server topology changes, and reduce load on individual nodes. Many Valkey-compatible client libraries come with cluster-aware configurations to automatically handle slot redirection and node discovery.

Additionally, implement connection pooling in the client configuration to manage multiple Valkey connections and prevent excessive resource usage. Set appropriate timeouts for idle connections to avoid resource leaks and improve application stability, especially in applications with variable traffic patterns.

## Empowering organizations to embrace Valkey with the Instaclustr Managed Platform

Valkey, the next-generation in-memrory database solution, is the leading successor to Redis. Due to licensing changes, Redis is no longer considered open source, but organizations may choose to migrate from Redis to Valkey. For organizations that require migrations services, on-going operations or support for Valkey, this technology is available on the Instaclustr Managed Platform.

According to the Linux Foundation, “To continue improving on this technology and allow for unfettered distribution of the project, the community created Valkey, an open source high performance key-value store. Valkey supports the Linux, macOS, OpenBSD, NetBSD, and FreeBSD platforms. In addition, the community will continue working on its existing roadmap including new features such as a more reliable slot migration, dramatic scalability and stability improvements to the clustering system, multi-threaded performance improvements, triggers, new commands, vector search support, and more.”

At Instaclustr, we’re believers in that Valkey is the natural choice for organizations running Redis based on the following Valkey benefits:

- Retains 2 out of 3 of the original corporate maintainers of Redis
- Keeps the open source license
- Continues with single-threaded C to ensure maximum compatibility.

For more information see:

- [Valkey® now available on the NetApp® Instaclustr Managed Platform](https://www.instaclustr.com/blog/valkey-now-available/)
- [Embracing the Future: Instaclustr’s Transition from Redis™ to Valkey](https://www.instaclustr.com/blog/redis-to-valkey/)