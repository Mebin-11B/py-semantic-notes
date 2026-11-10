---
title: "Show HN: s@: decentralized social networking over static sites"
url: http://satproto.org/
clipped: 2026-06-17 01:33:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - decentralized social networks
  - static site hosting
  - cryptographic identity
  - protocol design
  - serverless architecture
related:
  - "[[Decentralized Social Networks]]"
  - "[[Static Site Hosting]]"
  - "[[Cryptographic Identity]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The s@ protocol implements a serverless, decentralized social network by storing encrypted JSON feeds directly on user-controlled static websites.
>
> **Key points:**
> - Identity is established via the user's domain name, authenticating connections through standard HTTPS/TLS.
> - Data, posts, and lists are formatted as JSON, with updates published by pushing changes to a static host (e.g., GitHub Pages).
> - Cryptographic privacy is maintained through asymmetric envelopes (libsodium) and key rotation upon unfollowing.
>
> **Concept links:** [[Decentralized Social Networks]], [[Static Site Hosting]], [[Cryptographic Identity]], [[Protocol Design]], [[Serverless Architecture]]
>
> **Suggested connections:**
> - [[Decentralized Social Networks]] — protocols like Nostr, ActivityPub, and s@ that bypass centralized servers.
> - [[Static Site Hosting]] — serving application state and content via CDNs without backend databases.
> - [[Cryptographic Identity]] — using public key cryptography to establish user trust and ownership.
<!-- ai-summary:end -->

# [Show HN: s@: decentralized social networking over static sites](http://satproto.org/)

## Digest Summary
s@ (sAT Protocol) is a decentralized social‑networking protocol that runs entirely on static websites. Each user’s domain name serves as their identity, authenticated via HTTPS/TLS. User data is stored in encrypted JSON files within a `/satellite/` directory; a discovery document (`satproto.json` or a custom `satproto_root.json`) publishes the protocol version and the user’s X25519 public key.

Encryption uses a 256‑bit symmetric content key (XChaCha20‑Poly1305) sealed per follower with libsodium `crypto_box_seal`. The user’s own sealed box (`keys/_self.json`) contains the content key and publishing secrets, enabling device recovery. Unfollow triggers key rotation, re‑encryption, and new envelopes.

Posts are individually encrypted (`posts/{id}.json.enc`), listed in a plaintext `posts/index.json` (newest‑first). IDs follow `ISO8601‑compact‑UTC-4hex`. Follow lists are plain JSON (`follows/index.json`). Clients aggregate feeds by reading follow lists, fetching each followed site’s key envelope, decrypting posts, and merging them by `created_at`. Replies are top‑level only, grouped under the original post. Publishing creates a new encrypted post, pushes it via the host’s API (e.g., GitHub), and updates the index. The protocol is hosting‑agnostic, requiring no servers or relays.

## Discussion Summary
The discussion centers on decentralized social networking, emphasizing the appeal of static‑site approaches for self‑sovereignty while questioning their scalability and the need for complex cryptographic signing. Comparisons are drawn to earlier models such as FOAF, Pingback, and Webmention, as well as to Nostr and its relay‑based discovery, highlighting trade‑offs between infrastructure independence and polling overhead. Suggestions include exploring hybrid solutions, leveraging existing tools like Git, and simplifying interaction mechanisms, reflecting a cautious optimism about finding a practical middle ground.

---

## Full Article

`s@`: Social Networking over Static Sites
=========================================

```
      simple  *
      static  *  social networking
self-reliant  *
```

Quick Start
-----------

1. Fork [this repo](https://github.com/remysucre/satellite) (see below if you need a different name from `satellite`)
2. Enable [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-from-a-branch) on your fork (deploy from the `main` branch).
3. Visit the GitHub Pages URL (e.g. `https://username.github.io/satellite/`)

While this sample implementation uses GitHub, the protocol is agnostic to the hosting service.

**Using a custom repo name**:
by default, the client looks for data at `https://{domain}/satellite/`.
If you already have a `satellite/` path for something else, add a `.well-known/satproto.json`
file to the root of your main site (e.g. the `username.github.io` repo)
pointing to the actual repo:

```
{ "sat_root": "my-custom-repo" }
```

**Note on GitHub Pages and `.well-known`**:
GitHub Pages with Jekyll ignores dotfiles/directories by default.
To serve `.well-known/`, either:

* Add a `.nojekyll` file to your domain root repo (if you don’t use Jekyll), or
* Add `include: [".well-known"]` to `_config.yml` (if you do use Jekyll)

Protocol
--------

`s@` is a decentralized social networking protocol based on static sites.
Each user owns a static website storing all their data in encrypted JSON stores.
A client running in the browser aggregates feeds and publishes posts.
It does not rely on any servers or relays.

In plain terms, `s@` is designed for you and your friends, and no one else.
This applies to both the technical implementation and the user experience.
At the technical level, data only moves from your own website to your friend’s browser.
There are no servers (like Mastodon) or relays (like the AT Protocol) in the middle.
And unlike almost all social media platform today,
`s@` is not designed for *influencers*.
To see a friend’s post or to have a friend see your post, you must follow *each other*.

Identity
--------

A user’s identity is their domain name.
Identity is authenticated by HTTPS/TLS - fetching content from a domain proves
the domain owner published it.

Discovery
---------

A `s@`-enabled site exposes a discovery document at:

```
GET https://{domain}/satellite/profile.json
```

The discovery document simply contains the protocol version and the user’s public key:

```
{
  "satproto_version": "0.1.0",
  "public_key": "<base64-encoded X25519 public key>"
}
```

By convention, the client looks under `/satellite/` by default.
If that path is already taken, place a `.well-known/satproto.json` file at the domain
root containing `{ "sat_root": "my-custom-repo" }` — the client checks this first.

Encryption Model
----------------

All user data is stored in an encrypted JSON store.
Only the user and users in the owner’s follow list can decrypt it.

### Keys

* Each user generates an **X25519 keypair**.
  The public key is published in the discovery document.
  The private key is cached in the browser’s localStorage
  and should be exported for safekeeping.
* A random **content key** (256-bit symmetric key) encrypts
  post data with XChaCha20-Poly1305.
* The content key is encrypted per-follower using libsodium sealed boxes
  (`crypto_box_seal` with the follower’s X25519 public key)
  and stored at `keys/{follower-domain}.json`.

### Self Key (`keys/_self.json`)

The user’s content key and publishing secrets (e.g. GitHub access tokens)
are bundled into a single sealed box (`crypto_box_seal` with the user’s own public key)
and stored at `keys/_self.json`. Only the user’s private key can open it.

This allows a user to sign back in on a new device or after clearing
browser storage — they only need their domain and private key.

### Key Rotation (Unfollow)

When the user unfollows someone:

1. Generate a new content key
2. Re-encrypt all posts with the new key
3. Re-create key envelopes for all remaining followers
4. Update `keys/_self.json` with the new content key
5. The unfollowed user’s old key no longer decrypts anything

### Decryption Flow

When Bob visits Alice’s site:

1. Resolve Alice’s data path (via `.well-known/satproto.json` or the default `/satellite/`)
2. Fetch `keys/bob.example.com.json`
3. Decrypt the content key using Bob’s private key (`crypto_box_seal_open`)
4. Fetch `posts/index.json` to get the list of post IDs
5. Fetch and decrypt individual posts from `posts/{id}.json.enc`
   (XChaCha20-Poly1305 with the content key)

Data Schema
-----------

Each post is stored as an individually encrypted file. The post index
(`posts/index.json`) is a plaintext JSON file listing post IDs
newest-first, allowing clients to lazily load only recent posts.

A post object:

```
{
  "id": "20260309T141500Z-a1b2",
  "author": "alice.com",
  "created_at": "2026-03-09T14:15:00Z",
  "text": "Hello, decentralized world!",
  "reply_to": null,
  "reply_to_author": null
}
```

Post IDs are `{ISO8601-compact-UTC}-{4-hex-random}`, e.g. `20260309T141500Z-a1b2`.
The timestamp prefix gives natural sort order; the random suffix prevents collisions.

Follow List
-----------

The follow list is stored as a plain JSON file (unencrypted, since the key
envelopes already reveal follows):

```
GET https://{domain}/satellite/follows/index.json
```

```
{
  "follows": ["bob.example.com", "carol.example.com"]
}
```

Feed Aggregation
----------------

The client builds a feed by:

1. Reading the user’s follow list
2. For each followed user, resolving their repo path
3. For each followed user, decrypting their posts (using the key envelope
   the followed user published for this user)
4. Merging all posts, sorted by `created_at` descending

Replies
-------

A reply is a post with `reply_to` and `reply_to_author` set.
Replies are grouped as flat threads under the original post — nested replies
(replying to a reply) are not supported; you can only reply to top-level posts.

Threads are positioned in the timeline by the original post’s `created_at`;
replies within a thread are sorted by their own `created_at` ascending.

If the original post is inaccessible (e.g. the viewer doesn’t follow the
author), the reply is hidden entirely. A user only sees replies from people
they follow — this is the spam prevention mechanism.

Publishing
----------

The client publishes posts by:

1. Creating a new post with a unique ID
2. Encrypting the post JSON with the content key
3. Pushing the encrypted post as `posts/{id}.json.enc` to user’s static site (e.g. via the GitHub Contents API)
4. Updating `posts/index.json` to include the new post ID

Any secrets needed for publishing (e.g. GitHub token)
is encrypted in `keys/_self.json` (see [Self Key](http://satproto.org/#self-key-keys_selfjson)).

Static Site Structure
---------------------

```
{domain}/satellite/
  profile.json              # Discovery + profile + public key
  posts/
    index.json              # Post ID list (plaintext, newest first)
    {id}.json.enc           # Individually encrypted post files
  follows/
    index.json              # Follow list (unencrypted)
  keys/
    _self.json              # Sealed box: content key + credentials (owner only)
    {domain}.json           # Sealed box: content key for follower
```

FAQ
---

> Is this just RSS + encryption?

Yes.

> Is this just [AT Protocol](https://atproto.com) but no firehose?

Yes.

> Does this scale?

No! Neither does friendship.

> Wait so I can self-host this?

Yes, you’ll need to enable [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS).