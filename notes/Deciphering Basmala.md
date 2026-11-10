---
title: "Deciphering Basmala"
url: https://blog.plover.com/lang/bismillah.html
clipped: 2026-08-31 13:52:12
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Deciphering Basmala](https://blog.plover.com/lang/bismillah.html)

## Digest Summary
The article discusses challenges of Arabic typography, emphasizing that Arabic script is inherently cursive and relies on contextual ligatures to render correctly. Early font engines lacked proper ligature handling, producing disjointed glyphs that broke the visual flow of words such as “hello, world, this is Arabic text.” A critical example is the basmala—“bismillāh al‑raḥmān al‑raḥīm”—which appears at the start of every Qur’an surah except the ninth. Rendering the basmala as separate letters yields an unacceptable jumble, so Unicode introduced a dedicated code point (U+FDFD ARABIC LIGATURE BISMILLAH AR‑RAHMAN AR‑RAHEEM) that maps to a single, correctly shaped glyph. The article notes platform inconsistencies: the glyph appears long and narrow in Firefox on desktop but differently on Android. It also breaks down the four component words, explains the assimilation of the definite article “al‑” before /r/, and cites typographic critiques of the Android design, particularly the fused letter connections.

---

## Full Article

# 
[The Universe of Discourse](https://blog.plover.com/)

  
  

   

   
   Mark Dominus (陶敏修)
   [mjd@pobox.com](mailto:mjd@pobox.com) 
   

   

   
   

   

   [About me](https://blog.plover.com/meta/about-me.html)
   

   

   [RSS](https://blog.plover.com/index.rss)
   [Atom](https://blog.plover.com/index.atom)   

   

[12 recent entries](https://blog.plover.com/)
  
    
- [The road to epsilon-zero: Productive programs and well-founded orders](https://blog.plover.com/math/ordinals/05-shortlex.html)

- [There are two kinds of theorems](https://blog.plover.com/math/two-kinds-of-theorems.html)

- [The road to epsilon-zero: Coin-moving games with no coins](https://blog.plover.com/math/ordinals/04-coordinates.html)

- [Seven books I keep close because I love them](https://blog.plover.com/book/elbow-shelf.html)

- [The road to epsilon-zero: Infinite Nim as a coin-moving game](https://blog.plover.com/math/ordinals/03-track-tokens.html)

- [âSteph Curry: fluke or breakthroughâ ten years later](https://blog.plover.com/games/sport-flukes-followup.html)

- [The road to epsilon-zero: Nim always ends, even with infinite ordinals](https://blog.plover.com/math/ordinals/02-wellfoundedness.html)

- [The road to epsilon-zero: ordinals as nim-heaps](https://blog.plover.com/math/ordinals/01-nim.html)

- [Starting to understand epsilon-zero](https://blog.plover.com/math/epsilon-zero.html)

- [It's our language now!](https://blog.plover.com/lang/who-owns-english.html)

- [I owe my life to a 1913 road rage incident](https://blog.plover.com/history/andor.html)

- [Deciphering basmala](https://blog.plover.com/lang/bismillah.html)

  

   

Archive:
[2026](https://blog.plover.com/2026/):
    [J](https://blog.plover.com/2026/01/)[F](https://blog.plover.com/2026/02/)[M](https://blog.plover.com/2026/03/)AM[J](https://blog.plover.com/2026/06/)
 [J](https://blog.plover.com/2026/07/)[A](https://blog.plover.com/2026/08/)
[2025](https://blog.plover.com/2025/):
    J[F](https://blog.plover.com/2025/02/)[M](https://blog.plover.com/2025/03/)[A](https://blog.plover.com/2025/04/)[M](https://blog.plover.com/2025/05/)J
 JA[S](https://blog.plover.com/2025/09/)OND
[2024](https://blog.plover.com/2024/):
    J[F](https://blog.plover.com/2024/02/)[M](https://blog.plover.com/2024/03/)[A](https://blog.plover.com/2024/04/)[M](https://blog.plover.com/2024/05/)[J](https://blog.plover.com/2024/06/)
 [J](https://blog.plover.com/2024/07/)[A](https://blog.plover.com/2024/08/)SO[N](https://blog.plover.com/2024/11/)D
[2023](https://blog.plover.com/2023/):
    J[F](https://blog.plover.com/2023/02/)[M](https://blog.plover.com/2023/03/)[A](https://blog.plover.com/2023/04/)[M](https://blog.plover.com/2023/05/)[J](https://blog.plover.com/2023/06/)
 [J](https://blog.plover.com/2023/07/)[A](https://blog.plover.com/2023/08/)[S](https://blog.plover.com/2023/09/)[O](https://blog.plover.com/2023/10/)[N](https://blog.plover.com/2023/11/)[D](https://blog.plover.com/2023/12/)
[2022](https://blog.plover.com/2022/):
    [J](https://blog.plover.com/2022/01/)[F](https://blog.plover.com/2022/02/)[M](https://blog.plover.com/2022/03/)[A](https://blog.plover.com/2022/04/)[M](https://blog.plover.com/2022/05/)[J](https://blog.plover.com/2022/06/)
 [J](https://blog.plover.com/2022/07/)A[S](https://blog.plover.com/2022/09/)[O](https://blog.plover.com/2022/10/)[N](https://blog.plover.com/2022/11/)[D](https://blog.plover.com/2022/12/)
[2021](https://blog.plover.com/2021/):
    [J](https://blog.plover.com/2021/01/)[F](https://blog.plover.com/2021/02/)[M](https://blog.plover.com/2021/03/)[A](https://blog.plover.com/2021/04/)M[J](https://blog.plover.com/2021/05/)
 [J](https://blog.plover.com/2021/07/)[A](https://blog.plover.com/2021/08/)[S](https://blog.plover.com/2021/09/)[O](https://blog.plover.com/2021/10/)[N](https://blog.plover.com/2021/11/)[D](https://blog.plover.com/2021/12/)
[2020](https://blog.plover.com/2020/):
    [J](https://blog.plover.com/2020/01/)[F](https://blog.plover.com/2020/02/)[M](https://blog.plover.com/2020/03/)[A](https://blog.plover.com/2020/04/)[M](https://blog.plover.com/2020/05/)[J](https://blog.plover.com/2020/06/)
 [J](https://blog.plover.com/2020/07/)[A](https://blog.plover.com/2020/08/)[S](https://blog.plover.com/2020/09/)[O](https://blog.plover.com/2020/10/)[N](https://blog.plover.com/2020/11/)[D](https://blog.plover.com/2020/12/)
[2019](https://blog.plover.com/2019/):
[J](https://blog.plover.com/2019/01/)F[M](https://blog.plover.com/2019/03/)[A](https://blog.plover.com/2019/04/)[M](https://blog.plover.com/2019/05/)[J](https://blog.plover.com/2019/06/)
 [J](https://blog.plover.com/2019/07/)[A](https://blog.plover.com/2019/08/)[S](https://blog.plover.com/2019/09/)[O](https://blog.plover.com/2019/10/)[N](https://blog.plover.com/2019/11/)[D](https://blog.plover.com/2019/12/)
[2018](https://blog.plover.com/2018/):
[J](https://blog.plover.com/2018/01/)[F](https://blog.plover.com/2018/02/)[M](https://blog.plover.com/2018/03/)[A](https://blog.plover.com/2018/04/)[M](https://blog.plover.com/2018/05/)[J](https://blog.plover.com/2018/06/)
 [J](https://blog.plover.com/2018/07/)[A](https://blog.plover.com/2018/08/)[S](https://blog.plover.com/2018/09/)[O](https://blog.plover.com/2018/10/)[N](https://blog.plover.com/2018/11/)[D](https://blog.plover.com/2018/12/)
[2017](https://blog.plover.com/2017/):
[J](https://blog.plover.com/2017/01/)[F](https://blog.plover.com/2017/02/)[M](https://blog.plover.com/2017/03/)[A](https://blog.plover.com/2017/04/)[M](https://blog.plover.com/2017/05/)[J](https://blog.plover.com/2017/06/)
 [J](https://blog.plover.com/2017/07/)[A](https://blog.plover.com/2017/08/)[S](https://blog.plover.com/2017/09/)[O](https://blog.plover.com/2017/10/)[N](https://blog.plover.com/2017/11/)[D](https://blog.plover.com/2017/12/)
[2016](https://blog.plover.com/2016/):
J[F](https://blog.plover.com/2016/02/)[M](https://blog.plover.com/2016/03/)[A](https://blog.plover.com/2016/04/)[M](https://blog.plover.com/2016/05/)[J](https://blog.plover.com/2016/06/)
 [J](https://blog.plover.com/2016/07/)ASO[N](https://blog.plover.com/2016/11/)[D](https://blog.plover.com/2016/12/)
[2015](https://blog.plover.com/2015/):
JF[M](https://blog.plover.com/2015/03/)[A](https://blog.plover.com/2015/04/)[M](https://blog.plover.com/2015/05/)[J](https://blog.plover.com/2015/06/) [J](https://blog.plover.com/2015/07/)[A](https://blog.plover.com/2015/08/)[S](https://blog.plover.com/2015/09/)[O](https://blog.plover.com/2015/10/)[N](https://blog.plover.com/2015/11/)[D](https://blog.plover.com/2015/12/)
[2014](https://blog.plover.com/2014/):
[J](https://blog.plover.com/2014/01/)[F](https://blog.plover.com/2014/02/)[M](https://blog.plover.com/2014/03/)[A](https://blog.plover.com/2014/04/)MJ [J](https://blog.plover.com/2014/07/)ASO[N](https://blog.plover.com/2014/11/)[D](https://blog.plover.com/2014/12/)
[2013](https://blog.plover.com/2013/):
JFMAMJ [J](https://blog.plover.com/2013/07/)A[S](https://blog.plover.com/2013/09/)[O](https://blog.plover.com/2013/10/)N[D](https://blog.plover.com/2013/12/)
[2012](https://blog.plover.com/2012/):
[J](https://blog.plover.com/2012/01/)[F](https://blog.plover.com/2012/02/)[M](https://blog.plover.com/2012/03/)AMJ
 J[A](https://blog.plover.com/2012/08/)SON[D](https://blog.plover.com/2012/12/)
[2011](https://blog.plover.com/2011/):
JFMA[M](https://blog.plover.com/2011/05/)[J](https://blog.plover.com/2011/06/)
 JASO[N](https://blog.plover.com/2011/11/)D
[2010](https://blog.plover.com/2010/):
[J](https://blog.plover.com/2010/01/)FMAMJ
 J[A](https://blog.plover.com/2010/08/)[S](https://blog.plover.com/2010/09/)[O](https://blog.plover.com/2010/10/)[N](https://blog.plover.com/2010/11/)D
[2009](https://blog.plover.com/2009/):
[J](https://blog.plover.com/2009/01/)[F](https://blog.plover.com/2009/02/)[M](https://blog.plover.com/2009/03/)A[M](https://blog.plover.com/2009/05/)[J](https://blog.plover.com/2009/06/)
 [J](https://blog.plover.com/2009/07/)A[S](https://blog.plover.com/2009/09/)ON[D](https://blog.plover.com/2009/12/)
[2008](https://blog.plover.com/2008/):
[J](https://blog.plover.com/2008/01/)[F](https://blog.plover.com/2008/02/)[M](https://blog.plover.com/2008/03/)[A](https://blog.plover.com/2008/04/)[M](https://blog.plover.com/2008/05/)[J](https://blog.plover.com/2008/06/)
 [J](https://blog.plover.com/2008/07/)A[S](https://blog.plover.com/2008/09/)[O](https://blog.plover.com/2008/10/)[N](https://blog.plover.com/2008/11/)D
[2007](https://blog.plover.com/2007/):
[J](https://blog.plover.com/2007/01/)[F](https://blog.plover.com/2007/02/)[M](https://blog.plover.com/2007/03/)[A](https://blog.plover.com/2007/04/)[M](https://blog.plover.com/2007/05/)[J](https://blog.plover.com/2007/06/)
 [J](https://blog.plover.com/2007/07/)[A](https://blog.plover.com/2007/08/)[S](https://blog.plover.com/2007/09/)[O](https://blog.plover.com/2007/10/)[N](https://blog.plover.com/2007/11/)[D](https://blog.plover.com/2007/12/)
[2006](https://blog.plover.com/2006/):
[J](https://blog.plover.com/2006/01/)[F](https://blog.plover.com/2006/02/)[M](https://blog.plover.com/2006/03/)[A](https://blog.plover.com/2006/04/)[M](https://blog.plover.com/2006/05/)[J](https://blog.plover.com/2006/06/)
  [J](https://blog.plover.com/2006/07/)A[S](https://blog.plover.com/2006/09/)[O](https://blog.plover.com/2006/10/)[N](https://blog.plover.com/2006/11/)[D](https://blog.plover.com/2006/12/)
[2005](https://blog.plover.com/2005/): [O](https://blog.plover.com/2005/10/)[N](https://blog.plover.com/2005/11/)[D](https://blog.plover.com/2005/12/)

Subtopics:

[Mathematics](https://blog.plover.com/math/)252
[Programming](https://blog.plover.com/prog/)102
[Language](https://blog.plover.com/lang/)98
[Miscellaneous](https://blog.plover.com/misc/)75
[Book](https://blog.plover.com/book/)51
[Tech](https://blog.plover.com/tech/)49
[Etymology](https://blog.plover.com/lang/etym/)36
[Haskell](https://blog.plover.com/prog/haskell/)33
[Oops](https://blog.plover.com/oops/)30
[Unix](https://blog.plover.com/Unix/)27
[Cosmic Call](https://blog.plover.com/aliens/dd/)25
[Math SE](https://blog.plover.com/math/se/)25
[Law](https://blog.plover.com/law/)23
[Physics](https://blog.plover.com/physics/)21
[Perl](https://blog.plover.com/prog/perl/)17
[Biology](https://blog.plover.com/bio/)16
[Brain](https://blog.plover.com/brain/)15
[Calendar](https://blog.plover.com/calendar/)15
[Food](https://blog.plover.com/food/)15

   

   
   
   
   

  

Comments disabled
  

  
  

   
Tue, 23 Jun 2026

[Deciphering basmala](https://blog.plover.com/lang/bismillah.html)

Making the rounds last week was this magnificent article on the
complications of Arabic typesetting,
[An interactive introduction to the terrific experience of rendering Arabic typography and its technical debt](https://lr0.org/blog/p/arabic/).
The author, Saleh, promises:

  

The reply took and the closure of the ticket took half an hour or
  so. The reasons behind it took five hundred years to pile up, and
  they involve a twice-mutilated vizier, a QurÊ¾Än that vanished for
  four centuries, a Beirut newspaperman with a deadline, and an
  Egyptian physician who taught himself font engineering for fun (or
  that what I imagine about him). Walking through these, ended up to
  be the most enjoyable couple of weeks in that job, and I want to go
  through it here too.

And then wow, does it deliver.  Don't read my article, go read Saleh's
instead, or at least read it first.

Still here?  Then a disclaimer: I do not know Arabic, not
even all the letters, yet.  I tried hard to get the details right
in this article, but I expect there are misspellings, misstatements of
fact, and so on, for which I apologize in advance.

In one of my favorite parts of his article,
Saleh discusses how, because Arabic script is always cursive, it is
important how the
letters are joined to one another. Modern Latin script has only a
few ligatures, and omitting them is barely noticeable:

But in Arabic, the ligatures are important. The text looks grossly wrong without
the correct ligatures.

Early font engines couldn't render Arabic ligatures properly, and
on-screen Arabic text always came out looking ridiculous, with the
letters separate like Latin script letters, which is completely wrong
for Arabic.  Saleh gives this example,
which says âhello, world, this is Arabic textâ.  It should look like
this:

ÙØ±Ø­Ø¨Ø§ Ø¨Ø§ÙØ¹Ø§ÙÙØ ÙØ°Ø§ ÙØµ Ø¹Ø±Ø¨Ù

But early font renderers rendered it like this:

ÙâØ±âØ­âØ¨âØ§â âØ¨âØ§âÙâØ¹âØ§âÙâÙâØâ âÙâØ°âØ§â âÙâØµâ âØ¹âØ±âØ¨âÙ

The crappy rendering was unfortunate, and only barely tolerable,  just
barely better than nothing.  Even if you don't read Arabic (I don't)
you can see the differences.  Notice, for example how the elegant and
symmetric cluster ÙØ¹Ø§ is mangled to ÙâØ¹âØ§.  Or look at just the first
(rightmost) letter.  It is the Arabic letter âmâ, called mÄ«m.  It is
supposed to connect with the letter next to
it, and not to have that hanging tail, which only appears when mÄ«m
is written by itself, or at the end of a word.

For the supremely important phrase 

Ø¨ÙØ³ÙÙÙ Ù±ÙÙÙÙ Ù±ÙØ±ÙÙØ­ÙÙÙÙ°ÙÙ Ù±ÙØ±ÙÙØ­ÙÙÙÙÙ

the crappy rendering was not tolerable.  This phrase is âbismillah al-raá¸¥man
al-raá¸¥imâ.  It means âin the name of God, the gracious, the mercifulâ,
and it appears at the start of each of the 114 surahs (chapters) of
the Qur'an (except the ninth for some reason).  There is a
centuries-long tradition of calligraphic expression of this phrase,
in
the most perfect possible ways.

âKhalili Collection Islamic Art cal 0154",
Ottoman Turkish, 19th century.  Public domain, via
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Khalili_Collection_Islamic_Art_cal_0154.jpg).

It would be blasphemous to render this phrase, called the âbasmalaâ, this
crucial expression of honor for God, as a jumble of letters.  Imagine
if Exodus 20 had had God introducing the Ten Commandments by saying

The incredible solution to this one problem was the inclusion in
Unicode of a special codepoint U+FDFD  `ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM` .
As a single codepoint, the basmala could be assigned a single glyph, and the
single glyph could be designed correctly, so as not to look like
trash.
Here it is.  Remember, this is a single character:

ï·½

In Firefox, with my fonts, the glyph renders like this, long and narrow:

but on my Android phone there is a very different glyph.  Here it is, highly magnified:

What's going on here?  It's fun to find out.

The basmala actually has four words (âbismillahâ is a contraction):

- Bismi (Ø¨Ø³Ù, âin the name ofâ)

- Allah (Ø§ÙÙÙÙ°Ù, âGodâ)

- al-raá¸¥man (Ø§ÙØ±Ø­ÙÙ, âthe graciousâ)

- al-raá¸¥im (Ø§ÙØ±Ø­ÙÙ, âthe mercifulâ)

(At some  point I should slip in that when the word âal-â (which means
âtheâ) appears before an /r/ sound, its /l/ is assimilated, so that it
is pronounced like /ar-/.  This is analogous to what happens when the
English prefix âin-â is attached to a word like
ârelevantâ. âInrelevantâ is tricky to say, so the /n/ is assimilated
and the word is spelled and pronounced âirrelevantâ.)

Here are the four words picked out in different colors.  To a person
literate in Arabic, I suppose this is obvious, but I found it a bit challenging.

âAllahâ Ø§ÙÙÙ is at the top.
(I'm told this is traditional.)  I've colored it green because green is
said to have been Muhammad's favorite color.

The two marks above it, the W-shaped mark and the vertical stroke
above it, are diacritic marks (one called a [shaddah](https://en.wikipedia.org/wiki/shaddah) and
other other indicating the vowel).  I'm not sure how optional they
are, but in an earlier draft of this article
I tried to explain them in detail and got bogged down in a multi-paragraph
digression about the morphology of the word âAllahâ, so I'm just going to
move on without commenting on them further.

Below âAllahâ, in red, is âbismiâ.  In Arabic this has three letters,
/b/Â + /s/Â + /m/, since the vowels are omitted.  At the right we have
 Ø¨Ø³ which is /b/Â + /s/; the letters
are named bÄ' and sÄ«n.  Then
there's a horizontal stroke, called a [kashida](https://en.wikipedia.org/wiki/kashida), under
âAllahâ; this is just for layout, analogous to white space, and is not pronounced. Finally the Ù (/m/, called mÄ«m) over on the left.  MÄ«m Ù has a long
tail when it appears at the end of a word, as here, and the designer has
decided to attach the tail to the Ù (/n/, nÅ«n) at the end of al-raá¸¥man.  You can see
the same final Ù mÄ«m and its tail at
the end of the purple word al-raá¸¥im, and in the middle of the blue
word al-raá¸¥man without the tail.

([Khaled Hosny](https://khaledhosny.com/), designer of the widely used [Amiri](https://en.wikipedia.org/wiki/Amiri_%28typeface%29) font, [told
me that the design
of the Android basmala glyph is very bad](https://typo.social/@khaled/116752857475379426). One of his criticisms was âthe bizarre fusion of
the lettersâ and I suppose the attachment of the Ù and the Ù is one
of the things he had in mind.  He also objected to the insertion of
âAllahâ into the middle of âbismiâ.)

The third word, in blue, is al-raá¸¥man 
Ø§ÙØ±Ø­ÙÙ which as you can see
starts with the same letters as
al-raá¸¥im
Ø§ÙØ±Ø­ÙÙ.  You can also see the
same first  two of those letters at the start of âAllahâ Ø§ÙÙÙ.  As I mentioned before, âal-â
means âtheâ, so you see it at the beginning of many Arabic words.
It also survives in many English words that are descended from Arabic,
such as alcohol, alcove, algebra, algorithms, and alchemy.

(Not, however, âalligatorâ,
where the âal-â is the Spanish word for âtheâ.)

The /r/ sound in al-raá¸¥man and al-raá¸¥im is made by the letter rÄ',
which is written as the down-hanging
hook to the left of the Ø§Ù, as here: Ø§ÙØ±.  The designer has connected the
hook of the blue rÄ' with the upper part of a purple letter called á¸¥Ä'.  (I
suppose Hosny also dislikes this.)  When written by itself á¸¥Ä looks like
this: Ø­  but when it's in the middle of a word it loses its fancy
tail.  The á¸¥Ä is of course the common á¸¥ in both al-raá¸¥man and al-raá¸¥im.

Let's see, what else?  The only letter I haven't mentioned is the
fifth letter in al-raá¸¥im Ø§ÙØ±Ø­ÙÙ,
just before the mÄ«m and its tail, called yÄ'. When by itself, it
is written Ù, but in the middle of a word like al-raá¸¥im, it is the 
upward-pointing spike with two dots below.

Arabic writing is very beautiful, isn't it?  Last time I tried to
learn the alphabet I got stuck because I was trying to learn the
sounds at the same time, and Arabic sounds are very different from
English sounds.  Arabic has three sounds that resemble English /h/.
One is very soft, one is very rough, and one is in between.  á¸¤Ä' Ø­
is the in-between one, represented in English as âá¸¥â. The soft one,
hÄ', is the last letter in Ø§ÙÙÙ Allah.  Arabic also has a glottal stop, which
is a sound rarely used in English, but I have some practice saying it
because it's the apostrophe in âHawai'iâ.

[Wikimedia Commons has a gallery of basmalas](https://commons.wikimedia.org/wiki/Category:Basmala_in_Arabic_calligraphy), and web search produces
thousands more. I am looking forward to understanding more of
them.

[[Other articles in category /lang](https://blog.plover.com/lang)] 
[permanent link](https://blog.plover.com/lang/bismillah.html)
