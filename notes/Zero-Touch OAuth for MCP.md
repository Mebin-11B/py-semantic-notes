---
title: "Zero-Touch OAuth for MCP"
url: https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/
clipped: 2026-08-31 12:22:57
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Zero-Touch OAuth for MCP](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/)

## Digest Summary
Enterprise‑Managed Authorization (EMA) is a stable MCP extension that lets organizations control server access centrally via their identity provider (IdP). During single sign‑on, the client receives an Identity Assertion JWT Authorization Grant (ID‑JAG) from the IdP, exchanges it for an MCP access token, and bypasses per‑server consent screens. Key outcomes are: one‑time authorization that propagates to all authorized servers, centralized policy‑definition and audit in the IdP console, and separation of corporate and personal accounts. Early adopters include Okta (first supported IdP with Cross App Access), Anthropic and Visual Studio Code (client implementations), and servers such as Asana, Atlassian, Canva, Figma, Granola, Linear, and Supabase. The extension aims to eliminate the high‑friction, per‑user consent model that hinders enterprise MCP deployments, improving security, observability, and user experience. Participation is invited through the EMA Interest Group, and the spec is documented in SEP‑990 and the ext‑auth repository.

---

## Full Article

[Skip to content](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#main-content)
Table of Contents
- [Per-user auth is high friction](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#per-user-auth-is-high-friction)
- [Authorize once, inherit everywhere](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#authorize-once-inherit-everywhere)
- [Early adopters](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#early-adopters)
- [Get involved](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#get-involved)
- [Acknowledgements](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#acknowledgements)

The Enterprise-Managed Authorization extension is now stable. Organizations can centrally
manage authorization for MCP servers and end-users can access all connected MCP servers
through a single log in. The extension is being adopted by Anthropic, Microsoft, Okta and
a growing number of MCP servers.

The [Enterprise-Managed Authorization (EMA) extension](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization)
is now stable. We’ve heard from the community that authorization and repeated consent
prompts from connected MCP servers is one of the biggest pain points when it comes to
managing connectivity in enterprise environments. This extension helps address this.

EMA allows organizations to control MCP server access centrally through their trusted
identity provider. For end-users, this means a zero-touch setup: the MCP servers they
need are connected on first login, with no per-app OAuth and nothing to configure as a
one-off.

## Per-user auth is high friction[#](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#per-user-auth-is-high-friction)

The standard MCP authorization model was designed to be user-scoped and bound to the
traditional interactive auth conventions. While this might work well for more general
consumer scenarios where individuals decide what touches their data, this doesn’t quite
scale for enterprise deployments:
- Every employee has to authorize every server individually: onboarding means
manually connecting service after service.
- Security teams cannot enforce consistent policy: access is whatever each user
authorized, with no central control or audit trail.
- Work and personal accounts blur together: there’s no way to require a corporate
identity, so a user can connect a personal account to a work tool.

This combination of factors slows MCP adoption and pushes people toward brittle
workarounds. With no universal standard for preserving shared auth state, everyone
invents their own bespoke solution. The data and tools are available, but the per-user
authorization tax keeps most of them switched off.

## Authorize once, inherit everywhere[#](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#authorize-once-inherit-everywhere)

[Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization)
makes the organization’s IdP the authoritative decision-maker for MCP server access.
Administrators define the policy once and users can authenticate with their existing
identity into the MCP host. The IdP can grant or deny access based on group membership,
role, and conditional access rules.

Under the hood, the client obtains an
[Identity Assertion JWT Authorization Grant (ID-JAG)](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/)
from the IdP during single sign-on and exchanges it for an access token from the MCP
server’s authorization server. The user is never redirected through a per-server consent
screen. Three properties fall out of that flow:
- Authorize once, inherit everywhere: admins enable a server for the org. Users get
it automatically, scoped to the groups and roles they already have.
- Centralized policy and audit: access decisions live in the IdP admin console, with
one auditable trail across every connector.
- Removing personal/enterprise mixups: by removing the interactive account selection
step, it’s much easier to prevent data flowing between personal and enterprise accounts
by mistake or compromise.

We see this as a brand new baseline for MCP in the enterprise. When users log in, their
client should be connected to the tools and data they’re authorized to use with no extra
steps in between.

## Early adopters[#](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#early-adopters)

This launch brought together three groups that collaborated closely on making the
implementation real:
- Identity providers: Okta is the first supported identity provider. Organizations
using Okta can provision MCP access to supported servers through any supported client,
using
[Okta’s Cross App Access (XAA)](https://www.okta.com/identity-101/cross-app-access-securing-ai-agent-and-app-to-app-connections/).
- Clients:
[Anthropic has implemented the extension](https://claude.com/blog/enterprise-managed-auth)
in its shared MCP layer for Claude. Admins can authorize MCP servers for users across
Claude, Claude Code, and Cowork. Additionally,
[Visual Studio Code has also added support](https://code.visualstudio.com/updates/v1_123#_enterprise-managed-mcp-authentication-preview)
for EMA right in the IDE.
- Servers: Asana, Atlassian, Canva, Figma, Granola, Linear and Supabase now support
EMA, with Slack and more actively adding support.

We’re excited for more identity providers, clients, and servers to adopt
Enterprise-Managed Auth to help reduce the authorization-related fatigue and
significantly improve the security and observability posture for its implementers.

“The momentum around MCP is incredible, but as we move toward an interconnected AI
workforce, security can’t be an afterthought. By embedding the Cross App Access protocol
into MCP as the Enterprise-Managed Authorization extension, we turn identity into a
centralized governance plane and give security teams strict compliance control and users
a seamless, secure experience.”

— Aaron Parecki, Director of Identity Standards, Okta

“The Figma MCP brings the power of code and canvas together so teams can move faster,
explore more and ship products that stand out. As MCP adoption grows, XAA makes it
easier for enterprises to scale their MCP deployments securely without slowing teams
down.”

— Devdatta Akhawe, VP of Engineering, Figma

“Logging in once and automatically having all your MCP connectors automatically setup is
pretty magical.”

— Tom Moor, Head of Engineering, Linear

## Get involved[#](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#get-involved)

As with all other MCP extensions, features, and enhancements, we welcome your input.
We’re encouraging clients, servers, and identity platforms to review the extension
specification and add support for the new standard into their products:
- Read the requirements: the
[Enterprise-Managed Authorization page](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization)
documents the flow for clients, servers, and authorization servers.
- Source and spec: see the
[ext-auth repository](https://github.com/modelcontextprotocol/ext-auth) and the
[specification](https://github.com/modelcontextprotocol/ext-auth/blob/main/specification/stable/enterprise-managed-authorization.mdx)
for the latest in EMA evolution as well as any support materials that will help you get
started.

If you’re interested in discussing the extension, sharing compatibility reports, or
iterating on the extension, join the
[EMA Interest Group](https://modelcontextprotocol.io/community/interest-groups/enterprise-managed-authorization).

## Acknowledgements[#](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/#acknowledgements)

Enterprise-Managed Authorization is the work of the MCP community: the authors of
SEP-990, the maintainers of the
[ext-auth repository](https://github.com/modelcontextprotocol/ext-auth), and the identity
and MCP providers
who tested early implementations and pushed the spec forward. Thank you to everyone who
contributed.
