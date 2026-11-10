---
title: Setting up a free *.city.state.us locality domain (2025)
url: https://fredchan.org/blog/locality-domains-guide/
clipped: 2026-06-17 01:03:08
source: HackerNews Digest
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - domain name system
  - locality domains
  - internet governance
  - networking
related:
  - "[[Domain Name System]]"
  - "[[Locality Domains]]"
  - "[[Internet Governance]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A tutorial explaining how to register a free .city.state.us locality domain name in the United States using delegated regional managers and AWS DNS.
>
> **Key points:**
> - Locality domains (e.g., somename.city.state.us) are geographic domains created in 1992 and funded under government contract.
> - Registration requires setting up nameservers (such as AWS Lightsail) and submitting a specific domain registration template.
> - Processing is handled by regional delegated managers and can take days or weeks.
> - Locality domains offer WHOIS privacy as query results display only the registrar's info, not the registrant's details.
>
> **Concept links:** [[Domain Name System]], [[Locality Domains]], [[Internet Governance]], [[Networking]]
>
> **Suggested connections:**
> - [[Domain Name System]] — Details the configuration and delegation of local geographic subdomains.
> - [[Internet Governance]] — Explores the legacy administrative contracts that maintain the .us locality structure.
<!-- ai-summary:end -->

# [Setting up a free *.city.state.us locality domain (2025)](https://fredchan.org/blog/locality-domains-guide/)

## Digest Summary
Locality domains are U.S.-specific subdomains (e.g., somename.city.state.us) available for free to U.S. citizens, permanent residents, or entities with a bona‑fide U.S. presence. Registration is delegated to various private registrars; a 2009 list provides contact emails, though current contacts may need updating. If a domain is undelegated, only local government agencies can obtain it via NeuStar.

To register, you must first have functional nameservers, which can be obtained at no cost from Amazon Lightsail by creating a DNS zone and noting the provided nameserver hostnames. Next, complete the “Interim .US Domain Template v2.0,” supplying the fully‑qualified domain name, personal or organization details, a description, operational date, administrative/technical contacts, and the IP addresses of the Lightsail nameservers. Include the appropriate US‑Nexus category (e.g., natural person, U.S. citizen). Email the completed form to the identified registrar; processing may take days to weeks.

After approval, configure DNS records in Lightsail to point the domain to any target service (web, game, FTP, etc.). WHOIS queries for locality domains display only registrar information, not the registrant’s address.

## Discussion Summary
The comments express mixed feelings toward locality .us domains: many participants appreciate their short, inexpensive nature and see potential for civic or personal projects, while also noting significant bureaucratic hurdles such as notarized‑letter requirements and limited registrar support. Concerns are raised about privacy risks, reliability of hosting arrangements, and the disappearance of legacy ISPs that manage these domains. Users share nostalgic experiences, discuss technical workarounds, and suggest broader adoption or alternative city‑focused TLDs, highlighting both enthusiasm and frustration with the current system.

---

## Full Article

tl;dr
-----

In the US, you can get a domain name like `somename.city.state.us` for free. If your town has its own domain, you can get nameservers from Amazon Lightsail, send the *Interim .US Domain Template* to the delegated manager for your locality to register one, then point DNS entries at your webhost.

What’s a locality domain?
-------------------------

A locality domain is a domain name that’s associated with a location in the United States, such as `frederick.seattle.wa.us` (which currently redirects to fredchan.org). Locality domains were first created in 1992, and the infrastructure has been maintained under government contract ever since.

To register one, you must be a US citizen or permanent resident, an organization incorporated in the US, or an organization with a bona fide presence in the US that regularly engages in lawful activities or has an office in the US. (For the full verbiage, see the bottom of [this form](https://web.archive.org/web/20060210103628/http://www.nic.us/register/US_Domain_Template_v2.0.txt)).

Step 1: Choose a locality domain
--------------------------------

Registration of many locality domains have been delegated to various companies who actually handle the domain registration. See [the list of delegated subdomains](https://web.archive.org/web/20090909141302/http://neustar.us/register/delegated_subdomains.txt) for domains you can register under, which also has the contact e-mail for the corresponding registrar as of 2009.

Since this list is quite old and some companies may have restructured/renamed, you may need to hunt for an e-mail for the current incarnation of the registrar. For example, the e-mail listed for `seattle.wa.us` is `domainrq@nwnexus.com` belonging to NW Nexus, which is now NuOz Corporation, so the e-mail I contacted was `support@nuoz.com`.

If you do not live in one of these localities, you can try registering a domain under `gen.your-state.us`, like [next.gen.oh.us](https://www.next.gen.oh.us/), which is officially for *general independent entities*. The contact should be in the same list.

If the locality domain you’re looking for isn’t on the list (i.e. registration has not been delegated), you’re probably screwed. The manager of all undelegated domains, NeuStar, will only allow local government agencies to register them due to [government policy](https://www.ntia.gov/files/ntia/publications/mod_2_0.pdf). This is supposed to be temporary, but the policy has remained since 2002.

Step 2: Acquire nameservers
---------------------------

When you get a normal domain, like `fredchan.org`, your domain registrar usually provides nameservers for you after you buy. These nameservers are where you put DNS records that point your domain to an IP address, like your web host’s IP address. However, in order to register a locality domain, you need to already have nameservers.

The only place I could find that provides *free* nameservers for non-top level domains (e.g. every locality domain) is [Amazon Lightsail](https://aws.amazon.com/lightsail/). Lightsail is Amazon’s low cost AWS web hosting service. You’re normally supposed to rent a web hosting server from them, but you don’t actually need to do that.

1. Create an [AWS account](https://portal.aws.amazon.com/) and go to the [Lightsail console](https://lightsail.aws.amazon.com/).
2. On the left navigation panel, click `Domains & DNS`.
3. Click the `Create DNS zone` button.
4. Select `Use a domain from another registrar` and type in the domain you *intend* to register later.
5. Click `Create DNS zone`.
6. Take note of the domain names in the `Name servers` section. You need these when you fill out the domain registration form.

Step 3: Fill out the domain registration form
---------------------------------------------

Now that you have name servers, you can fill out the [Interim .US Domain Template v2.0](https://web.archive.org/web/20060210103628/http://www.nic.us/register/US_Domain_Template_v2.0.txt). In this section, I’ll walk you through some of the trickier parts of this form, assuming you are registering a domain for yourself.

### `2. FULLY-QUALIFIED DOMAIN NAME:`

This is the domain you want to register, e.g. `frederick.seattle.wa.us`.

### `3. ORGANIZATION INFORMATION`

If you are a human being and not an organization, you can fill out sections 3a-e with your own address.

### `4. DESCRIPTION OF ORGANIZATION/DOMAIN:`

Describe what you’re doing with this domain. For example, if you expect to host a website on it, you can say that. You can use it for purposes that you don’t write in the form later on as well.

### `5. Date Operational......:`

You can use your birth date here.

### `6. ADMINISTRATIVE CONTACT OF ORGANIZATION/DOMAIN` and `7. TECHNICAL AND ZONE CONTACT`

Both of these can be you. 6i, 7i, and 7j can all be your e-mail address, and if you don’t have a fax number, leave 7k blank.

### `8. PRIMARY SERVER: HOSTNAME, NETADDRESS` and `9. SECONDARY SERVER: HOSTNAME, NETADDRESS`

This is where you fill in your name server addresses.

Lightsail will have given you at least 2-4 name server addresses, of which you need to know the IP address of each. You can use an [online DNS lookup tool](https://mxtoolbox.com/DNSLookup.aspx) to find their IP addresses or the `dig` command in your terminal.

Any of the nameservers can be the primary server. Then, for the rest of the servers, you can repeat section 9 as many times as you need until you’ve added *all* the nameservers.

### `10. US NEXUS REQUIREMENTS`

Instructions for section 10 appear at the bottom of the form. For instance, if the domain is for personal use and you are a US Citizen, your application purpose is `(iii) personal use`, your Nexus Category is `(category 11) Natural person who is a United States Citizen`, and you leave Nexus Validator blank.

Step 4: Send the form and wait
------------------------------

Send the form to the domain registrar you identified before for your locality domain. When registering, I wrote *“I’d like to register a new locality domain with the following information”* and pasted the entire form contents into the e-mail, so they know what the form is for.

This can take days or possibly weeks, since they’re not usually automated. If successful, you’ll get an e-mail confirming that your domain has been registered.

Step 5: Finish setting up DNS in Lightsail
------------------------------------------

You can now go back to the DNS zone you created in Lightsail, and in the `DNS records` tab, create DNS records to point your domain to whatever server you want― web servers, Minecraft servers, FTP servers… anything!

For free web hosting, I use [GitHub Pages](https://pages.github.com/), which has a guide to [configuring custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages). Different web hosts will have slightly different instructions, but they will all involve creating DNS records.

Once your DNS records are configured, you should be able to visit your new locality domain and see your website!

FAQ
---

### Do I actually have to live in my locality domain’s area?

I’m not really sure. Honestly, I doubt anyone cares enough to actually check that you live at the address you supply in the registration form. I know someone who used to live in their locality, moved out of the country, and still has their locality domain. However, your mileage may vary.

### Will WHOIS requests leak my address?

Nope. Even though you must supply your address in the registration form, a WHOIS request for your locality domain will only show information about the registrar.

Special thanks
--------------

Big thanks goes to [sleepless](https://sleepless.seattle.wa.us/2022-07-01-110449/) and [Minh Nguyen](http://nguyen.cincinnati.oh.us/locality.html) for their guides on registering locality domains. After seeing their guides, I wanted to write my own that would clarify some of the questions I had while following them, which led to the creation of this article!
