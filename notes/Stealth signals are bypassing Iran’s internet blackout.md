---
title: "Stealth signals are bypassing Iran’s internet blackout"
url: https://spectrum.ieee.org/iran-internet-blackout-satellite-tv
clipped: 2026-06-17 01:16:35
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Stealth signals are bypassing Iran’s internet blackout](https://spectrum.ieee.org/iran-internet-blackout-satellite-tv)

## Digest Summary
In January 2026 Iran imposed a nationwide communications shutdown, cutting global internet access for over 90 million people. NetFreedom Pioneers responded with Toosheh, a one‑way data‑delivery system that piggybacks on free‑to‑air satellite TV. Using a digital video broadcasting (DVB) receiver, users capture an MPEG transport stream that carries compressed bundles of news, videos, software and tutorials in .ts format. The stream is broadcast via a Yahsat satellite over the Middle East; no subscription or two‑way link is required, making the transmission untraceable. To mitigate terrestrial jamming, Toosheh adds 5‑30 % redundant packets, enabling reconstruction of lost data. Operating costs are fixed—tens of thousands of dollars per month for satellite bandwidth—while end‑user hardware costs under $50. Since 2015, Toosheh has supported protests, delivered anti‑censorship tools, and expanded to public education, with plans for intelligent curation and offline sharing. It complements limited Starlink deployments, offering a low‑cost, resilient alternative for information access under severe internet blackouts.

## Discussion Summary
The feedback is largely critical, describing the proposed system as impractical and unused by Iranians who instead rely on VPNs and Shadowsocks‑type tunnels for real‑time communication. Commenters argue that a download‑only approach does not meet the need for interactive upload capabilities, and they view the redundancy technique as insufficient, likening it to a proof‑of‑work model that fails to address censorship circumvention effectively. Overall sentiment is disappointment with the solution’s relevance and effectiveness.

---

## Full Article

**On 8 January 2026,** the Iranian government imposed a near-total communications shutdown. It was the country’s first full information blackout: For weeks, the internet was off across all provinces while services including the government-run intranet, VPNs, text messaging, mobile calls, and even landlines were severely throttled. It was an unprecedented lockdown that left more than [90 million people](https://www.chathamhouse.org/2026/01/irans-internet-shutdown-signals-new-stage-digital-isolation) cut off not only from the world, but from one another.

Since then, connectivity has never fully returned. Following [U.S. and Israeli airstrikes](https://en.wikipedia.org/wiki/2026_Iran_war) in late February, Iran again imposed near-total restrictions, and people inside the country again saw global information flows dry up.

The original January shutdown came amid nationwide protests over the deepening economic crisis and political repression, in which millions of people chanted antigovernment slogans in the streets. While Iranian protests have become frequent in recent years, this was one of the most significant uprisings since the Islamic Revolution in 1979. The government responded quickly and brutally. One report put the death toll at [more than 7,000 confirmed deaths](https://www.en-hrana.org/the-crimson-winter-a-50-day-record-of-irans-2025-2026-nationwide-protests/) and more than 11,000 under investigation. Many sources believe the death toll could exceed 30,000.

Thirteen days into the January shutdown, we at [NetFreedom Pioneers](https://www.netfreedompioneers.org/) (NFP) turned to a system we had built for exactly this kind of moment—one that sends files over ordinary satellite TV signals. During the national information vacuum, our technology, called [Toosheh](https://www.netfreedompioneers.org/toosheh-datacasting-technology/), delivered real-time updates into Iran, offering a lifeline to millions starved of trusted information.

How Iran Censors the Internet
-----------------------------

I joined NetFreedom Pioneers, a nonprofit focused on anticensorship technology, in 2014. Censorship in [Iran](https://spectrum.ieee.org/tag/iran) was a defining feature of my youth in the 1990s. After the Islamic Revolution, most Iranians began to lead double lives—one at home, where they could drink, dance, and choose their clothing, and another in public, where everyone had to comply with stifling government laws.

![Photo of a helmeted soldier with a machine gun standing in front of an Iranian flag and cell tower.](https://spectrum.ieee.org/iran-internet-blackout-satellite-tv)Iran’s internet infrastructure is more centralized than in other parts of the world, making it easier for the government to restrict the flow of information. Morteza Nikoubazl/NurPhoto/Getty Images

My first experience with secret communications was when I was five and living in the small city of Fasa in southern Iran. My uncle brought home a satellite dish—dangerously illegal at the time—that allowed us to tune into 12 satellite channels. My favorite was Cartoon Network. Then, during my teenage years, this same uncle introduced me to the internet through dial-up modems. I remember using

[Yahoo](https://spectrum.ieee.org/tag/yahoo)

Mail with its 4 megabytes of storage, reading news from around the world, and learning about the Chandra X-ray telescope from NASA’s website.

That openness didn’t last. As internet use spread in the early 2000s, the Iranian government began reshaping the network itself. Unlike the highly distributed networks in the United States or Europe, where thousands of providers exchange traffic across many independent routes, Iran’s connection to the global internet is relatively centralized. Most international traffic passes through a small number of gateways controlled by state-linked telecom operators. That architecture gives authorities unusual leverage: By restricting or withdrawing those connections, they can sharply reduce the country’s access to the outside world.

Over the past decade, Iran has expanded this control through what it calls the [National Information Network](https://en.wikipedia.org/wiki/National_Information_Network), a domestically routed system designed to keep data inside the country whenever possible. Many government services, banking systems, and local platforms are hosted on this internal network. During periods of unrest, access to the global internet can be throttled or cut off while portions of this domestic network continue to function.

The government began its censorship campaign by redirecting or blocking websites. As internet use grew, it adopted more sophisticated approaches. For example, the [Telecommunication Company of Iran](https://en.wikipedia.org/wiki/Telecommunication_Company_of_Iran) uses a technique called [deep packet inspection](https://www.fortinet.com/resources/cyberglossary/dpi-deep-packet-inspection) to analyze the content of data packets in real time. This method enables it to identify and block specific types of traffic, such as VPN connections, messaging apps, social media platforms, and banned websites.

The Stealth of Satellite Transmissions
--------------------------------------

Toosheh’s communication workaround builds on a history of satellite TV adoption in Middle Eastern and North African countries. By the early 2000s, satellite dishes were common in Iran; today the majority of households in Iran have access to satellite TV despite its official prohibition.

Unlike subscription services such as DirecTV and Dish Network, “free-to-air” satellite TV broadcasts are unencrypted and can be received by anyone with a dish and receiver—no subscription required. Because the signals are open, users can also capture and store the data they carry, rather than simply watching it live. Tech-savvy people learned that they could use a digital video broadcasting (DVB) card—a piece of hardware that connects to a computer and tunes into satellite frequencies—to transform a personal computer into a satellite receiver. This way, they could watch and store media locally as well as download data from dedicated channels.

![Photo of satellite dishes adorning the side of an apartment building.](https://spectrum.ieee.org/iran-internet-blackout-satellite-tv)Many Iranian citizens have free-to-air satellite dishes, like the ones on this apartment building in Tehran, and can thus download Toosheh transmissions, giving them a lifeline during internet blackouts.Morteza Nikoubazl/NurPhoto/Getty Images

Toosheh, a Persian word that translates to “knapsack,” is the brainchild of [Mehdi Yahyanejad](https://x.com/mehdiy_fa), an Iranian-American technologist and entrepreneur. Yahyanejad cofounded NetFreedom Pioneers in 2012. He proposed that the satellite-computer connections enabled by a DVB card could be re-created in software, eliminating the need for specialized hardware. He added a simple digital interface to the software to make it easy for anyone to use. The next breakthrough came when the NFP team developed a new transfer protocol that tricks ordinary satellite receivers into downloading data alongside audio and video content. Thus, Toosheh was born.

Satellite TV uses a file system called an [MPEG transport stream](https://en.wikipedia.org/wiki/MPEG_transport_stream) that allows multiple audio, video, or data layers to be packaged into a single stream file. When you tune in to a satellite channel and select an audio option or closed captions, you’re accessing data stored in different parts of this stream. The NFP team’s insight was that, by piggybacking on one of these layers, Toosheh could send an MPEG stream that included documents, videos, and more.

![An illustration of an 8 step process for sending digital files via satellite TV signals.](https://spectrum.ieee.org/iran-internet-blackout-satellite-tv) HOW TOOSHEH WORKS: At NetFreedom Pioneers, content curators pull together files—news articles, videos, audio, and software [1]. Toosheh’s encoder software [2] compresses the files into a bundle, in .ts format, creating an MPEG transport stream [3]. From there, it’s uploaded to a server for transmission [4] via a free-to-air TV channel on a Yahsat satellite that’s positioned over the Middle East to provide regional coverage [5]. Satellite receivers [6] directly capture the data streams, which are downloaded to computers, smartphones, and other devices, and decoded by Toosheh software [8].Chris Philpot

A satellite receiver can’t tell the difference between our data and normal satellite audio and video data since it only “sees” the MPEG streams, not what’s encoded on them. This means the data can be downloaded and read, watched, and saved on local devices such as computers, smartphones, or storage devices. What’s more, the system is entirely private: No one can detect whether someone has received data through Toosheh; there are no traceable logs of user activity.

Toosheh doesn’t provide internet access, but rather delivers curated data through satellite technology. The fundamental distinction lies in the way users interact with the system. Unlike traditional internet services, where you type a request into your browser and receive data in response, Toosheh operates more like a combination of radio and television, presenting information in a magazine-like format. Users don’t make requests; instead, they receive 1 to 5 gigabytes of prepackaged, carefully selected data.

Access to information is not only about news or politics, but about exposure to possibilities.

During this year’s internet blackout, we distributed official statements from Iranian opposition leader Crown Prince Reza Pahlavi and the U.S. government. We provided first-aid tutorials for medics and injured protesters. We sent uncensored news reports from BBC Persian, Iran International, IranWire, VOA Farsi, and others. We also shared critical software packages including anticensorship and antisurveillance tools, along with how-to guides to help people securely connect to Starlink satellite terminals, allowing them to stay protected and anonymous as they sent their own communications.

How to Combat Signal Interference
---------------------------------

Because Toosheh relies on one-way satellite broadcasts, it evades the usual tactics governments use to block internet access. However, it remains vulnerable to [satellite signal jamming](https://spectrum.ieee.org/satellite-jamming).

The Iranian government is notorious for deploying signal jamming, especially in larger cities. In 2009, the government [used uplink interference](https://www.dw.com/fa-ir/%D9%86%D8%A7%D8%AA%D9%88%D8%A7%D9%86%DB%8C-%D8%AF%D8%B1-%D9%85%D9%82%D8%A7%D8%A8%D9%84-%D8%A7%D9%85%D9%88%D8%A7%D8%AC-%D9%BE%D8%A7%D8%B1%D8%A7%D8%B2%DB%8C%D8%AA-%D8%A7%D8%B2-%D8%AA%D9%87%D8%B1%D8%A7%D9%86/a-5417209), which attacks the satellite in orbit by beaming strong noise in the frequency of the satellite’s receiver. This makes it impossible for the satellite to distinguish the information it’s supposed to receive. However, because this type of attack temporarily disables the entire satellite, Iran was threatened with international [sanctions](https://www.dw.com/fa-ir/%D8%AA%D8%B4%D8%AF%DB%8C%D8%AF-%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D8%AF%D9%87%D8%A7-%D8%A8%D9%87-%D8%A7%D8%B1%D8%B3%D8%A7%D9%84-%D9%BE%D8%A7%D8%B1%D8%A7%D8%B2%DB%8C%D8%AA-%D8%A7%D8%B2-%D8%B3%D9%88%DB%8C-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86/a-5382663) and in 2012 stopped using the method .

![A chart displayed on a cellphone shows internet connectivity in Iran dropped from almost 100% to 0% on 9 January 2026.](https://spectrum.ieee.org/iran-internet-blackout-satellite-tv) A graph of network connectivity in Iran shows that on 9 January 2026, internet access dropped from nearly 100 percent to 0. Samuel Boivin/NurPhoto/Getty Images

The current method, called terrestrial jamming, uses antennas installed at higher elevations than the surrounding buildings to beam strong noise over a specific area in the frequency range of household receivers. This attack is effective in keeping some of the packets from arriving and damaging others, effectively jamming the transmission. But it’s short-range and requires significant power, so it’s impossible to implement nationwide. There are always people somewhere who can still watch TV, download from Toosheh, or tune into a satellite radio despite the jamming. Even so, we wanted a workaround that would keep our transmissions broadly accessible.

NFP’s solution was to add redundancy, similar in principle to a data-storage technique called RAID (redundant array of independent disks). Instead of sending each piece of data once, we send extra information that allows missing or corrupted packets to be reconstructed. Under normal circumstances, we often use 5 percent of our bandwidth for this redundancy. During periods of active jamming, we increase that to as much as 25 to 30 percent, improving the chances that users can recover complete files despite interference.

From Crisis Response to Public Access
-------------------------------------

Toosheh initially came online in 2015 in Iran and Afghanistan. Its full potential, however, was first realized during the 2019 protests in Iran, which saw the most widespread internet shutdown prior to the blackout this year. [**Wired**](https://www.wired.com/story/iran-news-internet-shutdown/) called the 2019 shutdown “the most severe disconnection” tracked by [NetBlocks](https://netblocks.org/) in any country in terms of its “technical complexity and breadth.” Our technology helped thousands of people stay informed. We sent crucial local updates, legal-aid guides, digital security tools, and independent news to satellite receivers all over the country, seeing a sixfold increase in our user base.

When that wave of protests subsided, the government allowed some communication services to return. People were again able to access the free internet using VPNs and other antifilter software that allowed them to bypass restrictions. Toosheh then became a public access point for news, educational material, and entertainment beyond government filtering.

Toosheh’s impact is often personal. A traveling teacher in western Iran told NFP that he regularly distributed Toosheh files to students in remote villages. One package included footage of female athletes competing in the Olympic Games, something never broadcast in Iran. For one young girl, it was the first time she realized women could compete professionally in sports. That moment underscores a broader truth: Access to information is not only about news or politics, but about exposure to possibilities.

The Cost of Toosheh
-------------------

Unlike internet-based systems, Toosheh’s operational cost remains constant regardless of the number of users. A single TV satellite in geostationary earth orbit, deployed and maintained by an international company such as Eutelsat, can broadcast to an entire continent with no increase in cost to audiences. What’s more, the startup cost for users isn’t high: A satellite dish and receiver in Iran costs less than US $50, which is affordable to many. And it costs nothing for people to use Toosheh’s service and receive its files.

We aim not just to build a tool for censorship circumvention, but to redefine access itself.

However, operating the service is costly: NetFreedom Pioneers pays tens of thousands of dollars a month for satellite bandwidth. We had received funding from the U.S. State Department, but in August of 2025, that funding ended, forcing us to suspend services in Iran.

Then the December protests happened, and broadcasting to Iran became an urgent priority. To turn Toosheh back on, we needed roughly $50,000 a month. With the support of a handful of private donors, we were able to meet these costs and sustain operations in Iran for a few months, though our future there and elsewhere is uncertain.

Satellites Against Censorship
-----------------------------

Toosheh’s revival in Iran came alongside NFP’s ongoing support for deployments of Starlink, a satellite internet service that allows users to connect directly to satellites rather than relying on domestic networks, which the government can shut down. Unlike Toosheh’s one-way broadcasts, [Starlink](https://spectrum.ieee.org/tag/starlink) provides full two-way internet access, enabling users to send messages, upload videos, and communicate with the outside world.

In 2022, we started gathering [donations](https://www.gofundme.com/f/urgent-help-deliver-starlink-and-vpn-access-for-freedom) to buy Starlink terminals for Iran. We have delivered more than 300 of the [roughly 50,000](https://www.theguardian.com/world/2026/jan/13/ecosystem-smuggled-tech-iran-last-link-outside-world-internet) there, enabling citizens to send encrypted updates and videos to us from inside the country. Because the technology is banned by the government, access remains limited and carries risk; Iranian authorities have recently arrested Starlink users and sellers. And unlike Toosheh’s receive-only broadcasts, Starlink terminals transmit signals back to orbit, creating a radio footprint that can potentially be detected.

![A photo of a laptop screen says the user is offline.](https://spectrum.ieee.org/iran-internet-blackout-satellite-tv) The internet shutdown in Iran continued after the attacks by Israel and the United States began in late February, preventing Iranians from communicating with the outside world and with one another.Fatemeh Bahrami/Anadolu/Getty Images

Looking ahead, we envision Toosheh becoming a foundational part of global digital resilience. It is uncensored, untraceable, and resistant to government shutdowns. Because Toosheh is downlink only, it can sometimes feel hard to explain the value of this technology to those living in the free world, those accustomed to open internet access. Yet, people living under censorship have few other choices when there’s a digital blackout.

Currently, NFP is developing new features like intelligent content curation and automatically prioritizing data packages based on geographic or situational needs. And we’re experimenting with local sharing tools that allow users who receive Toosheh broadcasts to redistribute those files via Wi-Fi hotspots or other offline networks, which could extend the system’s reach to disaster zones, conflict areas, and climate-impacted regions where infrastructure may be destroyed.

We’re also looking at other use cases. Following the Taliban’s return to power in Afghanistan, NetFreedom Pioneers designed a satellite-based system to deliver educational materials. Our goal is to enable private, large-scale distribution of coursework to anyone—including the girls who are banned from Afghanistan’s schools. The system is technically ready but has yet to secure funding for deployment.

We aim not just to build a tool for censorship circumvention, but to redefine access itself. Whether in an Iranian city under surveillance, a Guatemalan village without internet, or a refugee camp in East Africa, Toosheh offers a powerful and practical model for delivering vital information without relying on vulnerable or expensive networks.

Toosheh is a reminder that innovation doesn’t have to mean complexity. Sometimes, the most transformative ideas are the simplest, like delivering data through the sky, quietly and affordably, into the hands of those who need it most.

*This article appears in the May 2026 print issue as “The Stealth Signals Bypassing Iran’s Internet Blackout.”*

From Your Site Articles

Related Articles Around the Web