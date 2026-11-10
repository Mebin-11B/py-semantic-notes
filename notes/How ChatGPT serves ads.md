---
title: "How ChatGPT serves ads"
url: https://www.buchodi.com/how-chatgpt-serves-ads-heres-the-full-attribution-loop/
clipped: 2026-06-17 01:10:34
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [How ChatGPT serves ads](https://www.buchodi.com/how-chatgpt-serves-ads-heres-the-full-attribution-loop/)

## Digest Summary
OpenAI’s ChatGPT ad platform injects “single_advertiser_ad_unit” objects into the SSE conversation stream while the model generates a response. Each ad contains structured metadata: a stable advertiser ID (adacct_), brand info, carousel cards, and four Fernet‑encrypted tokens (ads_spam_integrity_payload, oppref, olref, ad_data_token). The ad payload is delivered from OpenAI’s CDN (bzrcdn.openai.com); clicking a card opens the merchant URL in an in‑app webview, preserving the tokens as query parameters.

On the merchant side, the OAIQ JavaScript SDK (hosted on the same CDN) reads the oppref token from the URL, stores it in a first‑party cookie (__oppref, TTL 720 h), and posts JSON events to bzr.openai.com/v1/sdk/events with a merchant pixel ID. The SDK also sets a probe cookie (__oaiq_domain_probe). The four tokens serve distinct purposes: server‑side click integrity, forward attribution (oppref), impression logging (olref), and additional encrypted data (ad_data_token). Token timestamps are recoverable from the public Fernet header. Blocking domains bzrcdn.openai.com and bzr.openai.com and inspecting the two cookies can interrupt the attribution loop.

## Discussion Summary
The comments express predominantly critical views toward OpenAI’s introduction of ads, questioning whether it signals financial pressure and lamenting a shift toward “enshittification.” Many highlight concerns about ad intrusion, relevance, and potential manipulation of model output, while a few note that advertising may be inevitable for free‑tier services and appreciate the technical separation of ad streams. Skepticism about the company’s business model coexists with brief acceptance that ads are a common last‑resort revenue source, but overall sentiment remains distrustful and dissatisfied.

---

## Full Article

OpenAI's ad platform has two halves. On the ChatGPT side, the backend injects structured `single_advertiser_ad_unit` objects into the conversation SSE stream while the model is responding. On the merchant side, a tracking SDK called OAIQ runs in the visitor's browser and reports product views back to OpenAI. The two are tied together by Fernet-encrypted click tokens, four of them per ad.

I captured both halves on a consented mobile-traffic research fleet. Everything below comes from observed traffic.

How an ad gets into a conversation
----------------------------------

When you send a message to ChatGPT, the backend opens an SSE response at `chatgpt.com/backend-api/f/conversation`. Most events in that stream are model-output. Some are ad units. They look like this:

```
event: delta
data: {
  "type":           "single_advertiser_ad_unit",
  "ads_request_id": "069e89b3-c038-7764-8000-6e5a193e5f69",
  "ads_spam_integrity_payload": "gAAAAABp6Js_<...redacted...>",
  "preamble":       "",
  "advertiser_brand": {
    "name":        "Grubhub",
    "url":         "www.grubhub.com",
    "favicon_url": "https://bzrcdn.openai.com/cabfae7ead26b03d.png",
    "id":          "adacct_6984ed0ba55481a29894bb192f7773b4"
  },
  "carousel_cards": [{
    "title":     "Get Chinese Food Delivered",
    "body":      "Satisfy Your Cravings with Grubhub Delivery.",
    "image_url": "https://bzrcdn.openai.com/cabfae7ead26b03d.png",
    "target": {
      "type":  "url",
      "value": "https://www.grubhub.com/?utm_source=chatgptpilot&utm_medium=paid&utm_campaign=diner_gh_search_chatgpt_kw_traffic_nb_x_nat_x&utm_content=nbchinese&oppref=gAAAA<...>&olref=gAAAA<...>",
      "open_externally": false
    },
    "ad_data_token": "eyJwYXlsb2<...>"
  }]
}
```

Notes:

* `single_advertiser_ad_unit` is a typed schema. The naming implies siblings (multi-advertiser, etc.).
* `advertiser_brand.id` is `adacct_<32-hex>` — a stable per-merchant account identifier.
* Brand favicon and ad image both load from `bzrcdn.openai.com`. OpenAI hosts the advertiser's creative, not the merchant.
* `target.open_externally: false` opens the link in ChatGPT's in-app webview, so OpenAI observes the post-click navigation on top of any pixel signal.
* Four Fernet tokens per ad: `ads_spam_integrity_payload`, `oppref`, `olref`, and a base64-wrapped `ad_data_token`. Each is AES-128-CBC under a server-only key with HMAC-SHA256 integrity.

How ads get selected
--------------------

A single account in the panel received six different ads across six conversations on six different topics. The targeting is contextual to the chat:

| Conversation topic | Advertiser delivered |
| --- | --- |
| Beijing trip planning (Great Wall, Forbidden City) | Grubhub — "Get Chinese Food Delivered" |
| Beijing tour bookings | GetYourGuide — Great Wall tour, `ad_id=beijing003` |
| Beijing flights | Axel — `utm_term=vflight_beijing_03` |
| NBA playoffs | Gametime — `utm_campaign=nba&utm_content=playoffs` |
| Spring fashion/trends | Aritzia — `utm_campaign=chatgptpilot_trav3` |
| Productivity / slides | Canva — `utm_campaign=…link-clicks_products` |

Same account, different topic, different brand. I didn't find evidence one way or the other on whether targeting also incorporates prior conversation history.

The four-token attribution chain
--------------------------------

Every ad ships with four distinct Fernet-encrypted blobs. Their roles, based on where they appear:

1. **`ads_spam_integrity_payload`** sent inside the SSE data, never on the click URL. Server-side integrity check against forged ad clicks.
2. `oppref` present on the click URL and copied verbatim by the OAIQ pixel into the cookie `__oppref` (TTL 720 hours / 30 days). The forward attribution token. Travels with every subsequent merchant pixel event.
3. `olref` paired with `oppref` on the click URL but not stored by the SDK we observed. Likely impression-side / outbound-link-reference logging on OpenAI's servers.
4. **`ad_data_token`** base64-wrapped JSON containing yet another Fernet token. Carried in the SSE payload, presumably reconciled server-side at click time.

Fernet's first nine bytes are public: version byte `0x80` plus an 8-byte big-endian Unix timestamp. So the mint time of any of these tokens is recoverable without OpenAI's key:

```
import base64, struct, datetime
b = base64.urlsafe_b64decode("gAAAAABp7fdA" + "==")
print(datetime.datetime.utcfromtimestamp(struct.unpack(">Q", b[1:9])[0]))
# → 2026-04-26 11:30:08 UTC
```

The Home Depot click URL I captured was minted at 11:30:08; the browser fetched the merchant page at 11:31:43. Click latency: 95 seconds.

How the loop closes on the merchant side
----------------------------------------

User taps the card. Browser opens:

```
https://www.grubhub.com/?utm_source=chatgptpilot&...
                       &oppref=gAAAA<...>
                       &olref=gAAAA<...>
```

The merchant page loads the OAIQ SDK:

```
<script src="https://bzrcdn.openai.com/sdk/oaiq.min.js"></script>
<script>
  oaiq('init',    { pid: '<merchant pixel ID>' });
  oaiq('measure', 'contents_viewed', { ... });
</script>
```

`oaiq.min.js` is at version 0.1.3. On `init` it reads `?oppref=` from `window.location`, writes it into the first-party cookie `__oppref` with a 720-hour TTL, and sets a probe cookie `__oaiq_domain_probe`. Every subsequent `measure` call POSTs JSON to:

```
POST https://bzr.openai.com/v1/sdk/events?pid=<merchant>&st=oaiq-web&sv=0.1.3
```

> Two domains to add to your filter list if you want to block ChatGPT ad events: `bzrcdn.openai.com`, `bzr.openai.com`. Two cookie names to inspect after any ChatGPT-recommended click: `__oppref`, `__oaiq_domain_probe`.