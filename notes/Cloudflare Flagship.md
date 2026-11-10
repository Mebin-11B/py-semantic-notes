---
title: "Cloudflare Flagship"
url: https://developers.cloudflare.com/flagship/
clipped: 2026-06-17 00:56:50
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Cloudflare Flagship](https://developers.cloudflare.com/flagship/)

## Digest Summary
Flagship is Cloudflare’s feature‑flag service that enables safe, code‑free feature rollouts. Flags are defined with targeting rules and percentage‑based rollouts, then evaluated directly in Cloudflare Workers via a native binding. The service conforms to the CNCF OpenFeature standard, allowing the @cloudflare/flagship SDK to be used from Workers, Node.js, or browsers and to replace other providers by a single configuration change. Key capabilities include:

- Type‑safe Worker binding with automatic default fallbacks.  
- OpenFeature provider for cross‑runtime flag evaluation.  
- Targeting rules supporting 11 comparison operators, logical AND/OR grouping, and sequential evaluation.  
- Percentage rollouts using consistent hashing to ensure stable user assignment.  
- Multi‑type flag variations (boolean, string, number, JSON) for delivering full configuration objects.  
- Dashboard‑driven flag management, organized into apps per project or service.  

Flagship leverages Cloudflare’s global key‑value store for distributed flag configuration delivery.

## Discussion Summary
The discussion centers on Cloudflare’s Flagship client SDK, noting the security warning that a shared API token can expose flag data across all apps and urging caution when used in public‑facing environments. Commenters compare this approach to other providers such as Statsig, LaunchDarkly, and OpenFeature, highlighting preferences for server‑side evaluation, fine‑grained permissions, and robust rollout controls. While many appreciate Cloudflare’s expanding free tier and integration potential, concerns persist about token scope, permission management, and the maturity of the feature‑flag ecosystem.

---

## Full Article

Ship features safely with feature flags.

Flagship is Cloudflare's feature flag service. It lets you control feature visibility in your applications without redeploying code. Define flags with targeting rules and percentage-based rollouts, then evaluate them directly inside your Workers through a [native binding](https://developers.cloudflare.com/flagship/binding/).

[OpenFeature â](https://openfeature.dev/) is the CNCF open standard for feature flag management. Flagship is compatible with OpenFeature, so you can use the [`@cloudflare/flagship` â](https://www.npmjs.com/package/@cloudflare/flagship) SDK from any JavaScript runtime â Workers, Node.js, or the browser â and swap providers without changing evaluation code.

Check out the [Get started guide](https://developers.cloudflare.com/flagship/get-started/) to create your first feature flag.

### Worker binding

Evaluate flags with a native Workers binding. Type-safe methods with automatic fallback to defaults.

 [Binding reference](https://developers.cloudflare.com/flagship/binding/)

### OpenFeature SDK

Use the [`@cloudflare/flagship` â](https://www.npmjs.com/package/@cloudflare/flagship) OpenFeature provider to evaluate flags from Workers, Node.js, or browsers. Switch from another flag provider by changing one line of configuration.

 [View SDK docs](https://developers.cloudflare.com/flagship/sdk/)

### Targeting rules

Serve different flag values based on user attributes. Rules support 11 comparison operators, logical AND/OR grouping, and sequential evaluation.

 [Learn about targeting](https://developers.cloudflare.com/flagship/targeting/)

### Percentage rollouts

Gradually release features to a percentage of users. Consistent hashing ensures the same user always receives the same flag value.

 [Learn about rollouts](https://developers.cloudflare.com/flagship/targeting/percentage-rollouts/)

### Multi-type variations

Flag variations can be booleans, strings, numbers, or structured JSON objects. Use object variations to deliver entire configuration blocks as a single flag.

 [Use Multi-type variations](https://developers.cloudflare.com/flagship/concepts/)

### Flag management

Create, update, and delete flags through the Cloudflare dashboard. Organize flags into apps that map to your projects or services.

 [Use Flag management](https://developers.cloudflare.com/flagship/get-started/)

---

**[Workers](https://developers.cloudflare.com/workers/)** 

Build serverless applications on Cloudflare's global network. Flagship integrates natively with Workers through a binding.

**[KV](https://developers.cloudflare.com/kv/)** 

Store key-value data across Cloudflare's global network. Flagship uses this infrastructure to deliver flag configurations.

[Developer Discord](https://discord.cloudflare.com)

Connect with the Workers community on Discord to ask questions, show what you
are building, and discuss the platform with other developers.

[@CloudflareDev](https://x.com/cloudflaredev)

Follow @CloudflareDev on Twitter to learn about product announcements and what
is new in Cloudflare Workers.