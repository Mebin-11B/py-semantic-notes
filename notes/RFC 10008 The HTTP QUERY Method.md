---
title: "RFC 10008: The HTTP QUERY Method"
source: "https://www.rfc-editor.org/info/rfc10008/"
author:
  - "[[J. Reschke]]"
  - "[[J.M. Snell]]"
  - "[[M. Bishop]]"
  - "[[J. Reschke]]"
  - "[[J.M. Snell]]"
  - "[[M. Bishop]]"
published: 2022-06-01
created: 2026-06-19
description: "This specification defines the QUERY method for HTTP. A QUERY requests that the request target process the enclosed content in a safe and idempotent manner and then respond with the result of that processing. This is similar to POST requests, but QUERY requests can be automatically repeated or restarted without concern for partial state changes."
tags:
  - "clippings"
---
- J. Reschke,
- J.M. Snell,
- M. Bishop

Proposed Standard

## Abstract

This specification defines the QUERY method for HTTP. A QUERY requests that the request target process the enclosed content in a safe and idempotent manner and then respond with the result of that processing. This is similar to POST requests, but QUERY requests can be automatically repeated or restarted without concern for partial state changes.[¶](#section-abstract-1)

## Status of This Memo

This is an Internet Standards Track document.[¶](#section-boilerplate.1-1)

This document is a product of the Internet Engineering Task Force (IETF). It represents the consensus of the IETF community. It has received public review and has been approved for publication by the Internet Engineering Steering Group (IESG). Further information on Internet Standards is available in Section 2 of RFC 7841.[¶](#section-boilerplate.1-2)

Information about the current status of this document, any errata, and how to provide feedback on it may be obtained at.[¶](#section-boilerplate.1-3)

## 1.

This specification defines the HTTP QUERY request method as a means of making a safe, idempotent request ([Section 9.2](https://rfc-editor.org/rfc/rfc9110#section-9.2) of \[\]) that encloses a representation describing how the request is to be processed by the target resource.[¶](#section-1-1)

A common query pattern is:[¶](#section-1-2)

```
GET /feed?q=foo&limit=10&sort=-published HTTP/1.1
Host: example.org
```

[¶](#section-1-3)

However, when the data conveyed is too voluminous to be encoded in the request's URI, this pattern becomes problematic:[¶](#section-1-4)

As an alternative to using GET, many implementations make use of the HTTP POST method to perform queries, as illustrated in the example below. In this case, the input to the query operation is passed as the request content as opposed to using the request URI's query component.[¶](#section-1-6)

A typical use of HTTP POST for requesting a query is:[¶](#section-1-7)

```
POST /feed HTTP/1.1
Host: example.org
Content-Type: application/x-www-form-urlencoded

q=foo&limit=10&sort=-published
```

[¶](#section-1-8)

In this variation, however, it is not readily apparent -- without specific knowledge of the resource and server to which the request is being sent -- that a safe, idempotent query is being performed.[¶](#section-1-9)

The QUERY method provides a solution that spans the gap between the use of GET and POST, with the example above being expressed as:[¶](#section-1-10)

```
QUERY /feed HTTP/1.1
Host: example.org
Content-Type: application/x-www-form-urlencoded

q=foo&limit=10&sort=-published
```

[¶](#section-1-11)

As with POST, the input to the query operation is passed as the content of the request rather than as part of the request URI. Unlike POST, however, the method is explicitly safe and idempotent, allowing functions like caching and automatic retries to operate.[¶](#section-1-12)

Recognizing the design principle that any important resource ought to be identified by a URI, this specification describes how a server can assign URIs to both the query itself or to a specific query result, for later use in a GET request.[¶](#section-1-13)

Summarizing:[¶](#section-1-14)

<table><caption>:</caption><thead><tr><th rowspan="1" colspan="1"></th><th rowspan="1" colspan="1">GET</th><th rowspan="1" colspan="1">QUERY</th><th rowspan="1" colspan="1">POST</th></tr></thead><tbody><tr><td rowspan="1" colspan="1">Safe</td><td rowspan="1" colspan="1">yes</td><td rowspan="1" colspan="1">yes</td><td rowspan="1" colspan="1">potentially no</td></tr><tr><td rowspan="1" colspan="1">Idempotent</td><td rowspan="1" colspan="1">yes</td><td rowspan="1" colspan="1">yes</td><td rowspan="1" colspan="1">potentially no</td></tr><tr><td rowspan="1" colspan="1">URI for query itself</td><td rowspan="1" colspan="1">yes (by definition)</td><td rowspan="1" colspan="1">optional (Location response field)</td><td rowspan="1" colspan="1">no</td></tr><tr><td rowspan="1" colspan="1">URI for query result</td><td rowspan="1" colspan="1">optional (Content-Location response field)</td><td rowspan="1" colspan="1">optional (Content-Location response field)</td><td rowspan="1" colspan="1">optional (Content-Location response field)</td></tr><tr><td rowspan="1" colspan="1">Cacheable</td><td rowspan="1" colspan="1">yes</td><td rowspan="1" colspan="1">yes</td><td rowspan="1" colspan="1">yes, but only for future GET or HEAD requests</td></tr><tr><td rowspan="1" colspan="1">Content (body)</td><td rowspan="1" colspan="1">"no defined semantics"</td><td rowspan="1" colspan="1">expected (semantics per target resource)</td><td rowspan="1" colspan="1">expected (semantics per target resource)</td></tr></tbody></table>

### 1.1.

This document uses terminology defined in [Section 3](https://rfc-editor.org/rfc/rfc9110#section-3) of \[\].[¶](#section-1.1-1)

Furthermore, it uses the terms *URI query parameter* for parameters in the query component of a URI ([Section 4.2.2](https://rfc-editor.org/rfc/rfc9110#section-4.2.2) of \[\]) and *query content* for the request content ([Section 6.4](https://rfc-editor.org/rfc/rfc9110#section-6.4) of \[\]) of a QUERY request.[¶](#section-1.1-2)

### 1.2.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 \[\] \[\] when, and only when, they appear in all capitals, as shown here.[¶](#section-1.2-1)

## 2.

The QUERY method is used to initiate a server-side query. Unlike the GET method, which requests a representation of the resource identified by the target URI (as defined by [Section 7.1](https://rfc-editor.org/rfc/rfc9110#section-7.1) of \[\]), the QUERY method is used to ask the target resource to perform a query operation within the scope of that target resource.[¶](#section-2-1)

The content of the request and its media type define the query. The origin server determines the scope of the operation based on the target resource.[¶](#section-2-2)

Servers MUST fail the request if the Content-Type request field (\[\], [Section 8.3](https://rfc-editor.org/rfc/rfc9110#section-8.3)) is missing or is inconsistent with the request content.[¶](#section-2-3)

As for all HTTP methods, the target URI's query part takes part in identifying the resource being queried. Whether and how it directly affects the result of the query is specific to the resource and is out of scope for this specification.[¶](#section-2-4)

QUERY requests are safe with regard to the target resource (\[\], [Section 9.2.1](https://rfc-editor.org/rfc/rfc9110#section-9.2.1)); that is, the client does not request or expect any change to the state of the target resource. This does not prevent the server from creating additional HTTP resources through which additional information can be retrieved (see Sections and ).[¶](#section-2-5)

Furthermore, QUERY requests are idempotent (\[\], [Section 9.2.2](https://rfc-editor.org/rfc/rfc9110#section-9.2.2)); they can be retried or repeated when needed, for instance, after a connection failure.[¶](#section-2-6)

As per [Section 15.3](https://rfc-editor.org/rfc/rfc9110#section-15.3) of \[\], a 2xx (Successful) response code signals that the request was successfully received, understood, and accepted.[¶](#section-2-7)

In particular, a 200 (OK) response indicates that the query was successfully processed and the results of that processing are enclosed as the response content.[¶](#section-2-8)

### 2.1.

The semantics of a QUERY request depend both on the request content and the associated metadata, such as the media type (\[\], [Section 8.3.1](https://rfc-editor.org/rfc/rfc9110#section-8.3.1)). In general, any problem with requests where content and metadata are inconsistent MUST be rejected with a 4xx (Client Error) response (\[\], [Section 15.5](https://rfc-editor.org/rfc/rfc9110#section-15.5)).[¶](#section-2.1-1)

The list below describes various cases of failures and recommends specific status codes:[¶](#section-2.1-2)

- If a request lacks media type information, it is incorrect by definition and needs to fail with a 4xx status code such as 400 (Client Error).[¶](#section-2.1-3.1)
- If a media type is specified but is not supported by the resource, a 415 (Unsupported Media Type) is appropriate. This specifically includes the case where the media type is known in principle, but it lacks semantics specific to a QUERY to the target resource. In both cases, the Accept-Query response field () can be used to inform the client of the media types that are supported.[¶](#section-2.1-3.2)
- If a media type is specified but is inconsistent with the actual request content, a 400 (Bad Request) can be returned. That is, a server is not allowed to infer a media type from the request content and then override a missing or "erroneous" value (i.e., "content sniffing").[¶](#section-2.1-3.3)
- If the media type is specified and understood, and the content is indeed consistent with the type, but the query cannot be processed due to the actual contents of the query, the status 422 (Unprocessable Content) can be used. An example would be a syntactically correct SQL query that identifies a non-existent table.[¶](#section-2.1-3.4)
- If the client requests a specific response media type using the Accept field (\[\], [Section 12.5.1](https://rfc-editor.org/rfc/rfc9110#section-12.5.1)) that is not supported by the resource, a status code of 406 (Not Acceptable) is appropriate.[¶](#section-2.1-3.5)

### 2.2.

The *equivalent resource* for any given QUERY request is a resource that responds to GET requests, represents that QUERY request and its target, and takes both message content and metadata into account ([Section 6](https://rfc-editor.org/rfc/rfc9110#section-6) of \[\]). In particular, this includes representation metadata ([Section 8](https://rfc-editor.org/rfc/rfc9110#section-8) of \[\]) such as the content's media type.[¶](#section-2.2-1)

In other words, the equivalent resource is derived from the resource implementing QUERY by incorporating the request content.[¶](#section-2.2-2)

The term *equivalent resource* is used as a means to define behavior for other HTTP aspects, such as selected representations. Servers can but do not have to assign URIs to these resources (see [Section 1.1](https://rfc-editor.org/rfc/rfc3986#section-1.1) of \[\]). If they do so, these resources will become accessible for GET requests.[¶](#section-2.2-3)

### 2.3.

A successful response (2xx, [Section 15.3](https://rfc-editor.org/rfc/rfc9110#section-15.3) of \[\]) can include a Content-Location header field containing an identifier for a resource corresponding to the results of the operation; see [Section 8.7](https://rfc-editor.org/rfc/rfc9110#section-8.7) of \[\] for details. This represents a claim from the server that a client can send a GET request for the indicated URI to retrieve the results of the query operation just performed. The indicated resource might be temporary.[¶](#section-2.3-1)

See for an example.[¶](#section-2.3-2)

### 2.4.

A server can assign a URI to the equivalent resource () of a QUERY request. If the server does so, the URI of that resource can be included in the Location header field of the 2xx response (see [Section 10.2.2](https://rfc-editor.org/rfc/rfc9110#section-10.2.2) of \[\]). This represents a claim that a client can send a GET request to the indicated URI to repeat the query operation just performed without resending the query content. This resource's URI might be temporary; if a future request fails, the client can retry using the original QUERY request target and the previously submitted content.[¶](#section-2.4-1)

See for an example.[¶](#section-2.4-2)

### 2.5.

In some cases, the server may choose to respond indirectly to the QUERY request by redirecting the user agent to a different URI (see [Section 15.4](https://rfc-editor.org/rfc/rfc9110#section-15.4) of \[\]).[¶](#section-2.5-1)

A response with either status codes 301 (Moved Permanently, \[\], [Section 15.4.2](https://rfc-editor.org/rfc/rfc9110#section-15.4.2)) or 308 (Permanent Redirect, \[\], [Section 15.4.9](https://rfc-editor.org/rfc/rfc9110#section-15.4.9)) indicates that the target resource has permanently moved to a different URI referenced by the Location response field (\[\], [Section 10.2.2](https://rfc-editor.org/rfc/rfc9110#section-10.2.2)). Likewise, a response with either status codes 302 (Found, \[\], [Section 15.4.3](https://rfc-editor.org/rfc/rfc9110#section-15.4.3)) or 307 (Temporary Redirect, \[\], [Section 15.4.8](https://rfc-editor.org/rfc/rfc9110#section-15.4.8)) indicates that the target resource has temporarily moved. In all four cases, the server is suggesting that the user agent can accomplish its original QUERY request by sending a similar QUERY request to the new target URI referenced by the Location.[¶](#section-2.5-2)

Note that the exceptions for redirecting a POST as a GET request after a 301 or 302 response do not apply to QUERY requests.[¶](#section-2.5-3)

A response to QUERY with the status code 303 (See Other, [Section 15.4.4](https://rfc-editor.org/rfc/rfc9110#section-15.4.4) of \[\]) indicates that the original query can be accomplished via a normal retrieval request on the URI referenced by the Location response field (\[\], [Section 10.2.2](https://rfc-editor.org/rfc/rfc9110#section-10.2.2)). For HTTP, this means sending a GET request to the new target URI, as illustrated by the example in.[¶](#section-2.5-4)

### 2.6.

The selected representation ([Section 3.2](https://rfc-editor.org/rfc/rfc9110#section-3.2) of \[\]) of a QUERY request is the same as for a GET request to the equivalent resource () of that QUERY request.[¶](#section-2.6-1)

A conditional QUERY requests that the selected representation (i.e., the query results after any content negotiation) be returned in the response only under the circumstances described by the conditional header field(s), as defined in [Section 13](https://rfc-editor.org/rfc/rfc9110#section-13) of \[\].[¶](#section-2.6-2)

See for examples.[¶](#section-2.6-3)

### 2.7.

The response to a QUERY method is cacheable; a cache MAY use it to satisfy subsequent QUERY requests as per [Section 4](https://rfc-editor.org/rfc/rfc9111#section-4) of \[\].[¶](#section-2.7-1)

The cache key for a QUERY request ([Section 2](https://rfc-editor.org/rfc/rfc9111#section-2) of \[\]) MUST incorporate the request content ([Section 6](https://rfc-editor.org/rfc/rfc9111#section-6) of \[\]) and related metadata ([Section 8](https://rfc-editor.org/rfc/rfc9110#section-8) of \[\]).[¶](#section-2.7-2)

To improve cache efficiency, caches MAY remove semantically insignificant differences from request content and related metadata first. For instance, by:[¶](#section-2.7-3)

- removing content encoding(s) ([Section 8.4](https://rfc-editor.org/rfc/rfc9110#section-8.4) of \[\]).[¶](#section-2.7-4.1)
- normalizing based upon knowledge of format conventions, as indicated by any media subtype suffix in the request's Content-Type field (e.g., "+json"; see [Section 4.2.8](https://rfc-editor.org/rfc/rfc6838#section-4.2.8) of \[\]).[¶](#section-2.7-4.2)
- normalizing based upon knowledge of the semantics of the content itself, as indicated by the request's Content-Type field.[¶](#section-2.7-4.3)

Note that any such transformation is performed solely for the purpose of generating a cache key; it does not change the request itself.[¶](#section-2.7-5)

Clients can indicate, using the "no-transform" cache directive ([Section 5.2.1.6](https://rfc-editor.org/rfc/rfc9111#section-5.2.1.6) of \[\]) that they wish that no such transformation happens (but note that this directive is just advisory).[¶](#section-2.7-6)

Note that caching QUERY method responses is inherently more complex than caching responses to GET, as complete reading of the request's content is needed in order to determine the cache key. If a QUERY response supplies a Location response field () to indicate a URI for an equivalent resource (), clients can switch to GET for subsequent requests, thereby simplifying processing.[¶](#section-2.7-7)

### 2.8.

The semantics of Range Requests for QUERY are identical to those for GET, as defined in [Section 14](https://rfc-editor.org/rfc/rfc9110#section-14) of \[\]. Byte Range Requests (the only range unit defined at the time of writing), however, offer little value for the results of a QUERY request.[¶](#section-2.8-1)

Query formats often define their own way of limiting or paging through result sets, such as with "FETCH FIRST... ROWS ONLY" in SQL. It is expected that these built-in features will be used instead of HTTP Range Requests.[¶](#section-2.8-2)

## 3.

The "Accept-Query" response header field can be used by a resource to directly signal support for the QUERY method while identifying the specific query format media type(s) that may be used.[¶](#section-3-1)

Accept-Query contains a list of media ranges ([Section 12.5.1](https://rfc-editor.org/rfc/rfc9110#section-12.5.1) of \[\]) using "Structured Fields" syntax \[\]. Media ranges are represented by a List Structured Header Field of either Tokens or Strings, containing the media range value without parameters.[¶](#section-3-2)

Media type parameters, if any, are mapped to Structured Field Parameters with the String or Token type. The choice of Token versus String is semantically insignificant. That is, recipients MAY convert Tokens to Strings, but MUST NOT process them differently based on the received type.[¶](#section-3-3)

Media types do not exactly map to Tokens; for instance, they allow a leading digit. In cases like these, the String format needs to be used.[¶](#section-3-4)

The only supported uses of wildcards are "\*/\*", which matches any type, or "xxxx/\*", which matches any subtype of the indicated type.[¶](#section-3-5)

The order of types listed in the field value is not significant.[¶](#section-3-6)

The value of the Accept-Query field applies to every URI on the server that shares the same path; in other words, the query component is ignored. If requests to the same resource return different Accept-Query values, the most recently received fresh value (per [Section 4.2](https://rfc-editor.org/rfc/rfc9111#section-4.2) of \[\]) is used.[¶](#section-3-7)

For example:[¶](#section-3-8)

```
Accept-Query: "application/jsonpath", application/sql;charset="UTF-8"
```

[¶](#section-3-9)

Although the syntax for this field appears to be similar to other fields, such as "Accept" ([Section 12.5.1](https://rfc-editor.org/rfc/rfc9110#section-12.5.1) of \[\]), it is a Structured Field and thus MUST be processed as specified in [Section 4](https://rfc-editor.org/rfc/rfc9651#section-4) of \[\].[¶](#section-3-10)

## 4.

The QUERY method is subject to the same general security considerations as all HTTP methods as described in \[\].[¶](#section-4-1)

It can be used as an alternative to passing request information in the URI (e.g., in the query component). This is preferred in some cases, as the URI is more likely to be logged or otherwise processed by intermediaries than the request content. In other cases, where the query contains sensitive information, the potential for logging of the URI might motivate the use of QUERY over GET.[¶](#section-4-2)

If a server creates a temporary resource to represent the results of a QUERY request (e.g., for use in the Location or Content-Location field), assigns a URI to that resource, and the request contains sensitive information that cannot be logged, then that URI SHOULD be chosen such that it does not include any sensitive portions of the original request content.[¶](#section-4-3)

Caches that normalize QUERY content incorrectly or in ways that are significantly different from how the resource processes the content can return an incorrect response if normalization results in a false positive.[¶](#section-4-4)

A QUERY request from user agents implementing Cross-Origin Resource Sharing (CORS) will require a "preflight" request, as QUERY does not belong to the set of CORS-safelisted methods (see \[\]).[¶](#section-4-5)

## 5.

### 5.1.

IANA has added the QUERY method to the "Hypertext Transfer Protocol (HTTP) Method Registry" at < [http://www.iana.org/assignments/http-methods](http://www.iana.org/assignments/http-methods) > (see [Section 16.3.1](https://rfc-editor.org/rfc/rfc9110#section-16.3.1) of \[\]).[¶](#section-5.1-1)

<table><caption>:</caption><thead><tr><th rowspan="1" colspan="1">Method Name</th><th rowspan="1" colspan="1">Safe</th><th rowspan="1" colspan="1">Idempotent</th><th rowspan="1" colspan="1">Specification</th></tr></thead><tbody><tr><td rowspan="1" colspan="1">QUERY</td><td rowspan="1" colspan="1">yes</td><td rowspan="1" colspan="1">yes</td><td rowspan="1" colspan="1">of RFC 10008</td></tr></tbody></table>

### 5.2.

IANA has added the Accept-Query field to the "Hypertext Transfer Protocol (HTTP) Field Name Registry" at < [https://www.iana.org/assignments/http-fields](https://www.iana.org/assignments/http-fields) > (see [Section 16.1.1](https://rfc-editor.org/rfc/rfc9110#section-16.1.1) of \[\]).[¶](#section-5.2-1)

<table><caption>:</caption><thead><tr><th rowspan="1" colspan="1">Field Name</th><th rowspan="1" colspan="1">Status</th><th rowspan="1" colspan="1">Structured Type</th><th rowspan="1" colspan="1">Reference</th><th rowspan="1" colspan="1">Comments</th></tr></thead><tbody><tr><td rowspan="1" colspan="1">Accept-Query</td><td rowspan="1" colspan="1">permanent</td><td rowspan="1" colspan="1">List</td><td rowspan="1" colspan="1">of RFC 10008</td><td rowspan="1" colspan="1"></td></tr></tbody></table>

## 6.

### 6.1.

\[HTTP\]

Fielding, R., Ed., Nottingham, M., Ed., and J. Reschke, Ed., "HTTP Semantics", STD 97, RFC 9110, DOI 10.17487/RFC9110, June 2022, < [https://www.rfc-editor.org/info/rfc9110](https://www.rfc-editor.org/info/rfc9110) >.

\[HTTP-CACHING\]

Fielding, R., Ed., Nottingham, M., Ed., and J. Reschke, Ed., "HTTP Caching", STD 98, RFC 9111, DOI 10.17487/RFC9111, June 2022, < [https://www.rfc-editor.org/info/rfc9111](https://www.rfc-editor.org/info/rfc9111) >.

\[RFC2119\]

Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997, < [https://www.rfc-editor.org/info/rfc2119](https://www.rfc-editor.org/info/rfc2119) >.

\[RFC8174\]

Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017, < [https://www.rfc-editor.org/info/rfc8174](https://www.rfc-editor.org/info/rfc8174) >.

\[STRUCTURED-FIELDS\]

Nottingham, M. and P. Kamp, "Structured Field Values for HTTP", RFC 9651, DOI 10.17487/RFC9651, September 2024, < [https://www.rfc-editor.org/info/rfc9651](https://www.rfc-editor.org/info/rfc9651) >.

\[URI\]

Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, DOI 10.17487/RFC3986, January 2005, < [https://www.rfc-editor.org/info/rfc3986](https://www.rfc-editor.org/info/rfc3986) >.

### 6.2.

\[FETCH\]

WHATWG, "FETCH", WHATWG Living Standard, < [https://fetch.spec.whatwg.org](https://fetch.spec.whatwg.org/) >. Commit snapshot: < [https://fetch.spec.whatwg.org/commit-snapshots/3bab31a55154bda73f25b45a23df718616f2f64e/](https://fetch.spec.whatwg.org/commit-snapshots/3bab31a55154bda73f25b45a23df718616f2f64e/) >.

\[RFC3253\]

Clemm, G., Amsden, J., Ellison, T., Kaler, C., and J. Whitehead, "Versioning Extensions to WebDAV (Web Distributed Authoring and Versioning)", RFC 3253, DOI 10.17487/RFC3253, March 2002, < [https://www.rfc-editor.org/info/rfc3253](https://www.rfc-editor.org/info/rfc3253) >.

\[RFC4918\]

Dusseault, L., Ed., "HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)", RFC 4918, DOI 10.17487/RFC4918, June 2007, < [https://www.rfc-editor.org/info/rfc4918](https://www.rfc-editor.org/info/rfc4918) >.

\[RFC5323\]

Reschke, J., Ed., Reddy, S., Davis, J., and A. Babich, "Web Distributed Authoring and Versioning (WebDAV) SEARCH", RFC 5323, DOI 10.17487/RFC5323, November 2008, < [https://www.rfc-editor.org/info/rfc5323](https://www.rfc-editor.org/info/rfc5323) >.

\[RFC6838\]

Freed, N., Klensin, J., and T. Hansen, "Media Type Specifications and Registration Procedures", BCP 13, RFC 6838, DOI 10.17487/RFC6838, January 2013, < [https://www.rfc-editor.org/info/rfc6838](https://www.rfc-editor.org/info/rfc6838) >.

\[RFC8259\]

Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", STD 90, RFC 8259, DOI 10.17487/RFC8259, December 2017, < [https://www.rfc-editor.org/info/rfc8259](https://www.rfc-editor.org/info/rfc8259) >.

\[RFC9535\]

Gössner, S., Ed., Normington, G., Ed., and C. Bormann, Ed., "JSONPath: Query Expressions for JSON", RFC 9535, DOI 10.17487/RFC9535, February 2024, < [https://www.rfc-editor.org/info/rfc9535](https://www.rfc-editor.org/info/rfc9535) >.

\[URL\]

WHATWG, "URL", WHATWG Living Standard, < [https://url.spec.whatwg.org](https://url.spec.whatwg.org/) >. Commit snapshot: < [https://url.spec.whatwg.org/commit-snapshots/52526653e848c5a56598c84aa4bc8ac9025fb66b/](https://url.spec.whatwg.org/commit-snapshots/52526653e848c5a56598c84aa4bc8ac9025fb66b/) >.

\[XSLT\]

Kay, M., Ed., "XSL Transformations (XSLT) Version 3.0", W3C Recommendation, 8 June 2017, < [https://www.w3.org/TR/2017/REC-xslt-30-20170608/](https://www.w3.org/TR/2017/REC-xslt-30-20170608/) >. Latest version available at [https://www.w3.org/TR/xslt-30/](https://www.w3.org/TR/xslt-30/).

## Appendix A.

The examples below are for illustrative purposes only; if one needs to send queries that are actually this short, it is likely better to use GET.[¶](#appendix-A-1)

The media type used in most examples is "application/x-www-form-urlencoded" (as used in POST requests from browser user clients, defined in ["application/x-www-form-urlencoded"](https://url.spec.whatwg.org/#application/x-www-form-urlencoded) in \[\]). The Content-Length fields have been omitted for brevity.[¶](#appendix-A-2)

### A.1.

Below is a simple query with a direct response:[¶](#appendix-A.1-1)

```
QUERY /contacts HTTP/1.1
Host: example.org
Content-Type: application/x-www-form-urlencoded
Accept: application/json

select=surname,givenname,email&limit=10&match=%22email=*@example.*%22
```

[¶](#appendix-A.1-2)

Response:[¶](#appendix-A.1-3)

```
HTTP/1.1 200 OK
Content-Type: application/json

[
  { "surname": "Smith",
    "givenname": "John",
    "email": "smith@example.org" },
  { "surname": "Jones",
    "givenname": "Sally",
    "email": "sally.jones@example.com" },
  { "surname": "Dubois",
    "givenname": "Camille",
    "email": "camille.dubois@example.net" }
]
```

[¶](#appendix-A.1-4)

### A.2.

A simple way to discover support for QUERY is provided by the OPTIONS ([Section 9.3.7](https://rfc-editor.org/rfc/rfc9110#section-9.3.7) of \[\]) method:[¶](#appendix-A.2-1)

```
OPTIONS /contacts HTTP/1.1
Host: example.org
```

[¶](#appendix-A.2-2)

Response:[¶](#appendix-A.2-3)

```
HTTP/1.1 200 OK
Allow: GET, QUERY, OPTIONS, HEAD
```

[¶](#appendix-A.2-4)

The Allow response field ([Section 10.2.1](https://rfc-editor.org/rfc/rfc9110#section-10.2.1) of \[\]) denotes the set of supported methods on the specified resource.[¶](#appendix-A.2-5)

There are alternatives to the use of OPTIONS. For instance, a QUERY request can be tried without prior knowledge of server support. The server would then either process the request, or it could respond with a 4xx status such as 405 (Method Not Allowed, [Section 15.5.6](https://rfc-editor.org/rfc/rfc9110#section-15.5.6) of \[\]), including the Allow response field.[¶](#appendix-A.2-6)

### A.3.

The discovery of supported media types for QUERY is possible via the Accept-Query response field ():[¶](#appendix-A.3-1)

```
HEAD /contacts HTTP/1.1
Host: example.org
```

[¶](#appendix-A.3-2)

Response:[¶](#appendix-A.3-3)

```
HTTP/1.1 200 OK
Content-Type: application/xhtml
Accept-Query: application/x-www-form-urlencoded, application/sql
```

[¶](#appendix-A.3-4)

Responses to which request methods will contain Accept-Query will depend on the resource being accessed.[¶](#appendix-A.3-5)

An alternative to checking Accept-Query would be to make a QUERY request, and then -- in case of a 4xx status such as a 415 response (Unsupported Media Type, [Section 15.5.16](https://rfc-editor.org/rfc/rfc9110#section-15.5.16) of \[\]) -- to inspect the Accept response field ([Section 12.5.1](https://rfc-editor.org/rfc/rfc9110#section-12.5.1) of \[\]):[¶](#appendix-A.3-6)

```
HTTP/1.1 415 Unsupported Media Type
Content-Type: application/xhtml
Accept: application/x-www-form-urlencoded, application/sql
```

[¶](#appendix-A.3-7)

### A.4.

As described in Sections and, the Content-Location and Location response fields in success responses (2xx, [Section 15.3](https://rfc-editor.org/rfc/rfc9110#section-15.3) of \[\]) provide a way to identify alternate resources that will respond to GET requests, either for the received result of the request or for future requests to perform the same operation. Going back to the example from:[¶](#appendix-A.4-1)

```
QUERY /contacts HTTP/1.1
Host: example.org
Content-Type: application/x-www-form-urlencoded
Accept: application/json

select=surname,givenname,email&limit=10&match=%22email=*@example.*%22
```

[¶](#appendix-A.4-2)

Response:[¶](#appendix-A.4-3)

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Location: /contacts/stored-results/17
Location: /contacts/stored-queries/42
Last-Modified: Sat, 25 Aug 2012 23:34:45 GMT
Date: Sun, 17 Nov 2024, 16:10:24 GMT

[
  { "surname": "Smith",
    "givenname": "John",
    "email": "smith@example.org" },
  { "surname": "Jones",
    "givenname": "Sally",
    "email": "sally.jones@example.com" },
  { "surname": "Dubois",
    "givenname": "Camille",
    "email": "camille.dubois@example.net" }
]
```

[¶](#appendix-A.4-4)

#### A.4.1.

The Content-Location response field received above identifies a resource holding the result for the QUERY response it appeared on:[¶](#appendix-A.4.1-1)

```
GET /contacts/stored-results/17 HTTP/1.1
Host: example.org
Accept: application/json
```

[¶](#appendix-A.4.1-2)

Response:[¶](#appendix-A.4.1-3)

```
HTTP/1.1 200 OK
Last-Modified: Sat, 25 Aug 2012 23:34:45 GMT
Date: Sun, 17 Nov 2024, 16:10:25 GMT

[
  { "surname": "Smith",
    "givenname": "John",
    "email": "smith@example.org" },
  { "surname": "Jones",
    "givenname": "Sally",
    "email": "sally.jones@example.com" },
  { "surname": "Dubois",
    "givenname": "Camille",
    "email": "camille.dubois@example.net" }
]
```

[¶](#appendix-A.4.1-4)

Note that there is no guarantee that the server will implement this resource indefinitely, so, after an error response, the client would need to redo the original QUERY request in order to obtain a new alternative location.[¶](#appendix-A.4.1-5)

#### A.4.2.

The Location response field identifies a resource that will respond to GET with a current result for the same process and parameters as the original QUERY request.[¶](#appendix-A.4.2-1)

```
GET /contacts/stored-queries/42 HTTP/1.1
Host: example.org
Accept: application/json
```

[¶](#appendix-A.4.2-2)

In this example, one entry was removed at 2024-11-17T16:12:01Z (as indicated in the Last-Modified field), so the response only contains two entries:[¶](#appendix-A.4.2-3)

```
HTTP/1.1 200 OK
Content-Type: application/json
Last-Modified: Sun, 17 November 2024, 16:12:01 GMT
ETag: "42-1"
Date: Sun, 17 Nov 2024, 16:13:17 GMT

[
  { "surname": "Smith",
    "givenname": "John",
    "email": "smith@example.org" },
  { "surname": "Dubois",
    "givenname": "Camille",
    "email": "camille.dubois@example.net" }
]
```

[¶](#appendix-A.4.2-4)

Assuming that the server still exposes the resource and that there was no change in the query result, a subsequent conditional GET request with the following:[¶](#appendix-A.4.2-5)

```
If-None-Match: "42-1"
```

[¶](#appendix-A.4.2-6)

would result in a 304 (Not Modified) response ([Section 15.4.5](https://rfc-editor.org/rfc/rfc9110#section-15.4.5) of \[\]).[¶](#appendix-A.4.2-7)

#### A.4.3.

Servers can send "indirect" responses () using the status code 303 (See Other, [Section 15.4.4](https://rfc-editor.org/rfc/rfc9110#section-15.4.4) of \[\]).[¶](#appendix-A.4.3-1)

Given the request at the beginning of, a server might respond with:[¶](#appendix-A.4.3-2)

```
HTTP/1.1 303 See Other
Content-Type: text/plain
Date: Sun, 17 Nov 2024, 16:13:17 GMT
Location: /contacts/stored-queries/42

See stored query at "/contacts/stored-queries/42".
```

[¶](#appendix-A.4.3-3)

This is similar to including Location on a direct response, except that no result for the query is returned. This allows the server to only generate or reuse an alternative resource. This resource could then be used as shown in.[¶](#appendix-A.4.3-4)

### A.5.

Consider a resource implementing QUERY that supports "application/sql" and "application/xslt+xml" \[\] as request media types, and which can generate responses as "text/csv". The data set being queried contains RFC document information, and the query returns information grouped by decade:[¶](#appendix-A.5-1)

```
QUERY /rfc-index.xml HTTP/1.1
Host: example.org
Date: Sun, 7 Sep 2025, 00:00:00 GMT
Content-Type: application/xslt+xml
Accept: text/csv

...Query content using XSLT...
```

[¶](#appendix-A.5-2)

Response:[¶](#appendix-A.5-3)

```
HTTP/1.1 200 OK
Date: Sun, 7 Sep 2025, 00:00:00 GMT
Location: /stored-queries/4815162342
Content-Type: text/csv
Accept-Query: "application/sql", "application/xslt+xml"
Last-Modified: Sun, 31 Aug 2025, 08:44:00 GMT
Vary: Accept-Query, Content-Encoding, Content-Type

decade, total, with errata, % with errata, average page count
1960, 26, 5, 19.2, 5.3
1970, 666, 18, 2.7, 6.1
1980, 376, 44, 11.7, 23.4
1990, 1593, 269, 16.9, 25.5
2000, 2888, 1048, 36.3, 27.3
2010, 2954, 895, 30.3, 26.1
2020, 1133, 230, 20.3, 26.2
```

[¶](#appendix-A.5-4)

Here, the server has assigned the path "/stored-queries/4815162342" to the equivalent resource () for subsequent use with GET.[¶](#appendix-A.5-5)

Later on, the client repeats the query, but specifies that results should only be returned when changed:[¶](#appendix-A.5-6)

```
QUERY /rfc-index.xml HTTP/1.1
Host: example.org
Date: Mon, 8, Sep 2025, 11:00:00 GMT
Content-Type: application/sql
Accept: text/csv
If-Modified-Since: Sun, 31 Aug 2025, 08:44:00 GMT
Vary: Accept-Query, Content-Type

...Same query, but using SQL...
```

[¶](#appendix-A.5-7)

The data being queried did not change, therefore the server responds with:[¶](#appendix-A.5-8)

```
HTTP/1.1 304 Not Modified
Date: Mon, 8 Sep 2025, 11:00:00 GMT
Content-Type: text/csv
Location: /stored-queries/4815162342
Accept-Query: "application/sql", "application/xslt+xml"
Last-Modified: Sun, 31 Aug 2025, 08:44:00 GMT
Vary: Accept-Query, Content-Type
```

[¶](#appendix-A.5-9)

As the server identified a URI for the equivalent resource, that resource can be accessed with GET. In particular, this avoids resending the query request's content:[¶](#appendix-A.5-10)

```
GET /stored-queries/4815162342 HTTP/1.1
Host: example.org
Date: Sun, 21, Sep 2025, 12:08:00 GMT
Accept: text/csv
If-Modified-Since: Sun, 31 Aug 2025, 00:00:00 GMT
```

[¶](#appendix-A.5-11)

Here, the state of the data set indeed changed, so new content is returned:[¶](#appendix-A.5-12)

```
HTTP/1.1 200 OK
Date: Sun, 21, Sep 2025, 12:08:00 GMT
Content-Type: text/csv
Last-Modified: Thu, 18 Sep 2025, 19:56:00 GMT
Vary: Accept-Query, Content-Encoding, Content-Type

decade, total, with errata, % with errata, average page count
1960, 26, 5, 19.2, 5.3
1970, 666, 18, 2.7, 6.1
1980, 376, 44, 11.7, 23.4
1990, 1593, 269, 16.9, 25.5
2000, 2888, 1048, 36.3, 27.3
2010, 2954, 895, 30.3, 26.1
2020, 1133, 230, 20.3, 26.2
```

[¶](#appendix-A.5-13)

(Note the change in the row for this decade.) [¶](#appendix-A.5-14)

The diagrams below illustrate the use of conditional requests and how they can differ when a URI is assigned to the equivalent resource (and when the client is taking advantage of it). The fictitious field name "Validator" is used for demonstration purposes.[¶](#appendix-A.5-15)

<svg xmlns="http://www.w3.org/2000/svg" version="1.1" height="496px" width="416px" viewBox="0 0 416 496" text-anchor="middle" font-family="monospace" font-size="13px" stroke-linecap="round"><path d="M 8,48 L 8,480" fill="none" stroke="black"></path><path d="M 288,304 L 288,336" fill="none" stroke="black"></path><path d="M 344,48 L 344,296" fill="none" stroke="black"></path><path d="M 344,344 L 344,480" fill="none" stroke="black"></path><path d="M 408,304 L 408,336" fill="none" stroke="black"></path><path d="M 8,80 L 336,80" fill="none" stroke="black"></path><path d="M 16,144 L 344,144" fill="none" stroke="black"></path><path d="M 8,208 L 336,208" fill="none" stroke="black"></path><path d="M 16,272 L 344,272" fill="none" stroke="black"></path><path d="M 288,304 L 408,304" fill="none" stroke="black"></path><path d="M 288,336 L 408,336" fill="none" stroke="black"></path><path d="M 8,400 L 336,400" fill="none" stroke="black"></path><path d="M 16,464 L 344,464" fill="none" stroke="black"></path><polygon points="344,400 332,394.4 332,405.6" fill="black" transform="rotate(0,336,400)"></polygon><polygon points="344,208 332,202.4 332,213.6" fill="black" transform="rotate(0,336,208)"></polygon><polygon points="344,80 332,74.4 332,85.6" fill="black" transform="rotate(0,336,80)"></polygon><polygon points="24,464 12,458.4 12,469.6" fill="black" transform="rotate(180,16,464)"></polygon><polygon points="24,272 12,266.4 12,277.6" fill="black" transform="rotate(180,16,272)"></polygon><polygon points="24,144 12,138.4 12,149.6" fill="black" transform="rotate(180,16,144)"></polygon><g><text x="28" y="36">Client</text> <text x="316" y="36">Resource</text> <text x="92" y="68">QUERY with content</text> <text x="308" y="116">200 OK</text> <text x="276" y="132">Validator: foo</text> <text x="92" y="180">QUERY with content</text> <text x="108" y="196">(conditional on 'foo')</text> <text x="268" y="244">304 Not Modified</text> <text x="276" y="260">Validator: foo</text> <text x="348" y="324">State Change</text> <text x="92" y="372">QUERY with content</text> <text x="108" y="388">(conditional on 'foo')</text> <text x="308" y="436">200 OK</text> <text x="276" y="452">Validator: bar</text> </g></svg> [¶](#appendix-A.5-16.1.2)

:

<svg xmlns="http://www.w3.org/2000/svg" version="1.1" height="512px" width="560px" viewBox="0 0 560 512" text-anchor="middle" font-family="monospace" font-size="13px" stroke-linecap="round"><path d="M 8,48 L 8,496" fill="none" stroke="black"></path><path d="M 264,48 L 264,192" fill="none" stroke="black"></path><path d="M 432,336 L 432,368" fill="none" stroke="black"></path><path d="M 488,88 L 488,328" fill="none" stroke="black"></path><path d="M 488,376 L 488,496" fill="none" stroke="black"></path><path d="M 552,336 L 552,368" fill="none" stroke="black"></path><path d="M 8,80 L 256,80" fill="none" stroke="black"></path><path d="M 264,96 L 480,96" fill="none" stroke="black"></path><path d="M 16,176 L 264,176" fill="none" stroke="black"></path><path d="M 8,240 L 480,240" fill="none" stroke="black"></path><path d="M 16,304 L 488,304" fill="none" stroke="black"></path><path d="M 432,336 L 552,336" fill="none" stroke="black"></path><path d="M 432,368 L 552,368" fill="none" stroke="black"></path><path d="M 8,416 L 480,416" fill="none" stroke="black"></path><path d="M 16,480 L 488,480" fill="none" stroke="black"></path><polygon points="488,416 476,410.4 476,421.6" fill="black" transform="rotate(0,480,416)"></polygon><polygon points="488,240 476,234.4 476,245.6" fill="black" transform="rotate(0,480,240)"></polygon><polygon points="264,80 252,74.4 252,85.6" fill="black" transform="rotate(0,256,80)"></polygon><polygon points="24,480 12,474.4 12,485.6" fill="black" transform="rotate(180,16,480)"></polygon><polygon points="24,304 12,298.4 12,309.6" fill="black" transform="rotate(180,16,304)"></polygon><polygon points="24,176 12,170.4 12,181.6" fill="black" transform="rotate(180,16,176)"></polygon><circle cx="488" cy="96" r="6" fill="white" stroke="black"></circle><g><text x="28" y="36">Client</text> <text x="236" y="36">Resource</text> <text x="92" y="68">QUERY with content</text> <text x="416" y="68">Equivalent Resource</text> <text x="428" y="84">(generates /xyz)</text> <text x="228" y="132">200 OK</text> <text x="196" y="148">Validator: foo</text> <text x="196" y="164">Location: /xyz</text> <text x="32" y="212">GET</text> <text x="108" y="228">(conditional on 'foo')</text> <text x="412" y="276">304 Not Modified</text> <text x="420" y="292">Validator: foo</text> <text x="492" y="356">State Change</text> <text x="32" y="388">GET</text> <text x="108" y="404">(conditional on 'foo')</text> <text x="452" y="452">200 OK</text> <text x="420" y="468">Validator: bar</text> </g></svg> [¶](#appendix-A.5-17.1.2)

:

### A.6.

The following examples show requests on a JSON-shaped \[\] database of RFC errata.[¶](#appendix-A.6-1)

The request below uses eXtensible Stylesheet Language Transformations (XSLT) to extract errata information summarized per year and the defined errata types.[¶](#appendix-A.6-2)

```
QUERY /errata.json HTTP/1.1
Host: example.org
Content-Type: application/xslt+xml
Accept: application/xml, text/csv

<transform xmlns="http://www.w3.org/1999/XSL/Transform"
  xmlns:j="http://www.w3.org/2005/xpath-functions"
  version="3.0">

  <output method="text"/>

  <param name="input"/>

  <variable name="json"
    select="json-to-xml(unparsed-text($input))"/>

  <variable name="sc">errata_status_code</variable>
  <variable name="sd">submit_date</variable>

  <template match="/">
    <text>year, total, rejected, verified, hdu, reported</text>
    <text>&#10;</text>
    <variable name="en" select="$json//j:map"/>
    <for-each-group select="$en"
      group-by="substring-before(j:string[@key=$sd],'-')">
      <sort select="current-grouping-key()"/>
      <variable name="year" select="current-grouping-key()"/>
      <variable name="errata" select=
        "$en[$year=substring-before(j:string[@key=$sd],'-')]"/>
      <value-of select="concat(
        $year,
        ', ',
        count($errata),
        ', ',
        count($errata['Rejected'=j:string[@key=$sc]]),
        ', ',
        count($errata['Verified'=j:string[@key=$sc]]),
        ', ',
        count(
          $errata['Held for Document Update'=j:string[@key=$sc]]),
        ', ',
        count($errata['Reported'=j:string[@key=$sc]]),
        '&#10;')"/>
    </for-each-group>
  </template>

</transform>
```

[¶](#appendix-A.6-3)

Response:[¶](#appendix-A.6-4)

```
HTTP/1.1 200 OK
Content-Type: text/csv
Accept-Query: "application/jsonpath", "application/xslt+xml"
Date: Wed, 19 Feb 2025, 17:10:01 GMT

year, total, rejected, verified, hdu, reported
2000, 14, 0, 14, 0, 0
2001, 72, 1, 70, 1, 0
2002, 124, 8, 104, 12, 0
2003, 63, 0, 61, 2, 0
2004, 89, 1, 83, 5, 0
2005, 156, 10, 96, 50, 0
2006, 444, 54, 176, 214, 0
2007, 429, 48, 188, 193, 0
2008, 423, 52, 165, 206, 0
2009, 331, 39, 148, 144, 0
2010, 538, 80, 232, 222, 4
2011, 367, 47, 170, 150, 0
2012, 348, 54, 149, 145, 0
2013, 341, 61, 169, 106, 5
2014, 342, 73, 180, 72, 17
2015, 343, 79, 145, 89, 30
2016, 295, 46, 122, 82, 45
2017, 303, 46, 120, 84, 53
2018, 350, 61, 118, 98, 73
2019, 335, 47, 131, 94, 63
2020, 387, 68, 117, 123, 79
2021, 321, 44, 148, 63, 66
2022, 358, 37, 198, 40, 83
2023, 262, 38, 121, 33, 70
2024, 322, 33, 125, 23, 141
9999, 1, 0, 0, 1, 0
```

[¶](#appendix-A.6-5)

Note the Accept-Query response field indicating that another query format, JSONPath \[\], is supported as well. The request below would report the identifiers of all rejected errata submitted since 2024:[¶](#appendix-A.6-6)

```
QUERY /errata.json HTTP/1.1
Host: example.org
Content-Type: application/jsonpath
Accept: application/json

$..[
     ?@.errata_status_code=="Rejected"
     && @.submit_date>"2024"
   ]
   ["doc-id"]
```

[¶](#appendix-A.6-7)

Response:[¶](#appendix-A.6-8)

```
HTTP/1.1 200 OK
Content-Type: application/json
Accept-Query: "application/jsonpath", "application/xslt+xml"
Date: Thu, 20 Feb 2025, 09:55:42 GMT
Last-Modified: Thu, 20 Feb 2025 06:10:01 GMT

[
  "RFC1185","RFC8407","RFC6350","RFC8467","RFC1157","RFC9543",
  "RFC9076","RFC7656","RFC2822","RFC9460","RFC2104","RFC6797",
  "RFC9499","RFC9557","RFC2131","RFC2328","RFC9001","RFC3325",
  "RFC9438","RFC2526","RFC2985","RFC7643","RFC9132","RFC6376",
  "RFC9110","RFC9460","RFC7748","RFC9497","RFC8463","RFC4035",
  "RFC7239","RFC9083","RFC9537","RFC9537","RFC9420","RFC9000",
  "RFC9656","RFC9110","RFC2324","RFC2549","RFC6797","RFC2549",
  "RFC8894"
]
```

[¶](#appendix-A.6-9)

## Appendix B.

The "Hypertext Transfer Protocol (HTTP) Method Registry" (< [http://www.iana.org/assignments/http-methods](http://www.iana.org/assignments/http-methods) >) already contains three other methods with the properties "safe" and "idempotent": "PROPFIND" \[\], "REPORT" \[\], and "SEARCH" \[\].[¶](#appendix-B-1)

It would have been possible to reuse any of these, updating it in a way that it matches what this specification defines as the new method "QUERY". Indeed, the early stages of this specification used "SEARCH".[¶](#appendix-B-2)

The method name "QUERY" ultimately was chosen because:[¶](#appendix-B-3)

- The alternatives use a generic media type for the request content ("application/xml"); the semantics of the request depend solely on the request content.[¶](#appendix-B-4.1)
- Furthermore, they all originate from the WebDAV activity, about which many have mixed feelings.[¶](#appendix-B-4.2)
- "QUERY" captures the relation with the URI's query component well.[¶](#appendix-B-4.3)

## Acknowledgements

We thank all members of the HTTP Working Group for their ideas, reviews, and feedback.[¶](#appendix-C-1)

The following individuals deserve special recognition:,,,,,, and.[¶](#appendix-C-2)

## Contributors

participated in early discussions leading to this specification:[¶](#appendix-D-1)

Ashok Malhotra

Email: [malhotrasahib@gmail.com](mailto:malhotrasahib@gmail.com)

Discussion on this HTTP method was reopened by during the HTTP Workshop in 2019:[¶](#appendix-D-2)

Asbjørn Ulsberg

Email: [asbjorn@ulsberg.no](mailto:asbjorn@ulsberg.no)

URI: [https://asbjor.nu/](https://asbjor.nu/)

## Authors' Addresses

Julian Reschke

greenbytes GmbH

Hafenweg 16

48155 Münster

Germany

Email: [julian.reschke@greenbytes.de](mailto:julian.reschke@greenbytes.de)

URI: [https://greenbytes.de/tech/webdav/](https://greenbytes.de/tech/webdav/)

James M Snell

Cloudflare

Email: [jasnell@gmail.com](mailto:jasnell@gmail.com)

Mike Bishop

Akamai

Email: [mbishop@evequefou.be](mailto:mbishop@evequefou.be)