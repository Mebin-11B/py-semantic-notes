---
title: "I Bypassed Adobe and Microsoft to Build a Git-Tracked Book Production Pipeline"
url: https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/
clipped: 2026-06-17 00:57:03
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [I Bypassed Adobe and Microsoft to Build a Git-Tracked Book Production Pipeline](https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/)

## Digest Summary
The author describes a self‑publishing workflow that replaces proprietary tools (Word + InDesign + Calibre + Kindle Create) with a fully version‑controlled pipeline. Original manuscripts are written in LibreOffice Writer (ODT) using semantic paragraph and character styles for language, poetry, epigraphs, etc. A custom Python/lxml script parses the ODT XML, maps styles via a TOML config, and outputs both XHTML (for Standard Ebooks‑compatible EPUBs) and LaTeX (for high‑quality print PDFs). The EPUB is linted with the Standard Ebooks command‑line tool, ensuring strict compliance with its style guide. LaTeX uses the memoir class with fontspec, polyglossia, graphicx, and microtype for advanced typography. All source files (ODT, generated XHTML, and TeX) are stored in Git, enabling diffs of content changes and reproducible builds on any platform, including Linux. The system eliminates reliance on .docx and .indd files, streamlines updates, and provides consistent print and electronic outputs while preserving the author’s preferred word‑processor editing environment.

## Discussion Summary
The comments acknowledge the article’s usefulness while noting the author’s limited grasp of existing publishing automation. Contributors cite established workflows—such as InDesign’s placed‑text updates, LaTeX, Asciidoctor, Pandoc, Typst, and CI/CD pipelines—that streamline multi‑format production, and they share personal tools that reduce manual effort. There is a recurring call for more accessible, open‑source converters for Word, PDF, and e‑book formats, and for better handling of print‑ready PDFs. Overall, the discussion is constructive, blending praise with technical critique and suggestions for improvement.

---

## Full Article

The most important piece of fiction writing is the story. Are the characters compelling? Is the plot exciting and coherent? Is the story believable? Paired with that is writing quality, which includes grammar, syntax, spelling, and punctuation. Without an immense amount of work on these points, authors lack a book worth publishing.

Formatting and typesetting a novel can become an afterthought. It’s probably the most technology-driven part of the self-publishing process, which can be scary to authors who just want to get a polished book into readers’ hands. I don’t mean to imply my formatting process is the best or the easiest. It works for me and satisfies my inclinations as both an independent novelist and software developer.

Word + InDesign + Calibre + Kindle Create
-----------------------------------------

I started safe. All three of my Christian historical novels—[*Heretics of Piedmont*](https://www.djspeckhals.com/books/witnesses-of-the-light/heretics-of-piedmont/ "Heretics of Piedmont"), [*The Lord of Luserna*](https://www.djspeckhals.com/books/witnesses-of-the-light/the-lord-of-luserna/ "The Lord of Luserna"), and [*Prince of Savoy*](https://www.djspeckhals.com/books/witnesses-of-the-light/prince-of-savoy/ "Prince of Savoy"), plus my novella [*The Outcast of Chivasso*](https://www.djspeckhals.com/books/witnesses-of-the-light/the-outcast-of-chivasso/ "The Outcast of Chivasso")—started as Microsoft Word files (DOCX). The vast majority of editors and proofreaders rely on Word for tracked changes, and practically every final formatting program (Adobe InDesign, Kindle Create, Calibre, Atticus, etc.) can import DOCX files. Like a good boy, I used paragraph styles rather than manual formatting. My Word document—named something like “Heretics-of-Piedmont\_revised-final-3.docx”—became my source of truth, the common ancestor for all final formats.

I didn’t want to format my book for print in Word, though. Can it be done? Yes. Does it meet the quality standards of professionals? That’s debatable. Its hyphenation and justification leave a lot to be desired, among other weaknesses. The last time I checked (early 2026), Word doesn’t include [microtypography](https://en.wikipedia.org/wiki/Microtypography) features like desktop publishing software does.

Other options exist, but Adobe InDesign is the industry standard. Professionals use its battle-tested feature set to produce what truly can be art. I wanted that level of quality in my own books. So I held my nose and plunged into the world of Adobe Creative Cloud. I didn’t know how to use InDesign at first, but I read a lot and watched plenty of YouTube videos on the craft. I learned about DOCX style mapping, preventing em-dash breaks, crisp margins, page balancing, attractive drop-caps, tracking, optical margins, baseline grids, and other minutia. Plenty of jargon there, but the work is quite satisfying, especially when you notice the details in the end product. (Side note: when I browse bookstores, I always investigate how big publishing houses do it.) When I got to the sequels, I again chose InDesign.

Ebooks are an entirely different matter. There are many decent options to produce an EPUB, but none seem to dominate ebook publishing like InDesign does for print. [Kovid Goyal](https://kovidgoyal.net/) is a familiar name in the software world; he’s one of those talented developers who make working with computers better for the rest of us. Perhaps his most well-known contribution is [Calibre](https://calibre-ebook.com/), a powerful ebook manager. Not only can you read nearly any ebook with it, but it also includes an amazing ebook authoring toolset. Importing from a Microsoft Word document is a breeze, and with a little HTML and CSS knowledge, you can create a very compatible EPUB.

Kindle is a different story. You *can* upload EPUBs to Kindle Direct Publishing (KDP), where they will convert it into their proprietary KFX file. I never had success uploading the EPUBs I had created with Calibre, however. Amazon’s suggested solution is their [Kindle Create](https://www.amazon.com/Kindle-Create/b?ie=UTF8&node=18292298011) program, which worked okay, but that was yet another format to maintain. The software developer in me was screaming for a better solution.

Opportunities
-------------

Making the slightest change became a chore.

* Update the “master” DOCX
* Update InDesign file, export PDF, upload to distributors
* Update EPUB in Calibre, export EPUB, upload to distributors
* Update in Kindle Create, export KPF, upload to KDP

A Linux laptop is my daily driver, but neither Kindle Create nor InDesign run on it (even with Wine), so I had to switch to my family Macbook—first-world problems, but I like what I’m used to.

A few years ago on [Hacker News](https://news.ycombinator.com), I discovered [Standard Ebooks](https://standardebooks.org/). I read the project’s goals and skimmed a few of their published works. To say I was impressed is an understatement. Their books were miles ahead of any free ebook. I noted the project and have since read at least a dozen books from their growing library of public domain works (by the way, they’re a worthy cause to [support](https://standardebooks.org/donate)). If only my own ebooks could match their quality.

Pivoting
--------

I finished *Prince of Savoy*, Book 3 of my trilogy, in 2025 and was ready to format it. As I had done numerous times, I imported the Word document into InDesign and formatted the print version. But then I had an idea—what if I followed Standard Ebooks’ (SE) process instead? For a few reasons, I used Calibre to convert the DOCX to a clean EPUB, to which I would later apply [SE’s Manual of Style](https://standardebooks.org/manual/latest/single-page) via their [detailed guide to producing an ebook](https://standardebooks.org/contribute/producing-an-ebook-step-by-step#rough).

I quickly discovered how strict, how pedantic, and how utterly opinionated SE is. Their style guide leaves little room for interpretation or ambiguity, which, if followed properly, results in a pristine EPUB that’s compatible on practically all devices. The process was a chore, especially the first time I worked through it. I told myself, “Trust the process; it’ll be worth it,” because it often felt more like a chore. Looking back, I feel like SE’s tools (all funnelled through the powerful [`standardebooks` command line program](https://github.com/standardebooks/tools)) are like having a copyeditor for ebook formatting or a linter for code. Here are some examples from SE’s linter:

* Illegal unit used to set `font-size`. Hint: Use `em` units.
* Word count in metadata doesn’t match actual word count.
* Header element with incompatible semantics. Hint: Headers should be either `title` or `ordinal`, not both.
* Possessive `’s` within name italics. Hint: If the name in italics is doing the possessing, `’s` goes outside italics.

…among hundreds of other checks. The strictness appeals to me as a software developer. Getting all lint rules to pass took some time, but it was satisfying to end up with a clean directory of XHTML source files, version controlled in Git, easily built as an EPUB with the `se build` command. I had scratched Kindle Create from my workflow, because Standard Ebooks EPUBs converts well for Kindles. *Prince of Savoy* was ready to distribute, and I was thoroughly satisfied with its electronic format.

With the trilogy complete, I wanted to go back and revise the first installment, *Heretics of Piedmont*. I spent 3 weeks of free time improving minor details (eliminating a few anachronisms, slimming prose, adding three hand-drawn maps), with the goal of fully matching the style of Books 2 and 3. But I was tired of editing the document on a Windows computer—or worse, Office 365 Online. Pedantically, I performed the conversion from DOCX to ODT (Open Document Text, the native format for LibreOffice Writer).

Does LibreOffice have its shortcomings? Certainly. But from my experience, it does its job: I can type, check spelling and grammar, and perhaps most importantly, apply styles. As I revised, I added semantic paragraph styles for songs, letters, poems, epigraphs, glossary entries, etc.; character styles are a less used feature of word processors, but they can act as semantics that go beyond basic formatting. I created styles for each foreign language (seven of them in *Heretics of Piedmont*) and applied them to the approximately one hundred non-English phrases in the text. There are also character styles for direct thoughts, creative work titles, prayers, and emphasis; though all of these translate to *italics* when reading in print and electronically, having these semantics is a key in producing a Standard Ebooks-compliant EPUB. Not only do the semantic attributes make the book more accessible for those who use screen-readers, but they also enable more control that surpasses simple italics formatting.

Now I had a clean, semantically rich ODT file: open source, easy to edit, and as I would soon discover, simple to parse. I chose this file as my “source of truth.” “Why didn’t you just author it in LaTeX? Or Markdown? Or RST?” you might ask. I considered each of those, but I prefer writing novels in a word processor, not a text editor.

Now I needed to create a PDF and an EPUB. Though I had never parsed an ODT file, a little Python, lxml, and Claude Code helped me quickly draft the conversion script. The script maps the XML nodes of the ODT file to an intermediary structure, which then allows for easily output to XHTML (and eventually LaTeX; I’ll get to that later). I ran the conversion script with a TOML config file (which maps ODT styles to XHTML elements and attributes), and I had everything I needed for the SE EPUB—and only a couple lint errors to fix. Ebook goal accomplished!

The more difficult path was the print PDF. I desperately wanted LibreOffice Writer to have the features I needed. Coincidentally, several microtypography features landed in 2025 that sounded much like Adobe InDesign’s capabilities. Would it be that simple?

Unfortunately, no. Though I read through changelogs and saw the care volunteer developers took in bringing microtypography to Writer, it wasn’t up to the task yet. The end edge of the page was ragged, the bottom edge was unbalanced, and drop caps appeared odd. I tried Scribus too, but 200+ page books bring the program to a crawl. And the results were worse than Writer. I’d have to settle for InDesign, I figured.

Then I thought of [LaTeX](https://en.wikipedia.org/wiki/LaTeX). I had heard of it since I started programming but was never fully exposed to it. In college (non-STEM), I submitted papers as Word documents or PDFs. LaTeX seemed daunting, but it had the features I desperately wanted: advanced typography, ability to automate, and version control. I tested a chapter from my book as LaTeX and compared the output with Adobe InDesign’s. It was nearly indistinguishable.

Now the hard part: How do I convert an ODT file to TeX? [Pandoc](https://pandoc.org/) can, but custom Writer styles aren’t carried over. So I repurposed the same conversion script I used for ODT→XHTML and generalized it to support ODT→TeX. Perhaps some day I’ll open source that code, but it’s currently tailored for my own unique use cases, and I’m not sure it will help others yet.

Retrofitting
------------

At last I had a sustainable, automated, version-controlled path for producing print and electronic versions of my books—without proprietary software like Word and InDesign. There’s still the downside of having to edit the “master” ODT file, then regenerating the PDF and EPUB, but it’s a trivial process I can perform on any computer. I had transitioned from opaque binary(ish) `.docx` and `.indd` files to plain-text `.xhtml` and `.tex`. Seeing exactly what changed in a proofreading pass via `git diff` was a massive quality-of-life win.

Even though I had revised and “retooled” *Heretics of Piedmont*, I still had two other novels and a novella that used the old tools. I also converted those Word documents to semantic Writer documents, then my conversion script handles the rest.

Is there room for improvement? For sure. I would love if the XHTML and TeX were artifacts rather than code. I currently have separate Git repositories for the XHTML and TeX for each book, mainly because I want the ODT file to remain the source of truth. It’s easier for me to write in, and professional copyeditors and proofreaders want word processor documents for their work.

My process certainly isn’t for everyone. Most independent authors would be fine with either hiring a professional formatter or settling with something similar to my earlier process. In the end, readers don’t care about the formatting process. They want to read a good story. I want to provide that first, but if I can also enjoy the formatting, I’ll count that as a win for my readers too.

Appendix: The LaTeX Preamble
----------------------------

For anyone interested in the underlying mechanics, you can [view the full LaTeX preamble here](https://www.djspeckhals.com/documents/latex-preamble-heretics-of-piedmont/ "LaTeX Preamble | Heretics of Piedmont").

These are the key packages I used:

* [`memoir`](https://ctan.org/pkg/memoir): “batteries included” class for document creation
* [`fontspec`](https://ctan.org/pkg/fontspec): allows rendering of OpenType fonts (like my favorite body text, [Adobe Garamond](https://fonts.adobe.com/fonts/adobe-garamond))
* [`polyglossia`](https://ctan.org/pkg/polyglossia): provides hyphenation patterns per language; I occasionally use non-English languages like Old Occitan and Latin for reader immersion
* [`graphicx`](https://ctan.org/pkg/graphicx): allows advanced embedding and adjustment of images like maps and my author portrait
* [`microtype`](https://ctan.org/pkg/microtype): provides the previously-mentioned features that enhance the appearance and readability of every page—one of the main reasons I chose LaTeX