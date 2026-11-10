---
title: "5NF and Database Design"
url: https://kb.databasedesignbook.com/posts/5nf/
clipped: 2026-06-17 01:17:21
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [5NF and Database Design](https://kb.databasedesignbook.com/posts/5nf/)

## Digest Summary
The article critiques common 5NF teaching examples as artificial and argues that proper design starts with a clear logical model derived from business requirements. It surveys three typical sources—the Wikipedia salesman/brand/product‑type case, the “ice‑cream” brand‑flavour‑friend scenario, and the “musicians” concert‑instrument‑musician example—and shows their shortcomings. From these, two generic patterns emerge:  

* **AB‑BC‑AC triangle** – three many‑to‑many links connecting three anchors (e.g., brands, flavours, friends). Implemented with three two‑column junction tables.  
* **ABC + D star** – a fourth anchor (Performance) links three primary anchors; links are 1:N and can be stored in a single table with either a composite primary key (concert_id, musician_id, instrument_id) or a synthetic ID plus a uniqueness constraint.

The article demonstrates how to choose composite versus synthetic keys based on uniqueness requirements and extends the models (e.g., adding specific preferences or musician skills). It concludes that 5NF decomposition is unnecessary when the logical model is built correctly; the two patterns yield fully normalized schemas without redundancy or anomalies.

## Discussion Summary
Commenters critique the 4NF definition as mischaracterized, arguing that multivalued dependency should be understood as a set of unique values and noting the article’s roundabout explanation highlights the combinatorial row explosion problem. Consensus views normal forms primarily as teaching tools that provide vocabulary rather than strict engineering specifications; they are valued after practical experience but recognized as having limitations and occasional justification for denormalization. Appreciation is expressed for the pragmatic style, while some observe that formalism can obscure common‑sense understanding, with occasional side remarks on related topics.

---

## Full Article

Author: Alexey Makhotkin [squadette@gmail.com](mailto:squadette@gmail.com), *(~3900 words)*

One of the goals of this publication is to deconstruct the traditional ways of teaching basic topics in relational databases. Previously we discussed the fourth normal form (4NF): “[Historically, 4NF explanations are needlessly confusing](https://minimalmodeling.substack.com/p/historically-4nf-explanations-are)”.

Letâs discuss the ultimate beast: **fifth normal form (5NF)**. Often itâs
presented even more confusingly than 4NF is, and we can show that this
presentation is unnecessary, and the confusion is completely
artificial.

Here is the roadmap of this post:

* Itâs essential to have good, well-motivated examples. We start with **a survey of examples** used in various texts that present 5NF.
* Wikipedia should have a good baseline explanation of a concept, but in the case of 5NF, it does not. We discuss **the problems with the Wikipedia example**.
* We discuss **a more logical sequence of designing tables**: a) start with business requirements, b) create a logical model, c) design physical table schema.
* We discuss the âice creamâ example, and **the AB-BC-AC triangle pattern** that naturally appears here.
* We discuss the âmusiciansâ example, and **the ABC+D star pattern** that appears here. For some business requirements, there is also a choice between using a composite or a synthetic primary key.
* Finally, we come to the conclusion that **you donât really need to involve 5NF to design your table schema**. You begin with the logical model, and apply a textbook table design strategy that preserves normalization.
* In two extra chapters we discuss extending both examples, with two different teaching points.

Table of contents
-----------------



Subscribe here to receive updates.

---

Sources
-------

First, we need to list the teaching scenarios that are used in the commonly available sources.

**Wikipedia**: *Salesman / Brand / Product Type*, with the following relationships:

* Salesman sells product types (e.g. âvacuum cleanerâ);
* Salesman sells brands (e.g. âPhilipsâ);
* Brands offer product types;

<https://en.wikipedia.org/w/index.php?title=Fifth_normal_form&oldid=1344596188#Example>

**Decomplexify**: *Ice cream brands / Flavours / Friends*, with the following relationships:

* Brands offer flavours (e.g., Frostyâs offers Vanilla, Chocolate, Strawberry, and Mint);
* Friends like flavours (e.g. Jason likes vanilla and chocolate);
* Friends like brands (e.g., Jason likes Frostyâs and Alpine);

<https://www.youtube.com/watch?v=GFQaEYEc8_8&t=1427s> (see also the âcorrectionsâ in the pinned comment).

**Data Demythed** blog by Barry Johnson: *Concerts / Musicians / Instruments / Performances*.

* Musician participates in a Concert;
* Musician is able to play an Instrument;
* Musician plays an Instrument at a certain Concert;

<https://datademythed.com/posts/5nf_missing_use_case/>  
(I particularly recommend the â*In Conclusion*â section)

Barryâs text also discusses the traditional poor treatment of 5NF.
Back then both of us had a discussion in the comments, which helped me
to make some progress in understanding. Here Iâll discuss my treatment
of this business case, because it seems to be structurally different
from the previous two examples.

Making sense of Wikipedia example
---------------------------------

Wikipedia presents its example in a roundabout way. First it shows a three-column table (*âTraveling salesmanâ, âBrandâ, âProduct typeâ*).

![Wikipedia example: traveling-salesman product availability by brand](https://kb.databasedesignbook.com/posts/5nf/wikipedia-1.png)

What does this table mean? Letâs discuss later.

Then there is the following quote:

> âIn the absence of any rules restricting the valid possible combinations of traveling salespeople, brand, and product type, the three-attribute table above is necessary in order to model the situation correctly.

> Suppose, however, that the following rule applies: *A traveling salesperson has certain brands and certain product types in their repertoire. If brand B1 and brand B2 are in their repertoire, and product type P is in their repertoire, then (assuming brand B1 and brand B2 both make product type P), the traveling salesperson must offer product type P from both brands; that is, the salesperson cannot sell only B1’s product P or only B2’s product P*.

> In that case, it is possible to split the table into three:

> ![Wikipedia example: Product types by traveling salesman / Brands by traveling salesman / Product types by brand](https://kb.databasedesignbook.com/posts/5nf/wikipedia-2.png)

> In this case, it’s impossible for Louis Ferguson to refuse to offer vacuum cleaners made by Acme (assuming Acme makes vacuum cleaners) if he sells anything else made by Acme (lava lamp) and he also sells vacuum cleaners made by any other brand (Robusto).â

The âimpossible to refuseâ wording, and the entire premise of âmust offer product type P from both brandsâ describe a weird scenario. I am not sure if it ever happens in real life.

Setting the tables aside: the rule itself is weird, it means that we cannot handle the normal case. If I want to start selling Robusto vacuum cleaners then I must also start selling Acme vacuum cleaners. If I want to sell Acme breadboxes, I must also sell Acme vacuum cleaners.

This makes no business sense, and because of that you wonât understand 5NF from this example. Nowadays I probably understand what this contrived wording is trying to achieve pedagogically, but I think that itâs failing at that. Itâs not useful for understanding database design.

Begin with logical model
------------------------

The entire premise is illogical. A table is presented, and we ask: what could be the meaning of this table? Then we split this table into three tables, and we ask again: what could be the meaning of those tables? We ask: what if there was this extra rule that makes very little sense, if weâd take it into account would we interpret the tables differently?

Instead, we must begin with the logical model that corresponds to the actual business scenario. When the logical model is complete, we can build a physical schema, using a textbook table design strategy. The result would be perfectly normalized: no redundancy, and no anomalies.

Two logical design patterns arise around 5NF:

* **AB-BC-AC triangle** (see the âice creamâ example below), and
* **ABC+D star pattern** (see the âmusiciansâ example).

AB-BC-AC triangle: the âice creamâ example
----------------------------------------------

Here is my rephrasing of the âice creamâ example, presented in the Decomplexify video on database normalization:

> â*There are several ice cream brands on the market, e.g. âFrostyâsâ, âAlpineâ, âIce Queenâ, etc. Each brand produces one or more flavours of ice cream, e.g. vanilla, strawberry, and rum raisin. We want to create a database of our friendsâ ice cream preferences. Each friend likes some brands, and also some flavours. We assume that those preferences intersect: that is, if a friend likes brands A and B and flavours 1 and 2 that means that they like exactly A-1, A-2, B-1, and B-2 (restricted to pairs the brand actually produces). They wonât like A-3 or C-1.*â

Two things to note: first, this example is more plausible than Wikipediaâs one, we’ll take it. Second, there is no requirement to handle specific tastes. For example, we donât record the fact that the aforementioned friend likes D-4 additionally, nor the fact that they donât like B-1.

Letâs write down the logical model that corresponds to the description above, using notation from âDatabase Design Bookâ. Weâll have three anchors (entities):

| Anchor | ID example | Table name |
| --- | --- | --- |
| **Brand** | *âAlpineâ* | `brands` |
| **Flavour** | *âvanillaâ* | `flavours` |
| **Friend** | *âJasonâ* | `friends` |

In the real database weâd use proper integer IDs, but this one is a tiny teaching database, so it makes sense to use so-called natural keys which are unique strings. We assume that all your friends have different names. In the textbook table design strategy, each anchor has a corresponding table. The table names are written in the last column.

We donât need any attributes here, because all information about entities is basically contained in the ID.

But the most interesting part is the list of links. 5NF is mostly about the links.

| Anchor1 : Anchor2 | Cardi- nality | Sentences | Table or column names |
| --- | --- | --- | --- |
| **Brand** : **Flavour** | M:N | A Brand produces *several* Flavours  A Flavour is produced by *several* Brands | `brand_flavours` |
| **Friend** : **Brand** | M:N | A Friend prefers *several* Brands  A Brand is preferred by *several* Friends | `friend_brands` |
| **Friend** : **Flavour** | M:N | A Friend prefers *several* Flavours  A Flavour is preferred by *several* Friends | `friend_flavours` |

A link is a relationship between two anchors. Here we have three links, connecting three anchors into a triangle, as we mentioned:

![Brand / Flavour / Friend anchors](https://kb.databasedesignbook.com/posts/5nf/5nf-ice-cream-example.png)

All three links have M:N cardinality. It is clearly visible because all the sentences contain the word â*several*â. In the textbook table design strategy, each M:N link has a corresponding two-column table (also known as junction table). The names of the tables are written down in the last column.

Here are three link tables, created based on the logical model. It uses the same dataset as presented in the Decomplexify video.

![Dataset: brand_flavours, friend_brands, friend_flavours](https://kb.databasedesignbook.com/posts/5nf/icecream-dataset-links.png)

One thing that we can see here is that Jason likes chocolate, but none of the brands produce it.

A useful exercise for the interested reader would be to write an SQL query that returns the brand offerings that would suit each friend, based on their preferences.

Note that there would exists three more tables: `brands`, `flavours`, and `friends`, containing IDs used in the link tables.

![Dataset: brands, flavours, friends](https://kb.databasedesignbook.com/posts/5nf/icecream-dataset-anchors.png)

Note that for each entity there is one more row that is not present in any of the link relationships. We know about the Coldflash brand, but we donât know which flavours it provides, and nobody prefers it. We have a Kiwi flavour which is not produced by any brand and not preferred by anyone. And we have Suzy, whose preferences we have not yet registered.

ABC+D star pattern: the âmusiciansâ example
-----------------------------------------------

Now letâs discuss an example from the â[5NF: The Missing Use Case](https://datademythed.com/posts/5nf_missing_use_case/)â post by Barry Johnson.

Suppose that we want to record information about concerts and musicians that played certain instruments in those concerts. We begin with the three anchors:

| Anchor | ID example | Table name |
| --- | --- | --- |
| **Concert** | *âchristmas-2025â* | `concerts` |
| **Instrument** | *âviolinâ* | `instruments` |
| **Musician** | *âPatriciaâ* | `musicians` |

Now letâs draft some possible links. This is one of the database modeling examples where natural language may mislead you, so we need to be careful and precise.

In plain English weâd say: â*A Musician played an Instrument in a Concert*â, but this sentence includes three anchors and not two. **Links always connect two anchors**. Even though the relational model allows relations with more than two elements, we insist on only using 2-element links because **they help you design unambiguous tables**.

Here is an example from a real-world concert, listing musicians and their instruments:

* *Marc, violin;*
* *Gilles, violin;*
* *Vlad, viola;*
* *Yovan, cello.*

You see that several musicians can play an instrument. If you think about it, itâs possible that one musician could play several instruments.

While weâre at it, why are we even building this database? Suppose that we want to track how much money musicians should get paid. Violin players get paid $x; maybe somebody was asked to help out and play some cymbals in the first half and a gong at the end, so theyâd be paid $y + $z.

When you see a list of something, very often it would be an anchor. List items **could be counted**, and you can **add one more** item to the list: a classic anchor.

We need to find a word for this â letâs try âPerformanceâ:

| Anchor | ID example | Table name |
| --- | --- | --- |
| **Performance** | *<two options possible, see below>* | performances |

Finding words like this is often hard, because natural language is ambiguous.

(Note that we use a synthetic integer ID for the performances.)

Letâs try to find links between the four anchors now. A concert is made of individual performances. A performance involves a specific musician playing a specific instrument. Letâs formalize this:

| Anchor1 : Anchor2 | Cardi- nality | Sentences | Table or column names |
| --- | --- | --- | --- |
| **Concert** : **Performance** | 1:N | A Concert consists of *several* Performances  A Performance is a part of *only one* Concert | `performances.` `concert_id` |
| **Instrument : Performance** | 1:N | An Instrument is played in *several* Performances   A Performance involves *only one* Instrument | `performances.` `instrument_id` |
| **Musician : Performance** | 1:N | A Musician may perform *several* Performances   A Performance is performed by *only one* Musician | `performances.` `musician_id` |

Read the sentences: they may sound a bit awkward, but you need to confirm that they make sense. Itâs crucial to make sure that â*only one*â and â*several*â is used correctly, because thatâs how you define cardinality. Read aloud if needed, or read to somebody else â thatâs how you prevent design mistakes.

In this case, all three links have cardinality 1:N.

Here is a diagram that has a distinctive three-pointed star shape:

![Concert, Musician, Instrument, Performance: anchors and links](https://kb.databasedesignbook.com/posts/5nf/5nf-musicians-diagram-3star.jpg)

This is why we call it the **ABC+D star pattern**. We have three âeasyâ words: concert, musician, and instrument. But you must also realize that there is an underlying concept of performance. Using a formalized approach, such as the one presented in the [âDatabase Design Bookâ](https://databasedesignbook.com/), helps a lot, making the design process more reliable and error-proof.

### Physical table design: primary keys

The concept of normal forms only appears when we talk about physical table design. The ice cream example was simple and straightforward, but the current scenario is a bit more complicated, because we have to talk about uniqueness constraints.

Textbook table design strategy could be applied directly:

* Performance anchor is implemented as â`performances`â table;
* All three links are 1:N, so they are implemented as columns in that table (â`concert_id`â, â`musician_id`â, and â`instrument_id`â).

But here is the question: what would be the primary key of that table? In most anchor tables weâd use a synthetic ID column, but here we can notice that the combination of (`concert_id`, `musician_id`, `instrument_id`) must be unique. In awkward semi-formalized English: a musician is paid for performing an instrument **only once** for a given concert (this follows from business requirements).

If we use a synthetic ID column, we need to add a uniqueness constraint:

```
CREATE TABLE performances (  
  id INTEGER NOT NULL PRIMARY KEY,  
  concert_id INTEGER NOT NULL,  
  musician_id INTEGER NOT NULL,  
  instrument_id INTEGER NOT NULL,  
  UNIQUE (concert_id, musician_id, instrument_id)  
);
```

The data looks like this:  
![performances table, using synthetic ID primary key](https://kb.databasedesignbook.com/posts/5nf/performances-dataset-with-id.png)

But what the relational theory textbooks want you to know is that you can also design this table by using a composite primary key (which also serves as a uniqueness constraint):

```
CREATE TABLE performances (  
  concert_id INTEGER NOT NULL,  
  musician_id INTEGER NOT NULL,  
  instrument_id INTEGER NOT NULL,  
  PRIMARY KEY (concert_id, musician_id, instrument_id)  
);
```

And the data will look like this:  
![performances table, using composite primary key](https://kb.databasedesignbook.com/posts/5nf/performances-dataset-composite.png)

The choice of composite vs synthetic primary key only appears when business requirements assume uniqueness. In other scenarios there is no uniqueness, and you must use the synthetic primary key.

> Imagine an online game where users can buy certain items and give them as gifts to other users. The same user can give the same type of item to the same friend multiple times, so there is no uniqueness. Weâd still have the same ABC+D star pattern, though.

Letâs go back to the three-column table variant. Itâs the same structure as was used in Wikipedia and in many other textbooks and tutorials. We did not need to split it into three two-column tables because the business requirements are different from the âice creamâ example.

More importantly, **we did not need to reason in terms of 5NF decomposition at all.** We only needed to define business requirements, and construct the physical tables in a straightforward way.

Yet, weâve seen both types of tables that are discussed in a typical 5NF tutorial:

* three two-column tables (**AB-BC-AC triangle**);
* one table (**ABC+D star**):
  + three-column if uniqueness is required and we want a composite PK;
  + one extra ID if there is no uniqueness or we want a synthetic PK;

Also, we did not need to perform this illogical operation of âsplitting tablesâ, because we just designed all the tables correctly from the beginning. In practice they would not be split or joined as part of the database design process.

Both presented patterns are not mutually exclusive. You can have several different links that connect the same anchors in a different way.

Letâs go back to the ice cream example and extend it. Some of our friends are extra picky: they prefer specific flavours from a specific brand, for example kiwi by Coldflash, but no other flavours by Coldflash, and no other kiwi brands.

We need to handle this example by *extending* the logical model defined above. Itâs important to note that the original behavior stays as it is: all the logical schema and existing tables stay as they are. We only add new entries to the logical schema, and weâll add some new tables.

Having discussed the âmusiciansâ example, we can immediately recognize how to model â*Frank loves Coldflash kiwi*â. We introduce a new anchor called Preference, and three links arranged as an ABC+D star pattern.

Logical schema is basically a copy-paste of the âmusiciansâ example. Anchors:

| Anchor | ID example | Table name |
| --- | --- | --- |
| **Preference** | *<two options are possible>* | `preferences` |

And links:

| Anchor1 : Anchor2 | Cardi- nality | Sentences | Table or column names |
| --- | --- | --- | --- |
| **Friend** : **Preference** | 1:N | A Friend can have *several* Preferences  A Preference belongs to *only one* Friend | `preferences.` `friend_id` |
| **Brand : Preference** | 1:N | A Brand is involved in *several* Preferences   A Preference refers to *only one* Brand | `preferences.` `brand_id` |
| **Flavour : Preference** | 1:N | A Flavour is involved in *several* Preferences   A Preference refers to *only one* Flavour | `preferences.` `flavour_id` |

Same as with âmusiciansâ example, we have the option of synthetic ID or a composite PK. In this example each (*Friend*, *Brand*, *Flavour*) combination must be unique, so we can use a composite PK if we want.

From those new elements we create a new â`preferences`â table, that exists alongside the three other tables: â`brand_flavours`â, â`friend_brands`â, and â`friend_flavours`â. We still capture both the information about broader preferences and about specific preferences, using two sets of tables, designed accordingly.

The point of this section is to reinforce the idea that both patterns are equally useful, one is not a replacement for the other. Sometimes they could even be used simultaneously. Which of them is applicable depends only on your business requirements.

Letâs go back to the âmusiciansâ example. If you read the â[5NF: The Missing Use Case](https://datademythed.com/posts/5nf_missing_use_case/)â post, youâll see that at some point an idea of âskillâ is introduced. Basically itâs a link that connects a Musician and an Instrument. This idea makes sense in natural language: â*Alice can play violin, so she gets invited to play in the classical concerts*â.

The data is modeled via this Skill in the text like this:

![Concert / Musician / Instrument / Performance, including Skill](https://kb.databasedesignbook.com/posts/5nf/skill-diagram.png)

This differs from the model discussed in this post. Why? Iâve been thinking about this exact issue for quite some time, and came to look at the problem from a different angle.

I think that â*A Musician can play an Instrument*â is a valid link, but it corresponds to a different business process. We discussed capturing the information about who played which instrument in specific concerts.

But if you think about that, itâs possible to play an instrument in the concert without necessarily declaring that you have a skill to play it.

Consider the quote from that post:

> “Looking at our example a bit further, for instance, itâs easy to conceive of a SkillRating in [Skill]. This could be used to help decide which [Musician] instance(s), with corresponding [Instrument] instance(s), **will be invited** to be part of a [Concert] instance.”

It makes total sense to extend our original logical model by capturing the information about which musicians are willing to be invited to the concerts to play certain instruments. Here is the link:

| Anchor1 : Anchor2 | Cardi- nality | Sentences | Table or column names |
| --- | --- | --- | --- |
| **Instrument : Musician** | M:N | An Instrument can be played by *several* Musicians   A Musician can play *several* Instruments | `musician_skills` |

Note that this link has M:N cardinality. Because of that, we had to add another two-column table (also known as a junction table). It is completely independent from the âperformancesâ table, in both ways.

First, we can record that Alice can play violin, but we donât have any records about her playing anything. This is normal: maybe she just started, or our own dataset is far from complete.

Second, somebody can play in a concert, but they do not necessarily want to be invited to further concerts. Maybe theyâve retired and are only doing exceptions for special occasions.

Or, somebody needs to play hammer in Mahlerâs Symphony No. 6 (there are only two or three blows in the entire piece). Itâs probably not necessary to have a âskillâ for that, but you certainly want to be mentioned in the lineup because itâs such an important part.

So, itâs a question of what you want to implement. Is it a sort of marketplace for musicians? Then you need â`musician_skills`â. Or, if you want to have a record of who played when â thatâs what â`performances`â table is for. Maybe you want both. Itâs up to you to decide.

Additional reading
------------------

Here are three more texts that may be useful if you want to understand more about the history of normal forms.

1. **William Kent â[A Simple Guide to Five Normal Forms in Relational Database Theory](https://www.bkent.net/Doc/simple5.htm)â (1982)**

5NF is discussed in chapter 4.2. We already used this text to better understand historical aspects of 4NF definition. There is a confusing sentence there:

> “Roughly speaking, we may say that ***a record type is in fifth normal form when its information content cannot be reconstructed from several smaller record types***, i.e., from record types each having fewer fields than the original record.”

It seems that there are too many negatives here, and itâs hard to follow. But I wonât attempt to edit this sentence: my goal is to present a completely different way of reaching the same result.

2. **Andrei Pall â[Database Normalization](https://andreipall.github.io/sql/database-normalization/)â (2020)**

This post contains a beautiful table that shows the full range of normal forms (including non-numerical ones), explaining which specific criteria motivated each of them.

3. **Hugh Darwen âAn Introduction to Relational Database Theoryâ (2010)**

The book is freely downloadable. On page 11 you can find âNote to Teachersâ which alone is hugely enlightening. It says that 4NF is just a simple special case of 5NF, which is a useful piece of spiritual guidance.

Another quote:

> â*Also in Chapter 7, [I have aimed] to study the normal forms in reverse order to that in which they are normally presented. I put 6NF first because it is the simplest and also the most extreme. More important to me was to deal with 5NF and join dependencies before BCNF and functional dependencies (though I do leave to the end discussion of those pathological cases where BCNF is satisfied but not 5NF).*â

This was a big confirmation that my own approach to teaching normal forms is plausible â I also think that 6NF is the foundational form.

5NF is presented in Section 7.4 (page 185), using the â*Wives of Henry VIII*â example. This is not a very good example because it is rather misaligned with the typical real-world scenarios. Nevertheless, the book, as well as other materials by Darwen, is a treasure.

---

“Database Design Book” (2025)
-----------------------------

[![](https://kb.databasedesignbook.com/posts/book-cover.jpg)](https://databasedesignbook.com/)

#### Learn how to get from business requirements to a database schema

If this post was useful, you may find this book useful too.

[Table of contents and sample chapters](https://databasedesignbook.com/)

Book length: 145 pages, ~32.000 words. Available in both PDF and in EPUB format.

[Purchase for â¬32](https://databasedesignbook.com/)

---

Conclusion
----------

Traditionally 5NF is presented with an unmotivated example of a 3-column table. This table is then âsplitâ into three 2-column tables. The splitting operation is not very well motivated and does not happen in practice.

This makes 5NF harder to understand and encourages the air of mysticism around the higher normal forms.

We propose a more straightforward way, better aligned with the practice of database design. We start from the business requirements and logical schema. Based on that, two patterns of physical table design follow naturally: AB-BC-AC triangle, or an ABC+D star pattern. Both patterns, when designed this way, are fully normalized: there are no anomalies and no redundancy.

I’d be happy to hear your feedback:  
Alexey Makhotkin
[squadette@gmail.com](mailto:squadette@gmail.com).