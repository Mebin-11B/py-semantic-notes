---
title: "I found a seashell in the middle of the desert"
url: https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert
clipped: 2026-06-17 00:55:13
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-07-10
summary_status: done
concepts:
  - geological analysis
  - morphology
  - principal component analysis
  - paleontology
  - convergent evolution
related:
  - "[[Geological Analysis]]"
  - "[[Principal Component Analysis]]"
  - "[[Convergent Evolution]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A morphological and geological analysis identifies an Al-Ghat desert fossil shell as structurally closest to a modern gastropod via Principal Component Analysis.
>
> **Key points:**
> - Explores the geological context of Saudi Arabia's desert fossil, reflecting historical marine submersions.
> - Implements an image-processing pipeline that normalizes, samples, and processes shell contour shapes.
> - Uses Principal Component Analysis (PCA) to reduce 256-dimensional coordinates to two latent dimensions.
> - Finds morphological alignment with *Sphincterochila candidissima*, attributing similarity to convergent evolution rather than direct ancestry.
> - Hosts an interactive visualization tool online for morphological shell comparison.
>
> **Concept links:** [[Geological Analysis]], [[Morphology]], [[Principal Component Analysis]], [[Paleontology]], [[Convergent Evolution]]
>
> **Suggested connections:**
> - [[Principal Component Analysis]] — applying dimensional reduction to coordinate contours in biology.
> - [[Convergent Evolution]] — explaining structural similarities across distant geological epochs.
<!-- ai-summary:end -->


# [I found a seashell in the middle of the desert](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert)

## Digest Summary
A solid rock resembling a seashell was found at the base of a cliff in Saudi Arabia’s Al‑ghat desert, far from the nearest coastline. The region’s Jurassic‑age carbonate rocks and marine fossils indicate that the Arabian Peninsula was once submerged, providing a plausible geological context for such a fossil. To infer its taxonomic affinity, the author applied a purely morphological pipeline: each shell image was centered, uniformly scaled (max radius = 1), and oriented using the longest radius; contours were sampled at 256 × 2 coordinates. Pairwise distances were computed as summed squared Euclidean differences, and Principal Component Analysis reduced the 256‑dimensional space to two latent dimensions. PC 1 captured “pointiness” of shells, while PC 2 related to vertical symmetry. Plotting the dataset (≈79 k shells from Zhang et al.) placed the Al‑ghat specimen nearest to the modern gastropod *Sphincterochila candidissima*. This species appears in the fossil record only ~38 Ma, far younger than the Jurassic, suggesting the similarity results from convergent evolution rather than direct ancestry. An interactive tool implementing the analysis is hosted at https://shell.hawzen.me.

## Discussion Summary
The comments show general appreciation for the concise, informative write‑up, with several readers noting its usefulness for understanding fossil shells and geological context. Many contribute additional details about shell morphology, regional fossil findings, and relevant resources, while a few question the identification or inject humor. Several remarks discuss the role of AI in replicating such analyses, expressing both curiosity and skepticism. Overall the discussion blends positive acknowledgment, supplemental scientific input, and light‑hearted commentary without significant disagreement.

---

## Full Article

I found a seashell in the middle of the desert
==============================================

To my amazement, I found a fully solid rock that eerily resembles a seashell at the base of a cliff in the Alghat desert, Saudi Arabia. I didn't know what to make of it at first, it had the swirls and shape of a seashell but was fully a rock, more importantly, it *shouldn't* be here; the nearest coastline is Dammam's, 500 km away.

[![Ancient fossil](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/ancient_fossil.jpeg)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/ancient_fossil.jpeg) [![Fossil location](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/fossil_location_26.07208_N_44.96803_E.jpeg)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/fossil_location_26.07208_N_44.96803_E.jpeg)

*This looks impossible*

Carbonate rocks (e.g. limestone), marine fossils, coral fossils, and sedimentary structures (like ripples or bioturbation) all exist in and around Alghat, which points to the fact that parts of the Arabian Peninsula were once submerged under the sea. Specifically in the late Jurassic age (~150 million years ago)[1].

[![Fossil location](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/marine_macroinvertebrate_lower_hanifa_figure_2_stratigraphy.png)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/marine_macroinvertebrate_lower_hanifa_figure_2_stratigraphy.png)

*Stratigraphic distribution figure of areas near Najd[1]*

Nevertheless, I was still super curious about the fossil I found; what animal inhabited it? what did it look like back in the Jurassic age? any modern relatives or lookalikes?

The proper way of answering these questions is to conduct a detailed analysis of the fossil (e.g. via inspecting the sediment it was found in, its shape, etc.), this should be done by an expert paleontologist. However, I know no paleontology, or any paleontologist, so I figured I could DIY it myself (how hard could it be..?), though I'll do it strictly via its shape — or what's called its *morphology*. Morphology alone is probably not accurate enough to discern lineage as different species might lookalike but are from different lineages, so this is probably not the best way to do it, but it sounded fun and intuitive, so I gave it a try.

Concretely, I plan on:

1. Mathematically representing the shape of a shell
2. Defining a distance metric between shapes (so that I can find shells similar to the fossil's)
3. Mapping out the *space* of shapes

7894 different species and 59244 images of shells were in the Zhang, et al. shell dataset[2]; good enough for me!

Capturing 'shape' is actually a very hard problem; any object can be rotated by [pitch, yaw, roll](https://simple.wikipedia.org/wiki/Pitch,_yaw,_and_roll), scaled, and translated. Before starting any statistical analysis, I followed a guideline to isolate the shape from other factors

1. The shell must be centered to the midpoint of the picture
2. The scale of the shell must be equivalent across all images (specifically, the maximum distance from the origin is 1)
3. Orientation is the hardest part
   * Pitch and yaw can be fixed by only choosing samples where the shell's opening is facing the camera. This is not perfect, but I found the dataset to be pretty consistent with its angles
   * Roll is difficult. A shell can be rotated in any way around the axis (even whilst the opening is facing the camera). My *fix* was to use the longest radius as the reference point, and rotate the shell so that the longest radius is always on the right. This is not perfect either, but it was good enough for me.

Then, I extracted the contour of the shell to 256 points relative to the center. This way, each shell is represented by a 256x2 matrix, where each row is the (x, y) coordinates of a point on the contour. Example:

```
> contours[0].shape

(256, 2)

> contours[0].tolist()[:5]

[-0.38561132550239563, 0.9804982542991638],
 [-0.4204626679420471, 0.9785506725311279],
 [-0.4553140103816986, 0.976603090763092],
 [-0.4901654124259949, 0.9746555089950562],
 [-0.5230183005332947, 0.9685550928115845]]
```

[![Ancient fossil](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/experimentation_data/shells.png)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/experimentation_data/shells.png)   
[![Fossil location](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/experimentation_data/normalized.png)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/experimentation_data/normalized.png)
[![Fossil location](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/experimentation_data/contours.png)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/experimentation_data/contours.png)

*Normalization pipeline*

Naturally, the distance between two shells s1 and s2 is [squared euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between their contour points:

$$
d(s1, s2) = {\sum\_{256} (s1.x\_i - s2.x\_i)^2 + (s1.y\_i - s2.y\_i)^2}
$$

Representing the space will require 256 dimensions, which is a little more than just the 2 I need to plot it over x and y. Given the normalized shell contour above, it's clear that many of these dimensions are redundant (for instance, the space of all possible 256 contour points allows intersection, while the space of possible shells doesn't, AFAIK), so the space of possible shells can be condensed into a smaller *[latent space](https://en.wikipedia.org/wiki/Latent_space)*. To drive my point home, I'll show three examples of fully random contours (i.e. pseudo-random points around the origin).

[![Ancient fossil](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/experimentation_data/random_contours.png)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/experimentation_data/random_contours.png)

*Probably not a real shell*

Dimensionality reduction techniques map the original 256 dimensions onto a smaller number of dimensions (e.g. 2 or 3) while trying to preserve the distance between shells as much as possible. One such technique I'll be using is [Principal Component Analysis (PCA)](https://en.wikipedia.org/wiki/Principal_component_analysis). Here's an excellent fragment that explains how PCA works: <https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues/140579#140579>.

After applying PCA, I retained 56.50% of the variance using only the first principal component (PC1), and 67.25% using the first two. This means we can describe a shell's shape by only two numbers, and be pretty close to the original shape!

The interesting part is trying to understand what these two numbers mean; dimension 1 in the original 256-dimensional space annotates the location of the first contour point of the shell, whereas dimension 1 of the latent space annotates a high-level feature, learned by the PCA algorithm. We can visually try to understand what PCA dimension PC1 represents by finding two shells, diametrically opposite in the PC1 dimension, yet similar in all other dimensions.

Essentially, we want to find two shells i and j such that the following score is maximized:

$$
\text{score}(i,j) =
\frac{|z\_{i,1} - z\_{j,1}|}
{|\mathbf{z}\_{i,2:k} - \mathbf{z}\_{j,2:k}|\_2}
$$

PC1 seems to capture the 'pointiness' of the shell, i.e. more than 50% of variance in shell shapes can be explained by how pointy they are. PC2 seems to capture the symmetry of the shell, or perhaps the mass distribution over the vertical axis. I'll leave the interpretation of the other dimensions as an exercise for the reader (I have no idea).

[![PCA](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/PCA.png)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/PCA.png)

And now for the grand finale, we can plot the shells in the latent space, and see where our Alghat fossil fits in it. But first, for dramatic tension, I will discuss the plot.

The plot represents PC1 on the x-axis and PC2 on the y-axis, while color represents the roughness of a shell (computed as the difference in slope between consecutive points). The following observations are worth noting:

1. Negative PC1 values (representing roundness) are way more common than positive PC1 values (representing pointiness). Yet roundness is less diverse and occupies less space than pointy shells
2. Pointy shells seem to be way more rough than round shells
3. Negative PC1 values always have PC2 values close to zero; no shell in the dataset has a round but asymmetric shape. Below, I will project those shells back from latent space to the shape space, imagining *impossible* shells

[![map](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/map.png)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/map.png)

*Map of shell latent space with example shells*

[![PC1 animation](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/PC1.gif)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/PC1.mp4)
[![PC2 animation](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/PC2.gif)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/PC2.mp4)

*Modifying Principal Components against the mean shell*

[![Impossible shell projections](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/impossible_shapes.gif)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/impossible_shapes.mp4)

*Projecting 'impossible' shells*

So, what shell most closely resembles our Alghat fossil? It's Sphincterochila candidissima (try to pronounce it). However, it is really young, nowhere near the Jurassic age; instead, the earliest fossil of it dates back 38 million years ago[4]. Ultimately, shape is not the best way of determining shell lineage, but its eerie similarity to the Alghat fossil is still fascinating, and perhaps points to some sort of convergent evolution, where two different species evolve to have similar shapes due to similar environmental pressures.

[![closest](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/comparison.jpeg)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/comparison.jpeg)
[![closest](https://camo.githubusercontent.com/3465ed4b0e4d1eb0afad41c09970a9c65d0c312a3e465e0822ec60228d160fbc/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f382f38302f537068696e637465726f6368696c615f63616e646964697373696d615f766976615f30312e6a7067)](https://camo.githubusercontent.com/3465ed4b0e4d1eb0afad41c09970a9c65d0c312a3e465e0822ec60228d160fbc/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f382f38302f537068696e637465726f6368696c615f63616e646964697373696d615f766976615f30312e6a7067)

*Left: Alghat fossil compared, Right: Sphincterochila candidissima[3]*

Feel free to explore the tool and try to figure out where a shell of your choice fits in the shell latent space!

<https://shell.hawzen.me>

[![](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/raw/main/media/demo.png)](https://github.com/Hawzen/I-found-a-seashell-in-the-middle-of-the-desert/blob/main/media/demo.png)

This article has been published to HackerNews, and numerous users have given their insightful opinions and additions. Feel free to read them in: <https://news.ycombinator.com/item?id=48318402>

1. Aba Alkhayl, S. S. (2022). Marine macro-invertebrate fossils from the Lower Hanifa Formation (Hawtah Member), central Saudi Arabia. Arabian Journal of Geosciences, 15, 1410. <https://doi.org/10.1007/s12517-022-10581-w>
2. Zhang, Q., Zhou, J., He, J. et al. A shell dataset, for shell features extraction and recognition. Sci Data 6, 226 (2019). <https://doi.org/10.1038/s41597-019-0230-3>
3. <https://en.wikipedia.org/wiki/Sphincterochila_candidissima>
4. Tracey, S., Todd, J. A., & Erwin, D. H. (1993). Mollusca: Gastropoda. In M. J. Benton (Ed.), The Fossil Record 2 (pp. 131–167). London: Chapman &