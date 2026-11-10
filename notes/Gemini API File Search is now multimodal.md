---
title: "Gemini API File Search is now multimodal"
url: https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/
clipped: 2026-06-17 01:04:47
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Gemini API File Search is now multimodal](https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/)

## Digest Summary
Gemini API File Search now supports multimodal queries, enabling retrieval from text documents and images. Users can attach custom key‑value metadata (e.g., department, status) to unstructured files, and apply metadata filters at query time to narrow results, reducing irrelevant hits and improving RAG speed and accuracy. The service records page numbers for each indexed segment, allowing responses to be directly linked to source locations for precise verification. File upload and search are handled by the File Search tool, abstracting infrastructure concerns. Early adopters report strong performance on mixed‑modality scientific corpora and image‑rich collections, noting higher semantic retrieval quality, reduced hallucinations, and significant context‑window savings when indexing diagrams and other visual assets. The update emphasizes reliable, citation‑backed outputs across text and visual content.

## Discussion Summary
Feedback highlights frustration with AI Studio’s search capabilities, noting that it only indexes conversation titles and lacks content search. Users also report that recent scrolling changes interfere with the reliability of standard browser find functions like Ctrl+F, further complicating navigation. The overall tone is critical, emphasizing a desire for more robust in‑conversation searching and stable scrolling behavior to improve usability.

---

## Full Article

Filter the noise with custom metadata
-------------------------------------

Dumping files into a database is easy. Finding the right one at scale is the real challenge. Custom metadata allows you to attach key-value labels to your unstructured data — things like `department: Legal` or `status: Final`.

By applying metadata filters at query time, your application can scope requests to the data slice required. This significantly reduces noise from irrelevant documents, increasing both the speed and accuracy of your RAG workflows.

Show your work with page citations
----------------------------------

When your application pulls an answer from a massive PDF, users need to verify exactly where that answer came from.

File Search now ties the model’s response directly to the original source. It captures the page number for every piece of indexed information. This level of granularity allows you to point users directly to the right spot, which helps build trust and makes your tool immediately useful for rigorous fact-checking.

Get started with File Search
----------------------------

We want to make it as easy as possible to store and retrieve the data that makes your ideas work. The File Search tool handles the heavy infrastructure so you can focus on building the product.

Uploading files and searching across them is simple: