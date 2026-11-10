---
title: "Decoy Font"
url: https://www.mixfont.com/experiments/decoy-font
clipped: 2026-08-31 12:22:51
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Decoy Font](https://www.mixfont.com/experiments/decoy-font)

## Digest Summary
Decoy Font is a TrueType font that encodes two different letters in the same glyph using spatial‑frequency separation: a low‑frequency blurred background forms the “hidden” message, while high‑frequency thin outlines convey a decoy text. When viewed up close, the outlines dominate and AI image‑to‑text models (e.g., ChatGPT, Gemini 3.5, GPT‑4) read the decoy; from a greater distance or when squinting, the low‑frequency mass reveals the intended message. The font implements the hybrid‑image principle demonstrated in optical‑illusion studies (e.g., Einstein/Marilyn Monroe composite). It can be installed like any TTF font, allowing typed text to carry concealed content without animation. Decoy Font is positioned among “anti‑AI fonts” that aim to hinder automated OCR and LLM scraping, though powerful models with advanced prompting may still recover the hidden text. The author suggests applications such as CAPTCHA, private messaging, and multilingual extensions, and invites further experimentation via a downloadable TTF file and an online playground.

---

## Full Article

# Decoy Font

A TTF font that hides what you're typing from AI. Type a message where each letter contains a decoy.100%ShuffleDownload imageHidden message11/48Decoy message11/48

## Download Decoy Font

Decoy Font is free to use in personal, commercial, and client projects. Its letterforms are derived from [DejaVu Sans Mono](https://dejavu-fonts.github.io/); see the [full font license](https://www.mixfont.com/experiments/decoy-font/DecoyFont-LICENSE.txt) for terms.64px[Download TTF](https://static.mixfont.com/assets/20260714-232642-decoyfont-htoqkd3x.ttf)

## What is Decoy Font?

Decoy font is a font that prints a decoy for every letter, making it more difficult for AI to read what you type. The font works by using separate spatial frequencies to communicate two different letters in the same space. The foreground contains thin outlines, while the background is a low-frequency mass that is blurred. When overlaid on top of each other, what you see depends on how you look at the letter. If you’re having a hard time seeing the hidden message, move your screen farther away, or try squinting to see it.Decoy font says two different things from up close vs far away

Most AI systems work by reading the pixels of an image up close. So when this type of image is pasted into an AI model like ChatGPT, even when the text is small, the llm focuses on the foreground text because that is what is most clearly outlined. However, from a slightly zoomed out distance, the text reads the actual hidden message. This simple illusion is enough to trick even more advanced LLMs like GPT Sol and Gemini 3.5 with Thinking:ChatGPT struggles to read the actual hidden message when passed a single image.Gemini 3.5 with Thinking also fails to read the actual message.

Decoy Font also exists as an actual TTF font file that can be installed and used to write complete text. You can download and install the TTF font file [here](https://static.mixfont.com/assets/20260714-232642-decoyfont-htoqkd3x.ttf). The following paragraph is written in Decoy Font - you can actually copy the text and paste it into your own notepad.

This sentence is written in Decoy Font

Funnily enough, when we pass a screenshot of this font into ChatGPT, it fails to read it properly, even though it might really clear and obvious to you.ChatGPT fails to read the Decoy Font properly from a screenshot.

Decoy Font is constructed based on the technique behind [hybrid images](https://en.wikipedia.org/wiki/Hybrid_image). This technique has been well studied for many existing optical illusions. One of the most famous is the image of Albert Einstein and Marilyn Monroe mixed together. Decoy Font applies this same idea to typography as a way to protect the words that you are typing from AI or OCR techniques.The famous hybrid image of Albert Einstein and Marilyn Monroe

We've applied this idea of spatial frequencies to create a new font that can used to obscure your writing from AI scrapers.

### Anti-AI Fonts

As AI becomes more and more capable at reading text online, there's been a rising interest in protecting information and IP from it. Anti-AI fonts can help help with obscuring text in images and ensuring that messages that are meant for humans are only read by other humans.

Decoy Font is one of the many experiments at [Mixfont](https://www.mixfont.com/) that explores this initiative. One of our other explorations in this vein is [Ghost Font](https://www.mixfont.com/ghost-font), another anti-AI font that hides a message in motion. However, where Ghost Font relies on a animation to disguise its message, Decoy Font works as a direct TTF font file and can be directly typed in projects.

Decoy Font is an interesting way to obscure messages, but it's not a guarantee. Models with powerful agents and coding abilities may be able to see past the initial lettering, and of course with some basic prompting, certain agents should know to look for the hidden letters. However, Decoy Font still serves as a initial point of confusion for AI, which can make it very effective at deterring scraping or casual observation.

### What's next?

If you're interested in exploring Decoy Font further, you can [download](https://static.mixfont.com/assets/20260714-232642-decoyfont-htoqkd3x.ttf) the TTF font file and use it in your own projects. You can also use the playground above to test out the spatial frequency technique used by Decoy Font on different letter combinations. Then, take your creations and send them to your favorite frontier LLM to see how well it works to decipher the hidden message.

Because Decoy Font can be downloaded and used as a TTF font file, I believe this makes the idea of obscuring text with AI much more accessible to the public (compared with other techniques that require motion and video). It would be interesting to see how this could be applied to technologies like captcha, or just simpler things like sending private messages between friends.

Using Decoy Font as a benchmark of text recognition LLMs would be interesting. As the intelligence of these frontier models improve, they would more and more be able to understand the techniques behind the illusion and decode both messages.

It would be a fun project to extend Decoy Font to support more languages. I believe that character based languages like Chinese would potentially benefit even more from this technique, as the characters are all roughly the same size and shape, which would make it more easy to hide a hidden message.

At Mixfont, I'm building a frontier [AI font generator](https://www.mixfont.com/font-generator) and I'm always interested to explore new ways that typography and AI intersect. I would love to hear your ideas on Decoy Font and how it can be improved. You can find me on X at [@ericlu](https://x.com/ericlu). Thanks for reading!

Thanks for checking out Decoy Font
