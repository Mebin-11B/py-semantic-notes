---
title: "Coding My Handwriting"
url: https://www.amygoodchild.com/blog/cursive-handwriting-in-javascript
clipped: 2026-06-17 01:33:09
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Coding My Handwriting](https://www.amygoodchild.com/blog/cursive-handwriting-in-javascript)

## Digest Summary
The post compares the file size of two font‑generation classes. The block‑print class is 9.7 KB, while the cursive handwriting class, after minification, is 26.1 KB. The larger size stems from multiple SVG paths per character and an algorithm that adjusts point coordinates to align neighboring letters. The author notes that points are defined relative to a default font size of 20, producing decimal values (e.g., x = 14.5). By increasing the default size to 200, coordinates could be expressed as whole numbers (e.g., 145), eliminating decimal points and reducing character count. This scaling change is planned for a future update, along with other potential optimizations. An image labeled “Amy Goodchild” accompanies the text.

## Discussion Summary
The comments express strong appreciation for the clean, adaptable handwriting demonstrated, noting its impressiveness even for those with dysgraphia and highlighting how alignment influences readability. Readers show enthusiasm for further exploration, particularly wanting to see the font applied in code contexts and to experiment with it using neural‑network techniques as a learning exercise. Overall, the feedback is positive and curious, focusing on potential practical extensions rather than criticizing the current presentation.

---

## Full Article

### WHAT DOES IT WEIGH?

The letter class for the block print was 9.7kb. The letter class for the cursive handwriting (after being run through a minifier) is currently 26.1kb.

This one is larger because there are multiple paths for each letter as well as the function for adjust the points to meet the letter’s neighbours, but I have made some other savings. I’m sure further savings could be made - I am not a code golf wizard but I have a few ideas.

For example, currently the letters are designed around a default font size of 20 and then resized, meaning lots of the points are defined as e.g. x: 14.5, but if I switch this to a default size of 200, the point could be defined as 145, removing one character (the decimal place). I need to make this change carefully, so it’s on the To Do list for later.