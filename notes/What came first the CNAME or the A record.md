---
title: "What came first: the CNAME or the A record?"
url: https://blog.cloudflare.com/cname-a-record-order-dns-standards/
clipped: 2026-06-17 01:56:18
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [What came first: the CNAME or the A record?](https://blog.cloudflare.com/cname-a-record-order-dns-standards/)

## Digest Summary
- On 2025‑12‑02 Cloudflare introduced a memory‑saving change that altered how CNAME records were merged into cached DNS answers, moving CNAMEs from the start of the answer section to the end.  
- The change was deployed to testing on 2025‑12‑10 and globally rolled out on 2026‑01‑07. By 2026‑01‑08 the reordered responses caused widespread resolution failures, prompting a rollback at 18:27 UTC and full restoration by 19:55 UTC.  
- Some DNS clients (e.g., glibc’s getaddrinfo and Cisco switch DNSC) parse answers sequentially and expect CNAME records before any A/AAAA records; when CNAMEs appear later, they discard the preceding A records, resulting in empty answers or reboot loops.  
- Most resolvers (e.g., systemd‑resolved) search the entire answer set, so they remain unaffected.  
- RFC 1034’s wording (“possibly preface”) is ambiguous; it does not mandate CNAME ordering, unlike later RFCs (e.g., 4035) which use normative “MUST” language for other record types.  
- Cloudflare reverted the change and is drafting an Internet‑Draft to clarify that CNAMEs should be placed before other answer records in DNS responses.

## Discussion Summary
The discussion focuses on the interpretation of RFC 1034 regarding CNAME ordering, asserting that the wording clearly requires CNAME records to precede other data and criticizing implementations that ignore this. Participants cite Cloudflare’s past apex‑CNAME feature, glibc’s resolver behavior, and various vendor bugs as evidence of widespread breakage caused by ambiguous specifications and insufficient testing. The consensus calls for stricter adherence to the original RFC, more comprehensive test suites, and cautious evolution of DNS standards to avoid further incompatibilities.

---

## Full Article

On January 8, 2026, a routine update to 1.1.1.1 aimed at reducing memory usage accidentally triggered a wave of DNS resolution failures for users across the Internet. The root cause wasn't an attack or an outage, but a subtle shift in the order of records within our DNS responses.

While most modern software treats the order of records in DNS responses as irrelevant, we discovered that some implementations expect CNAME records to appear before everything else. When that order changed, resolution started failing. This post explores the code change that caused the shift, why it broke specific DNS clients, and the 40-year-old protocol ambiguity that makes the "correct" order of a DNS response difficult to define.

*All timestamps referenced are in Coordinated Universal Time (UTC).*

| **Time** | **Description** |
| --- | --- |
| 2025-12-02 | The record reordering is introduced to the 1.1.1.1 codebase |
| 2025-12-10 | The change is released to our testing environment |
| 2026-01-07 23:48 | A global release containing the change starts |
| 2026-01-08 17:40 | The release reaches 90% of servers |
| 2026-01-08 18:19 | Incident is declared |
| 2026-01-08 18:27 | The release is reverted |
| 2026-01-08 19:55 | Revert is completed. Impact ends |

While making some improvements to lower the memory usage of our cache implementation, we introduced a subtle change to CNAME record ordering. The change was introduced on December 2, 2025, released to our testing environment on December 10, and began deployment on January 7, 2026.

### How DNS CNAME chains work

When you query for a domain like `www.example.com`, you might get a [CNAME (Canonical Name)](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/) record that indicates one name is an alias for another name. Itâs the job of public resolvers, such as [1.1.1.1](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/), to follow this chain of aliases until it reaches a final response:

`www.example.com â cdn.example.com â server.cdn-provider.com â 198.51.100.1`

As 1.1.1.1 traverses this chain, it caches every intermediate record. Each record in the chain has its own [TTL (Time-To-Live)](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/), indicating how long we can cache it. Not all the TTLs in a CNAME chain need to be the same:

`www.example.com â cdn.example.com (TTL: 3600 seconds) # Still cached
cdn.example.com â 198.51.100.1Â  Â  (TTL: 300 seconds)Â  # Expired`

When one or more records in a CNAME chain expire, itâs considered partially expired. Fortunately, since parts of the chain are still in our cache, we donât have to resolve the entire CNAME chain again â only the part that has expired. In our example above, we would take the still valid `www.example.com â cdn.example.com` chain, and only resolve the expired `cdn.example.com` [A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/). Once thatâs done, we combine the existing CNAME chain and the newly resolved records into a single response.

The code that merges these two chains is where the change occurred. Previously, the code would create a new list, insert the existing CNAME chain, and then append the new records:

```
impl PartialChain {
    /// Merges records to the cache entry to make the cached records complete.
    pub fn fill_cache(&self, entry: &mut CacheEntry) {
        let mut answer_rrs = Vec::with_capacity(entry.answer.len() + self.records.len());
        answer_rrs.extend_from_slice(&self.records); // CNAMEs first
        answer_rrs.extend_from_slice(&entry.answer); // Then A/AAAA records
        entry.answer = answer_rrs;
    }
}
```

However, to save some memory allocations and copies, the code was changed to instead append the CNAMEs to the existing answer list:

```
impl PartialChain {
    /// Merges records to the cache entry to make the cached records complete.
    pub fn fill_cache(&self, entry: &mut CacheEntry) {
        entry.answer.extend(self.records); // CNAMEs last
    }
}
```

As a result, the responses that 1.1.1.1 returned now sometimes had the CNAME records appearing at the bottom, after the final resolved answer.

When DNS clients receive a response with a CNAME chain in the answer section, they also need to follow this chain to find out that `www.example.com` points to `198.51.100.1`. Some DNS client implementations handle this by keeping track of the expected name for the records as theyâre iterated sequentially. When a CNAME is encountered, the expected name is updated:

```
;; QUESTION SECTION:
;; www.example.com.        IN    A

;; ANSWER SECTION:
www.example.com.    3600   IN    CNAME  cdn.example.com.
cdn.example.com.    300    IN    A      198.51.100.1
```

1. Find records for `www.example.com`
2. Encounter `www.example.com. CNAME cdn.example.com`
3. Find records for `cdn.example.com`
4. Encounter `cdn.example.com. A 198.51.100.1`

When the CNAME suddenly appears at the bottom, this no longer works:

```
;; QUESTION SECTION:
;; www.example.com.	       IN    A

;; ANSWER SECTION:
cdn.example.com.    300    IN    A      198.51.100.1
www.example.com.    3600   IN    CNAME  cdn.example.com.
```

1. Find records for `www.example.com`
2. Ignore `cdn.example.com. A 198.51.100.1` as it doesnât match the expected name
3. Encounter `www.example.com. CNAME cdn.example.com`
4. Find records for `cdn.example.com`
5. No more records are present, so the response is considered empty

One such implementation that broke is the [`getaddrinfo`](https://man7.org/linux/man-pages/man3/getaddrinfo.3.html) function in glibc, which is commonly used on Linux for DNS resolution. When looking at its `getanswer_r` implementation, we can indeed see it expects to find the CNAME records before any answers:

```
for (; ancount > 0; --ancount)
  {
    // ... parsing DNS records ...
    
    if (rr.rtype == T_CNAME)
      {
        /* Record the CNAME target as the new expected name. */
        int n = __ns_name_unpack (c.begin, c.end, rr.rdata,
                                  name_buffer, sizeof (name_buffer));
        expected_name = name_buffer;  // Update what we're looking for
      }
    else if (rr.rtype == qtype
             && __ns_samebinaryname (rr.rname, expected_name)  // Must match!
             && rr.rdlength == rrtype_to_rdata_length (type:qtype))
      {
        /* Address record matches - store it */
        ptrlist_add (list:addresses, item:(char *) alloc_buffer_next (abuf, uint32_t));
        alloc_buffer_copy_bytes (buf:abuf, src:rr.rdata, size:rr.rdlength);
      }
  }
```

Another notable affected implementation was the DNSC process in three models of Cisco ethernet switches. In the case where switches had been configured to use 1.1.1.1 these switches experienced spontaneous reboot loops when they received a response containing the reordered CNAMEs. [Cisco has published a service document describing the issue](https://www.cisco.com/c/en/us/support/docs/smb/switches/Catalyst-switches/kmgmt3846-cbs-reboot-with-fatal-error-from-dnsc-process.html).

### Not all implementations break

Most DNS clients donât have this issue. For example, [systemd-resolved](https://www.freedesktop.org/software/systemd/man/latest/systemd-resolved.service.html) first parses the records into an ordered set:

```
typedef struct DnsAnswerItem {
        DnsResourceRecord *rr; // The actual record
        DnsAnswerFlags flags;  // Which section it came from
        // ... other metadata
} DnsAnswerItem;


typedef struct DnsAnswer {
        unsigned n_ref;
        OrderedSet *items;
} DnsAnswer;
```

When following a CNAME chain it can then search the entire answer set, even if the CNAME records donât appear at the top.

[RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034), published in 1987, defines much of the behavior of the DNS protocol, and should give us an answer on whether the order of CNAME records matters. [Section 4.3.1](https://datatracker.ietf.org/doc/html/rfc1034#section-4.3.1) contains the following text:

> If recursive service is requested and available, the recursive response to a query will be one of the following:
>
> - The answer to the query, possibly preface by one or more CNAME RRs that specify aliases encountered on the way to an answer.

While "possibly preface" can be interpreted as a requirement for CNAME records to appear before everything else, it does not use normative key words, such as [MUST and SHOULD](https://datatracker.ietf.org/doc/html/rfc2119) that modern RFCs use to express requirements. This isnât a flaw in RFC 1034, but simply a result of its age. [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119), which standardized these key words, was published in 1997, 10 years *after* RFC 1034.

In our case, we did originally implement the specification so that CNAMEs appear first. However, we did not have any tests asserting the behavior remains consistent due to the ambiguous language in the RFC.

### The subtle distinction: RRsets vs RRs in message sections

To understand why this ambiguity exists, we need to understand a subtle but important distinction in DNS terminology.

RFC 1034 [section 3.6](https://datatracker.ietf.org/doc/html/rfc1034#section-3.6) defines Resource Record Sets (RRsets) as collections of records with the same name, type, and class. For RRsets, the specification is clear about ordering:

> The order of RRs in a set is not significant, and need not be preserved by name servers, resolvers, or other parts of the DNS.

However, RFC 1034 doesnât clearly specify how message sections relate to RRsets. While modern DNS specifications have shown that message sections can indeed contain multiple RRsets (consider [DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/) responses with signatures), RFC 1034 doesnât describe message sections in those terms. Instead, it treats message sections as containing individual Resource Records (RRs).

The problem is that the RFC primarily discusses ordering in the context of RRsets but doesn't specify the ordering of different RRsets relative to each other within a message section. This is where the ambiguity lives.

RFC 1034 [section 6.2.1](https://datatracker.ietf.org/doc/html/rfc1034#section-6.2.1) includes an example that demonstrates this ambiguity further. It mentions that the order of Resource Records (RRs) is not significant either:

> The difference in ordering of the RRs in the answer section is not significant.

However, this example only shows two A records for the same name within the same RRset. It doesn't address whether this applies to different record types like CNAMEs and A records.

It turns out that this issue extends beyond putting CNAME records before other record types. Even when CNAMEs appear before other records, sequential parsing can still break if the CNAME chain itself is out of order. Consider the following response:

```
;; QUESTION SECTION:
;; www.example.com.              IN    A

;; ANSWER SECTION:
cdn.example.com.           3600  IN    CNAME  server.cdn-provider.com.
www.example.com.           3600  IN    CNAME  cdn.example.com.
server.cdn-provider.com.   300   IN    A      198.51.100.1
```

Each CNAME belongs to a different RRset, as they have different owners, so the statement about RRset order being insignificant doesnât apply here.

However, RFC 1034 doesn't specify that CNAME chains must appear in any particular order. There's no requirement that `www.example.com. CNAME cdn.example.com.` must appear before `cdn.example.com. CNAME server.cdn-provider.com.`. With sequential parsing, the same issue occurs:

1. Find records for `www.example.com`
2. Ignore `cdn.example.com. CNAME server.cdn-provider.com`. as it doesnât match the expected name
3. Encounter `www.example.com. CNAME cdn.example.com`
4. Find records for `cdn.example.com`
5. Ignore `server.cdn-provider.com. A 198.51.100.1` as it doesnât match the expected name

What should resolvers do?
-------------------------

RFC 1034 section 5 describes resolver behavior. [Section 5.2.2](https://datatracker.ietf.org/doc/html/rfc1034#section-5.2.2) specifically addresses how resolvers should handle aliases (CNAMEs):

> In most cases a resolver simply restarts the query at the new name when it encounters a CNAME.

This suggests that resolvers should restart the query upon finding a CNAME, regardless of where it appears in the response. However, it's important to distinguish between different types of resolvers:

* Recursive resolvers, like 1.1.1.1, are full DNS resolvers that perform recursive resolution by querying authoritative nameservers
* Stub resolvers, like glibcâs getaddrinfo, are simplified local interfaces that forward queries to recursive resolvers and process the responses

The RFC sections on resolver behavior were primarily written with full resolvers in mind, not the simplified stub resolvers that most applications actually use. Some stub resolvers evidently donât implement certain parts of the spec, such as the CNAME-restart logic described in the RFC.

The DNSSEC specifications provide contrast
------------------------------------------

Later DNS specifications demonstrate a different approach to defining record ordering. [RFC 4035](https://datatracker.ietf.org/doc/html/rfc4035), which defines protocol modifications for [DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/), uses more explicit language:

> When placing a signed RRset in the Answer section, the name server MUST also place its RRSIG RRs in the Answer section. The RRSIG RRs have a higher priority for inclusion than any other RRsets that may have to be included.

The specification uses "MUST" and explicitly defines "higher priority" for [RRSIG](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/) records. However, "higher priority for inclusion" refers to whether RRSIGs should be included in the response, not where they should appear. This provides unambiguous guidance to implementers about record inclusion in DNSSEC contexts, while not mandating any particular behavior around record ordering.

For unsigned zones, however, the ambiguity from RFC 1034 remains. The word "preface" has guided implementation behavior for nearly four decades, but it has never been formally specified as a requirement.

Do CNAME records come first?
----------------------------

While in our interpretation the RFCs do not require CNAMEs to appear in any particular order, itâs clear that at least some widely-deployed DNS clients rely on it. As some systems using these clients might be updated infrequently, or never updated at all, we believe itâs best to require CNAME records to appear in-order before any other records.

Based on what we have learned during this incident, we have reverted the CNAME re-ordering and do not intend to change the order in the future.

To prevent any future incidents or confusion, we have written a proposal in the form of an [Internet-Draft](https://www.ietf.org/participate/ids/) to be discussed at the IETF. If consensus is reached on the clarified behavior, this would become an RFC that explicitly defines how to correctly handle CNAMEs in DNS responses, helping us and the wider DNS community navigate the protocol. The proposal can be found at [https://datatracker.ietf.org/doc/draft-jabley-dnsop-ordered-answer-section](https://datatracker.ietf.org/doc/draft-jabley-dnsop-ordered-answer-section/). If you have suggestions or feedback we would love to hear your opinions, most usefully via the [DNSOP working group](https://datatracker.ietf.org/wg/dnsop/about/) at the IETF.