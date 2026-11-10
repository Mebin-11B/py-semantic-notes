---
title: "Learning a few things about running SQLite"
url: https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/
clipped: 2026-08-31 12:22:56
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Learning a few things about running SQLite](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/)

## Digest Summary
The author runs a small Django site on SQLite (≈10 k rows) and shares practical lessons learned. Enabling WAL mode is standard, but a full‑text search query over 4 000 rows took 5 s until an `ANALYZE` command was run, which generated table statistics and reduced the query time to ~0.05 s. Deleting large numbers of rows can lock the database for several seconds; concurrent writers then hit the 5‑second timeout and crash. The author mitigates this by batching cleanup operations. For backups, two approaches are used: (1) a manual `VACUUM INTO` to a temporary file, gzip compression, and storage with restic on S3, noting occasional OOM‑related lock issues; (2) Litestream for continuous, incremental replication to S3 with a 400‑hour retention setting. Splitting tables into separate SQLite files is mentioned as a useful organization trick. Overall, the site remains stable with SQLite, provided statistics are kept up‑to‑date, write contention is limited, and backups are handled reliably.

---

## Full Article

[Skip to main content](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/#main)

     

Hello! I’ve been working on a Django site recently, and I decided to use SQLite
as the database.
When I was getting started with using SQLite as database for a website I read a [bunch](https://alldjango.com/articles/definitive-guide-to-using-django-sqlite-in-production)
of blog posts about how it is totally fine to use SQLite in production for a
small site and I think it is totally fine, but what I did not fully appreciate
is that SQLite is still a database, databases are complicated, and I do not know
a lot about operating databases.

So here are a couple of small things I’ve been learning about running SQLite. This
is the 4th website I’ve used SQLite for, and I think this one is harder because
with the power of the Django ORM I’ve been making the database do more work than
I was previously without Django.

I started by turning on WAL mode like all the blog posts said to do and hoping for the best.

### 
     `` [ANALYZE is apparently important](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/#analyze-is-apparently-important)

Today I was running a query (using [SQLite’s FTS5](https://www.sqlite.org/fts5.html) for
full-text search) on a table with 4000 rows and it took 5 seconds. That seemed
wrong to me: computers are fast!

It turned out that what I needed to do was to run  `` [ANALYZE](https://sqlite.org/lang_analyze.html)!
Immediately the problem query went from taking 5 seconds to like 0.05 seconds
(or some other number small enough that I didn’t care to investigate further).
I still don’t know exactly what went wrong in the query plan,
but my best guess is that it was some sort of [accidentally quadratic](https://accidentallyquadratic.tumblr.com/) thing.

 `ANALYZE`  generates “statistics” (I guess about the number of rows in each table? and presumably other things?)
so that the query planner can make better choices.

Maybe one day I’ll learn to read a query plan.

### 
    [cleaning up the database is tricky](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/#cleaning-up-the-database-is-tricky)

Occasionally I’ve run into situations where I accidentally put a bunch of rows
in my database that I don’t want to be there (for example completed tasks from
[django-tasks-db](https://github.com/RealOrangeOne/django-tasks-db)), and I want to clean them up.

What’s happened to me a few times in this case is:

- I run some kind of command to clean up the rows

- The command takes more than 5 seconds, since there are a lot of rows (though I still have some questions about why these DELETE statements are so slow honestly, maybe there’s a bunch of Python code running inside a transaction, I’m not sure)

- One of the other workers tries to write the database while this is happening, and times out after 5 seconds (I have a timeout of 5 seconds set)

- The worker crashes because it couldn’t write to the database and the VM shuts down

My approach so far has been to just do these cleanup operations in small batches
so that I don’t need to do database queries that take more than 5 seconds to
run. This whole experience has given me more of an appreciation for why someone
might want to use a “real” database like Postgres which can have more than one
writer at the same time though.

Maybe in the future I’ll just take the site down for scheduled maintenance
instead when I need to do this kind of thing, but I haven’t figured out a
workflow for that yet.

### 
    [no notes on performance of ORM queries yet](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/#no-notes-on-performance-of-orm-queries-yet)

So far I’ve been using Django’s ORM to make any query I want without paying any
attention at all to query performance and it’s mostly been going okay other
than the  `ANALYZE`  thing. The database is pretty small (maybe 10000 rows?) and
I expect it to stay pretty small forever, so I’m hoping that that plan will
keep working.

### 
    [backing up sqlite](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/#backing-up-sqlite)

I’ve done SQLite backups a couple of ways. I don’t think I’ve actually tested
restoring from my backups but I do usually try to monitor them with a dead man’s
switch.

way 1: restic
 ` `sqlite3 /data/calendar.db "VACUUM INTO '/tmp/calendar.sqlite'"
gzip /tmp/calendar.sqlite

# Upload backup to S3
# Sometimes the backup gets OOM killed and so it stays locked, do an unlock
restic -r s3://s3.amazonaws.com/some_bucket/ unlock
# Do the backup & prune old backups
restic -r s3://s3.amazonaws.com/some_bucket/ backup /tmp/calendar.sqlite.gz
restic -r s3://s3.amazonaws.com/some_bucket/ snapshots
restic -r s3://s3.amazonaws.com/some_bucket/ forget -l 1 -H 6 -d 2 -w 2 -m 2 -y 2
restic -r s3://s3.amazonaws.com/some_bucket/ prune
` ` 

way 2: [litestream](https://litestream.io/)

I started trying out Litestream recently because I felt like doing incremental backups might
be more efficient: my restic backups were sometimes getting OOM killed, and I
was a bit tired of it. Basically I just write a config file and run:
 ` `litestream replicate -config litestream.yml
` ` 

I set  `retention: 400h`  in my config file in an attempt to
retain some amount of history of the database but I have no idea if it works.

I’ve been backing up to AWS, which is always a pain because it’s annoying to
navigate the AWS console to generate credentials. Maybe one day I’ll move away
to some other S3-compatible alternative.

### 
    [you can use multiple databases](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/#you-can-use-multiple-databases)

My current project only has one database, but one trick I used with
[Mess with DNS](https://messwithdns.net/) was to split the tables into three separate
database files because I didn’t actually need my tables to be in the same db. I think it was helpful.

Mess with DNS has been running on SQLite for 4 years now (since 2022) and it’s
been great, I think the move from Postgres was a great choice for that project.

### 
    [that’s all!](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/#that-s-all)

It’s always kind of fun to see how long it takes me to learn sort of basic
things about the technologies I’m using. I think I used SQLite for a web project
for the first time in 2022 and I only learned that  `ANALYZE`  existed today!
I imagine in a year or two I’ll be learning about some other very basic feature.

### 
    [some references](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/#some-references)

Some blog posts I’ve looked at, other than the official docs:

- [The definitive guide to using Django with SQLite in production](https://alldjango.com/articles/definitive-guide-to-using-django-sqlite-in-production)

- [a gist on sqlite performance tuning](https://gist.github.com/phiresky/978d8e204f77feaa0ab5cca08d2d5b27)
