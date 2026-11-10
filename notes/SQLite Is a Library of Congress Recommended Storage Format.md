---
title: "SQLite Is a Library of Congress Recommended Storage Format"
url: https://sqlite.org/locrsf.html
clipped: 2026-06-17 01:06:43
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - data archiving
  - database technology
  - sqlite
related:
  - "[[Show HN ChunkHound, a local-first tool for understanding large codebases]]"
  - "[[πFS]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** The US Library of Congress recommends SQLite as a preferred storage format for long-term dataset preservation due to its disclosure, adoption, and portability.
>
> **Key points:**
> - Identifies SQLite as an LOC recommended dataset format chosen for durability and ease of long-term preservation.
> - Outlines key criteria: disclosure, transparency, adoption, and minimal external software dependencies.
> - Discusses database portability and the relative security risks of portable formats versus heavyweight servers.
>
> **Concept links:** [[Data Archiving]], [[Database Technology]], [[SQLite]], [[Information Preservation]], [[Technical Standards]]
>
> **Suggested connections:**
> - [[Show HN ChunkHound, a local-first tool for understanding large codebases]] — links local data structures and portable database models.
> - [[πFS]] — contrasts practical archival storage standards with theoretical/playful filesystem concepts.
<!-- ai-summary:end -->

# [SQLite Is a Library of Congress Recommended Storage Format](https://sqlite.org/locrsf.html)

## Digest Summary
SQLite is identified by the U.S. Library of Congress (LOC) as a recommended storage format for datasets (as of 2018‑05‑29). The LOC also lists XML, JSON, and CSV as recommended formats. Recommended formats are chosen to maximize long‑term survival and accessibility, based on several criteria:

- **Disclosure**: Complete, publicly available specifications and validation tools.  
- **Adoption**: Widespread use by creators, disseminators, and users, including as master, delivery, and interchange formats.  
- **Transparency**: Ability to inspect the digital representation with basic tools (e.g., text editors).  
- **Self‑documentation**: Inclusion of essential descriptive, technical, and administrative metadata.  
- **External Dependencies**: Minimal reliance on specific hardware, operating systems, or software.  
- **Impact of Patents**: Absence of patent barriers that could hinder archival preservation.  
- **Technical Protection Mechanisms**: No encryption or similar controls that impede trusted repositories.  

These criteria guide the LOC’s endorsement of formats like SQLite for reliable, fast, and small‑scale data storage.

## Discussion Summary
The discussion acknowledges an eight‑year‑old news item, expressing gratitude for its resurfacing and reaffirming a strong preference for SQLite despite its age. Concerns are noted about SQLite’s ease of deployment leading some organizations to prohibit its use, citing risks of handling sensitive data in portable file formats and a preference for more visible, heavyweight database servers. Nevertheless, SQLite is highlighted as a viable, widely adopted, open‑specification format suitable for long‑term public‑sector data preservation due to its portability and low patent risk.

---

## Full Article

[![SQLite](https://sqlite.org/images/sqlite370_banner.svg)](https://sqlite.org/index.html)

Small. Fast. Reliable.  
Choose any three.

LoC Recommended Storage Format

1. Overview
===========

SQLite is a
[Recommended Storage Format](https://www.loc.gov/preservation/resources/rfs/)
for datasets according to the
[US Library of Congress](https://www.loc.gov/).
Further information:

As of this writing (2018-05-29) the only other recommended storage formats
for datasets are XML, JSON, and CSV.

1.1. What Is A Recommended Storage Format?
------------------------------------------

Recommended storage formats are formats which, in the opinion of the
preservationists at the Library of Congress, maximizes the chance of
survival and continued accessibility of digital content.
When selecting recommended storage formats, the following criteria are
considered (quoting from the LOC website):

1. **Disclosure.**
   Degree to which complete specifications and tools for validating
   technical integrity exist and are accessible to those creating and
   sustaining digital content.
   A spectrum of disclosure levels can be observed for digital formats.
   What is most significant is not approval by a recognized standards body,
   but the existence of complete documentation.
2. **Adoption.**
   Degree to which the format is already used by the primary creators,
   disseminators, or users of information resources.
   This includes use as a master format, for delivery to end users,
   and as a means of interchange between systems.
3. **Transparency.**
   Degree to which the digital representation is open to direct analysis
   with basic tools, such as human readability using a text-only editor.
4. **Self-documentation.**
   Self-documenting digital objects contain basic descriptive,
   technical, and other administrative metadata.
5. **External Dependencies.**
   Degree to which a particular format depends on particular hardware,
   operating system, or software for rendering or use and the predicted
   complexity of dealing with those dependencies in future technical
   environments.
6. **Impact of Patents.**
   Degree to which the ability of archival institutions to sustain content
   in a format will be inhibited by patents.
7. **Technical Protection Mechanisms.**
   Implementation of mechanisms such as encryption that prevent the
   preservation of content by a trusted repository.