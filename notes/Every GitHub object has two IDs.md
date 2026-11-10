---
title: "Every GitHub object has two IDs"
url: https://www.greptile.com/blog/github-ids
clipped: 2026-06-17 01:58:29
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-17
summary_status: done
concepts:
  - github api
  - messagepack
  - database identifiers
  - reverse engineering
  - base64 encoding
  - graphql vs rest
related:
  - "[[API Design]]"
  - "[[Serialization Formats]]"
  - "[[Software Reverse Engineering]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** An engineer at Greptile reverse-engineered GitHub's global node ID formats, revealing how legacy base64 strings and newer MessagePack arrays encode underlying database IDs.
>
> **Key points:**
> - GitHub uses two identifier systems: older legacy global node IDs and newer MessagePack-based global node IDs, alongside traditional REST database IDs.
> - The legacy format decodes from base64 into a simple colon-separated string: `[Object Type Number]:[Object Type Name][Database ID]`.
> - The newer format (e.g. `PRRC_kwDOL4aMSs6Tkzl8`) decodes into a MessagePack array containing a version marker, a repository DB ID, and the object's DB ID.
> - Because the MessagePack payload is 96 bits, a simple bitmask (`decoded & 0xffffffff`) or MessagePack unpacking can extract the database ID from the node ID.
> - Although GitHub's official guidelines advise developers to treat node IDs as opaque, their structured nature makes decoding and reverse-engineering straightforward.
>
> **Concept links:** [[GitHub API]], [[MessagePack]], [[database identifiers]], [[reverse engineering]], [[base64 encoding]], [[GraphQL vs REST]]
>
> **Suggested connections:**
> - [[API Design]] — Examines the architectural decisions behind identifier opacity, security, and global uniqueness.
> - [[Serialization Formats]] — Compares binary serialization protocols like MessagePack, Protocol Buffers, and JSON.
> - [[Software Reverse Engineering]] — Discusses the process of analyzing a system's structure to extract hidden logic or data.
<!-- ai-summary:end -->


# [Every GitHub object has two IDs](https://www.greptile.com/blog/github-ids)

## Digest Summary
GitHub objects have two identifier schemes. The older format encodes a string of the form “:” and is base‑64‑encoded (e.g., `MDEwOlJlcG9zaXRvcnkyMzI1Mjk4` → `010:Repository2325298`). Newer objects use a global node ID prefixed by an object type (e.g., `PRRC_kwDOL4aMSs6Tkzl8`). The suffix is a base‑64‑encoded MessagePack array: `[version, repository‑DB‑ID, object‑DB‑ID]`. Decoding yields the repository ID and the object’s database ID; the object ID is always the last array element. Because the MessagePack payload is 96 bits, the lower 32 bits correspond to the database ID, allowing extraction via a simple bitmask (`decoded & 0xffffffff`). Legacy IDs persist for older repositories and certain object types (e.g., Users), while newer repositories receive the MessagePack‑based IDs. The first array element appears to be a version marker. Converting a node ID to its database ID can be done with:

```python
import base64, msgpack
def node_id_to_db_id(node_id):
    _, enc = node_id.split('_')
    return msgpack.unpackb(base64.b64decode(enc))[-1]
```

## Discussion Summary
The discussion centers on GitHub’s migration guide advising IDs be treated as opaque, yet participants note observable structure in the IDs, describing a type prefix, colon, and numeric component. Commenters express frustration that such patterns undermine the notion of true opacity and argue that robust APIs would need encryption to prevent reliance on hidden formats. Technical explanations counter claims about conditional logic, attributing the encoding to GraphQL’s base64 handling rather than time‑based checks, and note that the ID format changed only after the migration.

---

## Full Article

I was recently building a feature for Greptile (an AI-powered code review tool), when I hit a weird snag with GitHub's API.

The feature should have been simple: I wanted to add clickable links to GitHub PR comments, so users could jump directly from our reviews to relevant GitHub discussions. We already stored the comment IDs, so I just needed to construct the URLs.

The problem was, when I tested it, the links didn't work.

Searching through [GitHub's documentation](https://docs.github.com/en/graphql/guides/using-global-node-ids) for answers revealed that their team maintains two separate ID systems. We'd been using GitHub's GraphQL API, which returns [node IDs](https://docs.github.com/en/graphql/reference/scalars#id) like `PRRC_kwDOL4aMSs6Tkzl8`. GitHub designed these node IDs to uniquely identify any object across its entire system. But web URLs required database IDs, integer values visible in URLs and often associated with REST responses, like `2475899260`.

I was looking at either backfilling millions of records or migrating our entire database, and neither sounded fun. So I did what any annoyed engineer would do: I stared at these IDs for way too long, looking for a way out of the migration.

And I found it.

I looked for a relationship between these two ID formats. I pulled up a few of our stored node IDs and opened the corresponding PR comments from the same pull request in my editor:

| Node ID | Database ID |
| --- | --- |
| PRRC\_kwDOL4aMSs6Tkzl8 | 2475899260 |
| PRRC\_kwDOL4aMSs6Tkzya | 2475900058 |
| PRRC\_kwDOL4aMSs6Tkz3e | 2475900382 |

The database IDs incremented sequentially, and the node IDs were almost identical too, differing only in their last few characters. GitHub's documentation mentioned that node IDs are base64 encoded. I tried decoding just the part after `PRRC_`:

```
def base64_2_int(s):
    base64_part = s.split("_")[1]
    return int.from_bytes(base64.b64decode(base64_part))
```

The decoded values were very long (96 bit) integers:

| Node ID | Decoded Integer | Database ID |
| --- | --- | --- |
| PRRC\_kwDOL4aMSs6Tkzl8 | 45495270127925374062727215484 | 2475899260 |
| PRRC\_kwDOL4aMSs6Tkzya | 45495270127925374062727216282 | 2475900058 |
| PRRC\_kwDOL4aMSs6Tkz3e | 45495270127925374062727216606 | 2475900382 |

The decoded integers were incremented by 798, exactly matching the database ID increment. The database ID had to be embedded in there somewhere.

Since both values were changing by the same amount, and the decoded value was 96 bits, I figured the database ID was likely embedded in the lower 32 bits of the node ID. I wrote a quick test:

```
def node_id_to_database_id(s):
    decoded = int.from_bytes(base64.b64decode(s.split("_")[1]))
    # Mask to keep only the lower 32 bits
    return decoded & ((1 << 32) - 1)

node_id_to_database_id("PRRC_kwDOL4aMSs6Tkzl8")
# Returns: 2475899260
```

It worked! The database ID was just the last 32 bits of the decoded node ID. I could skip the entire migration, and extract what I needed with a simple bitmask operation.

After the relief sunk in, I couldn't help but ask, "If the database ID only used the last 32 bits out of the 96 total bits, what were the first 64 bits being used for?"

Since the node ID is a global identifier across all of GitHub, I assumed that the extra 64 bits had to encode either the object type or an id to another resource that "owned" the current node. I wanted to see if I could decode them the same way I'd decoded the database ID.

To understand what was in those 64 bits, I started [querying different GitHub objects](https://docs.github.com/en/graphql/overview/explorer). My test repository returned the familiar `PRRC_` format for everything. I tried the first famous repository that came to mind, `torvalds/linux`, to see if the pattern held.

The response was a completely different base64 encoded string:

```
MDEwOlJlcG9zaXRvcnkyMzI1Mjk4
MDQ6VHJlZTIzMjUyOTg6NzIwMWJmYjkyOGIyOWU4MGIwMDVkYTE1OTc4MzQ1ZjIzYmEwZmY5Yg==
MDQ6QmxvYjIzMjUyOTg6ZjM3MWExM2I0ZDE5MmQyZTM3ZDcwMTdiNjNlMzNkZmE3YzY3Mzc4Zg==
```

When I decoded these they showed the following:

```
base64.b64decode("MDEwOlJlcG9zaXRvcnkyMzI1Mjk4")
# Returns: b'010:Repository2325298'
```

The Linux repository was using a completely different format. I realized the repository was created in 2011. By picking an old repository, I'd accidentally stumbled onto GitHub's legacy ID format which was quite simple:

```
[Object Type Number]:[Object Type Name][Database ID]
```

That repository ID (`010:Repository2325298`) had a clear structure: `010` is some type enum, followed by a colon, the word `Repository`, and then the database ID `2325298`. Since repositories are just containers, I wanted to see if git objects like trees would reveal more complexity:

```
base64.b64decode("MDQ6VHJlZTIzMjUyOTg6NzIwMWJmYjkyOGI...")
# Returns: b'04:Tree2325298:7201bfb928b29e80b005da15978345f23ba0ff9b'
```

That's the enum again, the word `Tree`, the repository ID, and the tree SHA.

It was apparent that GitHub had two systems for ID'ing their internal objects. Somewhere in GitHub's codebase, there's an if-statement checking when a repository was created to decide which ID format to return.

I started mapping out which objects used which format. The pattern wasn't as simple as "old repos use old IDs, new repos use new IDs":

| Format | Example | Usage |
| --- | --- | --- |
| Legacy | MDEwOlJlcG9zaXRvcnkyMzI1Mjk4 | Old repositories like torvalds/linux |
| New | PRRC\_kwDOL4aMSs6Tkzl8 | Newer repositories and most objects |

Old repositories kept their legacy IDs, while newer ones were issued IDs following the new format. But the split isn't clean; GitHub still uses the legacy format for some object types, like Users, even when newly created. New objects in old repositories sometimes get new IDs, sometimes don't. It depends on their creation date.

Surely the new format had some benefit that warranted this messy migration. It shouldn't be too hard to create a more efficient IDing system than base64 encoding the string representation of an enum and the object name. This information could easily be packed into those 64 extra bits that I still had to understand.

GitHub's [migration guide](https://docs.github.com/en/graphql/guides/migrating-graphql-global-node-ids) tells developers to treat the new IDs as opaque strings and treat them as references. However it was clear that there was some underlying structure to these IDs as we just saw with the bitmasking. My best guess was that it used some binary serialization format, so I could just test a bunch to see what worked.

This is when I came across [MessagePack](https://msgpack.org/), a compact binary serialization format. It seemed promising as it was frequently used in Ruby projects, and GitHub's backend is built on Ruby. I tried decoding it:

```
import msgpack
import base64

def decode_new_node_id(node_id):
    prefix, encoded = node_id.split('_')
    packed = base64.b64decode(encoded)
    return msgpack.unpackb(packed)

decode_new_node_id("PRRC_kwDOL4aMSs6Tkzl8")
# Returns: [0, 47954445, 2475899260]
```

It worked. The new format uses MessagePack to encode the relevant IDs into an array.

The structure made sense once I saw it:

* **First element (0):** Still unclear. Probably a version identifier, but if you know what this is for, please email me at [soohoon@greptile.com](mailto:soohoon@greptile.com).
* **Second element (47954445):** The repository's database ID. This provides the context needed to make the ID global. Pull requests, issues, and comments are all usually scoped to a repository.
* **Third element (2475899260):** The object's database ID.

Different object types sometimes have different array lengths. Repositories only need `[0, repository_database_id]`. Commits include the git SHA: `[0, repository_database_id, commit_sha]`. The first element is always 0, and repository-scoped objects include both the repository ID and the specific object identifier. Since the database ID of the comment is the last element in the array, when bitmasking for the lower 32 bits we are able extract just that.

What started as a URL generation problem turned into "reverse-engineering" and exploring of GitHub's ID system.

Putting it all together, for modern GitHub node IDs you can use:

```
import base64
import msgpack

def node_id_to_database_id(node_id):
    prefix, encoded = node_id.split('_')
    packed = base64.b64decode(encoded)
    array = msgpack.unpackb(packed)
    return array[-1]
```

to extract the database ID for pull request comments. Should I have made sure that we were storing the right ID in the first place? Probably, but then I wouldn't have had much fun uncovering all of this. And my deepest condolences to the GitHub engineer who has to deal with supporting these two different node ID formats.