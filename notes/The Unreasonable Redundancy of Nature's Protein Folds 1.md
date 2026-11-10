---
title: "The Unreasonable Redundancy of Nature's Protein Folds"
source: "https://research.ligo.bio/posts/unreasonable-redundancy-of-natural-protein-folds/"
author:
published: 2026-05-20
created: 2026-07-01
description: "A Ligo research note on redundancy in natural protein fold space and what kind of data still carries signal."
tags:
  - "clippings"
---
Over the last few years, deep neural networks have made generative language modeling dramatically more powerful, giving us large language models. A similar leap happened for continuous modalities like images and videos. Recently, similar techniques have been applied to the generative modeling of biomolecules with great success. Models such as DeepMind's AlphaFold3 made it much easier to predict biomolecular interactions, including drug-protein and antibody-protein complexes, and soon after people figured out how to re-purpose these capabilities to design drug-like molecules. In the near future, we might see most antibodies entering the clinic designed in large part with deep-learning-based generative models, potentially with superior pharmaceutical properties and targeting receptors that have resisted wet-lab based approaches.

How would you improve on these systems? We definitely want to have better biomolecular modeling so we can put better drugs into the clinic. The recipe for improving a deep learning system has been surprisingly simple at a high level: you scale the model, scale the compute, and scale the data. LLMs are obviously improving by being scaled aggressively. AlphaFold3 was also a major effort to scale the model and data; it is trained on a broad collection of known biomolecular complexes, from experimental structures and protein-ligand complexes to the enormous sequence databases produced by genomics and metagenomics such as MGnify. Internally, DeepMind called the project "all-PDB" for a while, referring to all the interactions represented in the Protein Data Bank.

The key move in AlphaFold3's scaling recipe was to turn sequence scale into structure scale: use structure prediction to convert large protein sequence databases into predicted 3D structures. Genomics and metagenomics have given us billions of protein sequences, many inferred from environmental DNA collected from organisms that have never been cultured in the lab. For training structure-based design models, though, the useful object is often the 3D structure. Structure prediction models let us convert some of that sequence scale into structural data: take millions of natural sequences, predict the folds they adopt, and use those predicted structures as training examples for the next generation of biomolecular models.

At Ligo, we care about this recipe because we train generative models for designing enzymes. When we tried to scale our structural training data by folding more natural sequences, we ran into a problem: natural protein sequences are vast, but their folds are much more redundant than the sequence counts suggest. This post is about that mismatch, and about why simply folding more natural sequences may not buy as much new structural diversity as we hoped. We will describe data engineering tricks for clustering the known protein universe, and what our results imply about how to think about the enzyme design problem.

## Modern biomolecular models rely on sequence scale

Modern structure prediction models rely heavily on multiple sequence alignments. A multiple sequence alignment, or MSA, lines up related versions of a protein from different organisms. When two positions in that alignment tend to change together, it can be a clue that the corresponding residues are close in 3D space or tied together by function. My mental model of AlphaFold2 is that it used this kind of coevolutionary signal to constrain the rough geometry of a protein, then learned how to fill in the rest of the structure.

AlphaFold3 seems to be doing something broader. Its antibody-antigen performance is especially interesting because there are no MSAs to extract clues from. Antibodies and their targets do not share an evolutionary history. To do well there, the model has to learn something about protein surfaces themselves: which shapes, chemistries, and local geometries are likely to be compatible with each other. That is a different kind of signal than residue coevolution within one protein family.

This is where MGnify-scale data may matter. Metagenomic sequence resources expose models to enormous numbers of natural variants, many from organisms we have never cultured. The empirical clue is that models trained with MGnify-scale protein distillation seem to separate most clearly on antibody-antigen prediction, where direct coevolution cannot explain the interaction signal ([Supplementary info](#supplementary-interface-benchmarks)). That increased coverage of sequence space looks valuable. The question is whether it also comes with comparable diversity in protein folds.

## Sequence diversity is not fold diversity

The theoretical protein sequence space is absurdly large: a protein of length N has 20 <sup>N</sup> possible amino-acid sequences. Natural proteins occupy only a tiny, highly structured part of that space. Evolution tends to reuse folds that are stable, expressible, and adaptable, rather than scattering proteins uniformly across every possible sequence and shape.

That matters for training data. When we scale predicted structures, we are not necessarily adding independent examples. We may also be adding many sequence variants of the same fold families, domain combinations, and evolutionary compromises. The example below shows the basic problem: proteins can look far apart when measured by sequence similarity, while still being very close in fold space.

One concrete example from our AFDB fragment clusters: in structural cluster `A0A242HMU2_f1`, three proteins are only 23.9–28.3% identical in sequence while still sharing the same fold (TM-score > 0.75).

| Fragment | UniProt annotation | Length | Seq. id. to rep. | TM to rep. |
| --- | --- | --- | --- | --- |
| `A0A518BRX6_f1` | 3-oxoacyl-\[acyl-carrier-protein\] reductase FabG, Bacteria | 249 aa | 100% | 1.000 |
| `A0A1Q3EPK1_f1` | NAD-binding protein, *Lentinula edodes* | 283 aa | 28.2% | 0.768 |
| `A0A6I8MDZ6_f1` | Short-chain dehydrogenase/reductase SDR, *Oceanivirga miroungae* | 261 aa | 23.9% | 0.793 |

### Same fold, low sequence identity

Three AFDB predictions from the same structural cluster, aligned with local TM-align.

`A` FabG reductase `B` SDR protein `C` clipped NAD-binding core

Aligned fold overlay ready.

The NAD-binding protein was clipped to residues 201-483 before alignment. The removed N-terminal tail had mean pLDDT 31.9, while the retained core has mean pLDDT 91.3. The overlay uses A0A518BRX6 as the reference frame.

As we scale up our sequence datasets, how many genuinely new folds should we expect to see? If MGnify grew 10x, how many of those new sequences would actually be structurally novel?

To answer this systematically across the whole space, we need a scalable clustering algorithm. Foldseek is a brilliant tool for this, and its authors have already clustered the AlphaFold Database with it, [reporting 2.3 million non-singleton structural clusters](https://www.nature.com/articles/s41586-023-06510-w). But there are real issues with clustering predicted structures, and the clustering problem itself is ill-posed. We think the true number of reusable structural neighborhoods **is much closer to tens of thousands than to the 2.3 million non-singleton clusters reported by that fast Foldseek pass** — closer to 25,000 than 2.3 million in our current analysis. Here's the reasoning.

## The predicted-structure problem for clustering

Predicted structures are different from crystals. The sequences and MSAs are real, but the structures are missing context, and AlphaFold will predict the whole chain: ordered domains, floppy tails, long linkers, signal peptides, and multi-domain proteins whose relative placement may not be meaningful.

This makes the clustering problem ill-posed. Are two proteins the same fold because one domain matches? Are they different because one has a disordered extension?

The shape of predicted structures is also a problem for training generative models on this data. You don't want to waste model capacity fitting disordered regions, and you don't want to learn to generate bizarre, elongated chains. You could filter on global pLDDT, radius of gyration, and similar whole-chain metrics, but those filters are too crude for data shaped like this — they throw out good domains attached to bad tails. We need a more surgical way to keep the signal and drop the noise.

### Predicted chains are not clean domains

very high confident low very low

`A0A5B2Z7Q7`, ArsR-family transcriptional regulator

AFDB prediction ready.

`P38398-3`, breast cancer type 1 susceptibility protein isoform (BRCA1)

AFDB prediction ready.

## First pass: remove the obvious noise

Our first attempt was simple. Remove residues below a pLDDT threshold, split what remains into contiguous sequence fragments, and then spatially rejoin fragments that are clearly touching. The rejoin step is a union-find problem: if fragment A touches B, and B touches C, then A, B, and C become one connected fragment.

- Residues below pLDDT 65 are marked as unusable.
- Remaining residues become contiguous sequence fragments.
- Fragments with enough close contacts are merged spatially.
- The resulting candidates can then be filtered before clustering.

This gets rid of a lot of obvious disorder. It also keeps ordered domains that global filters would throw away because the full protein looked too long, too extended, or too messy.

**Limitations of naive fragmentation.** The obvious failure mode is a high-confidence linker. If the linker survives the pLDDT filter and makes enough contacts, the spatial merge can connect two domains that we would rather treat separately. Union-find then does exactly what it was asked to do: it turns the connected chain into one fragment.

The problem is that this is not really a local-confidence question. The residues can be predicted confidently and still be the wrong unit of training. What we need to detect is the bottleneck in the spatial graph: the narrow path that connects otherwise independent pieces.

### A0A0E0RCK4 first pass

The full chain is kept intact; fragments shorter than 20 residues are left unnumbered.

First-pass coloring ready.

pLDDT < 65 fragment 1 (178 aa) fragment 2 (196 aa)

## The graph-theoretic split

We need a way to split proteins based on how the residues are connected to each other. For that, a protein is naturally a graph: each residue is a node, and edges connect residues that are close in space. We use C-alpha atoms from the confident part of the prediction, connect each residue to its spatial nearest neighbors, and give close neighbors stronger weights than distant ones. In the current version, each residue sees its 15 nearest spatial neighbors.

This turns the fragmentation problem into a connectivity problem. A compact domain becomes a dense local graph. A high-confidence linker becomes a narrow bridge between two dense regions. Graph theory gives us tools for asking whether that bridge is really part of one unit, or whether it is holding two independent pieces together.

### Graph theoretic split of a nearest neighbour protein graph

Nearest-neighbor graph ready.

Fiedler vector

The protein cartoon is shown in Mol\* green; the overlay is the actual k-nearest-neighbor graph, with each edge colored by the average Fiedler value of its endpoint residues.

Spectral bisection asks for the weakest global connection in this graph (why the quantity we compute finds this connection is a little bit black magic to me, ask the graph theorists). We found that the spectral bisection points of a protein correlate very well with the points we'd cut at if we were manually identifying different protein regions. A standalone version of the splitter is included in [Supplementary info](#supplementary-spectral-split).

### For the curious: the Fiedler vector

Given a weighted adjacency matrix $W$ of a graph, the normalized graph Laplacian is:

$$
L_{\mathrm{sym}} = I - D^{-1/2} W D^{-1/2}
$$

Here $D$ is the diagonal degree matrix. The eigenvectors of $L_{\mathrm{sym}}$ reveal graph structure:

- The smallest eigenvalue is always 0.
- The second smallest eigenvalue, $\lambda_2$, measures algebraic connectivity.
- The corresponding Fiedler vector gives a useful two-way partition: residues with opposite signs sit on opposite sides of the cut.

This is the same quantity shown on the graph above. The protein is just green context, while the graph edges are colored by the average Fiedler value of their two endpoint residues. Strongly negative edges are blue, strongly positive edges are red, and edges near zero are pale. Those near-zero residues are the bottleneck between the two sides, so those are the residues we remove before assigning fragments.

### Recursive bisection

A single bisection only finds one cut. Multi-domain proteins need repeated cuts, so after each split we check each partition separately. If a partition has `λ<sub>2</sub> > threshold`, we treat it as internally well connected and stop. Otherwise, we split again.

### Naive merge versus spectral pipeline

Both panels load one full-chain CIF; fragments shorter than 20 residues are left unnumbered.

**`A0A0M9EDZ0`** uncharacterized protein, Candidatus Magnetomorum sp. HK-1 573 residues; mean pLDDT 92.4

Naive pLDDT + union-find: 1 fragment; largest 568 aa

Fragments ready.

low confidence / cut (5 aa) fragment 1 (568 aa)

Spectral pipeline Fiedler + spatial merge: 2 fragments; largest 418 aa

Fragments ready.

low confidence / cut (8 aa) fragment 1 (418 aa) fragment 2 (147 aa)

The right panel shows the current split-then-merge pipeline: spectral bisection first proposes cuts, then spatial clustering re-merges pieces that still look like one compact unit.

## Clustering the fragments

Once we split proteins into their "interacting units", the unit of clustering is no longer one predicted protein. It is one compact fragment. We can cluster those fragments by structural similarity and ask how much independent fold signal the distillation sets actually contain.

We cluster MGnify at roughly 30% sequence identity with MMseqs2, which gives about 40 million sequence clusters. From there, we discard sequence singletons, then use the [OpenFold3-predicted structures released through the OpenFold datasets portal](https://portal.openfold.omsf.io/datasets) for the remaining MGnify sequences. We fragment those predicted structures and filter the fragments with quality metrics meant to keep examples amenable to training a generative model (we will write more about this in a later post). The structural clustering below starts from the resulting set: about 2 million MGnify fragments.

[We use Foldseek for the first pass of clustering](#supplementary-foldseek-command). Foldseek's fast mode uses both structural and sequence-derived signals, which is what makes it practical, but also means it can split fragments that are structurally very similar and sequence-divergent.

### Common pitfall: Foldseek singletons are not always singletons

A Foldseek singleton is not necessarily a new fold. It only means no other fragment crossed the thresholds in that particular Foldseek run. To check this failure mode, we took 1,000 fragments that Foldseek had labeled as singletons and compared them against each other with pairwise TM-score. At TM ≥ 0.8, 373 of those fragments fell into 69 connected components. The largest hidden cluster had 35 members. These were supposed to be singletons.

### Hidden clusters among Foldseek singletons

Each panel overlays four fragments that Foldseek had separated into singleton clusters.

Cluster 6 18 singletons · min TMalign TM 0.953–1.000

Singleton overlay ready.

Cluster 11 7 singletons · min TMalign TM 0.929–1.000

Singleton overlay ready.

Cluster 13 6 singletons · min TMalign TM 0.841–1.000

Singleton overlay ready.

Three hidden clusters from a random sample of 1,000 Foldseek-labeled singleton fragments. Each panel shows one representative plus three aligned members from the same TM-score component. Ranges use the lower of the two directional TM-scores reported by `TMalign.cpp`.

The practical lesson is to be skeptical of the singletons. If we treat every Foldseek singleton as an independent structural mode, we overestimate novelty and give the sampler a distorted picture of fold space. TM-score is much slower, but it is the right ground-truth audit pass when the question is whether two fragments really share a fold.

So we added a second pass over cluster representatives. Instead of comparing every fragment to every other fragment, we compared representatives against representatives with a more structure-centered alignment, then confirmed candidate merges with our TM-align implementation. Merge criterion: min(tm\_norm\_a, tm\_norm\_b) ≥ 0.7. Both directions had to independently confirm fold-level similarity. If two representatives passed that test, we merged their clusters with union-find.

1.96M → 25.3K MGnify fragments → structural clusters

71.5% of MGnify multi-member fragments are in the top 1,000 clusters

64.3% of AFDB multi-member fragments are in the top 1,000 clusters

| Dataset | Fragments in multi-member clusters | Multi-member clusters | Largest cluster | Top 100 | Top 1,000 |
| --- | --- | --- | --- | --- | --- |
| AlphaFold Database | 1,592,372 | 30,622 | 20,836 | 26.0% | 64.3% |
| MGnify | 1,961,750 | 25,302 | 41,801 | 29.1% | 71.5% |

These are the results that surprised us. After sequence clustering, fragmentation, quality filtering, and dropping singleton clusters from this summary, MGnify is not two million independent structural examples. The repeated part of the dataset is closer to twenty-five thousand structural neighborhoods, with most of the mass concentrated in a small head of the distribution. The top 1,000 MGnify clusters are only about 4.0% of the multi-member cluster list, but they contain 71.5% of the fragments in those clusters.

### MGnify is dominated by a small head of clusters

Singleton clusters are omitted here to focus on the multi-member distribution.

**1.96M** fragments plotted **25.3K** multi-member clusters **71.5%** in the top 1,000

#### Cumulative fragment mass

<svg id="cluster-cumulative-svg" viewBox="0 0 660 390" role="img" aria-label="Cumulative percent of MGnify fragments covered by the largest clusters"><line x1="66" y1="318" x2="644" y2="318" stroke="#4d4942" stroke-width="1"></line><line x1="66" y1="28" x2="66" y2="318" stroke="#d3cec5" stroke-width="1"></line><line x1="66" y1="318" x2="66" y2="323" stroke="#4d4942" stroke-width="1"></line><text x="66" y="342" text-anchor="middle" fill="#514c45" font-size="12.5" font-weight="500">1</text> <line x1="197.2695145882545" y1="28" x2="197.2695145882545" y2="318" stroke="#d3cec5" stroke-width="1"></line><line x1="197.2695145882545" y1="318" x2="197.2695145882545" y2="323" stroke="#4d4942" stroke-width="1"></line><text x="197.2695145882545" y="342" text-anchor="middle" fill="#514c45" font-size="12.5" font-weight="500">10</text> <line x1="328.539029176509" y1="28" x2="328.539029176509" y2="318" stroke="#d3cec5" stroke-width="1"></line><line x1="328.539029176509" y1="318" x2="328.539029176509" y2="323" stroke="#4d4942" stroke-width="1"></line><text x="328.539029176509" y="342" text-anchor="middle" fill="#514c45" font-size="12.5" font-weight="500">100</text> <line x1="459.80854376476356" y1="28" x2="459.80854376476356" y2="318" stroke="#d3cec5" stroke-width="1"></line><line x1="459.80854376476356" y1="318" x2="459.80854376476356" y2="323" stroke="#4d4942" stroke-width="1"></line><text x="459.80854376476356" y="342" text-anchor="middle" fill="#514c45" font-size="12.5" font-weight="500">1k</text> <line x1="591.078058353018" y1="28" x2="591.078058353018" y2="318" stroke="#d3cec5" stroke-width="1"></line><line x1="591.078058353018" y1="318" x2="591.078058353018" y2="323" stroke="#4d4942" stroke-width="1"></line><text x="591.078058353018" y="342" text-anchor="middle" fill="#514c45" font-size="12.5" font-weight="500">10k</text> <line x1="644" y1="28" x2="644" y2="318" stroke="#d3cec5" stroke-width="1"></line><line x1="644" y1="318" x2="644" y2="323" stroke="#4d4942" stroke-width="1"></line><text x="644" y="342" text-anchor="middle" fill="#514c45" font-size="12.5" font-weight="500">25.3k</text> <text x="355" y="374" text-anchor="middle" fill="#514c45" font-size="13.5" font-weight="500">largest clusters included</text> <line x1="66" y1="28" x2="66" y2="318" stroke="#4d4942" stroke-width="1"></line><line x1="66" y1="318" x2="644" y2="318" stroke="#d3cec5" stroke-width="1"></line><line x1="61" y1="318" x2="66" y2="318" stroke="#4d4942" stroke-width="1"></line><text x="56" y="323" text-anchor="end" fill="#514c45" font-size="12.5" font-weight="500">0%</text> <line x1="66" y1="245.5" x2="644" y2="245.5" stroke="#d3cec5" stroke-width="1"></line><line x1="61" y1="245.5" x2="66" y2="245.5" stroke="#4d4942" stroke-width="1"></line><text x="56" y="250.5" text-anchor="end" fill="#514c45" font-size="12.5" font-weight="500">25%</text> <line x1="66" y1="173" x2="644" y2="173" stroke="#d3cec5" stroke-width="1"></line><line x1="61" y1="173" x2="66" y2="173" stroke="#4d4942" stroke-width="1"></line><text x="56" y="178" text-anchor="end" fill="#514c45" font-size="12.5" font-weight="500">50%</text> <line x1="66" y1="100.5" x2="644" y2="100.5" stroke="#d3cec5" stroke-width="1"></line><line x1="61" y1="100.5" x2="66" y2="100.5" stroke="#4d4942" stroke-width="1"></line><text x="56" y="105.5" text-anchor="end" fill="#514c45" font-size="12.5" font-weight="500">75%</text> <line x1="66" y1="28" x2="644" y2="28" stroke="#d3cec5" stroke-width="1"></line><line x1="61" y1="28" x2="66" y2="28" stroke="#4d4942" stroke-width="1"></line><text x="56" y="33" text-anchor="end" fill="#514c45" font-size="12.5" font-weight="500">100%</text> <text x="14" y="173" text-anchor="middle" fill="#514c45" font-size="13.5" font-weight="500" transform="rotate(-90 14 173)">fragment mass</text> <path d="M66.00,311.82 L105.52,308.70 L128.63,306.02 L145.03,303.89 L157.75,301.99 L168.15,300.16 L176.94,298.73 L184.55,297.31 L191.26,295.89 L197.27,294.50 L202.70,293.15 L207.66,291.88 L216.45,289.36 L220.38,288.22 L224.06,287.10 L227.52,286.00 L230.78,284.91 L236.79,282.79 L239.57,281.76 L242.22,280.73 L247.18,278.69 L249.51,277.70 L253.89,275.75 L257.97,273.96 L259.90,273.08 L263.58,271.50 L267.04,269.99 L270.30,268.51 L273.38,267.05 L276.30,265.61 L279.08,264.20 L281.74,262.82 L284.27,261.46 L286.70,260.15 L289.02,258.86 L291.26,257.62 L294.46,255.81 L296.49,254.64 L299.42,252.91 L301.29,251.77 L303.98,250.11 L305.71,249.07 L308.21,247.55 L310.60,246.05 L312.14,245.06 L314.37,243.61 L316.53,242.20 L318.60,240.81 L320.60,239.43 L322.53,238.08 L324.40,236.75 L326.21,235.43 L327.97,234.15 L330.22,232.48 L331.86,231.24 L333.45,230.03 L335.51,228.43 L337.00,227.25 L338.93,225.71 L340.34,224.59 L342.17,223.13 L343.93,221.72 L345.65,220.33 L346.90,219.29 L348.53,217.94 L350.11,216.60 L351.65,215.28 L353.15,213.97 L354.62,212.70 L356.04,211.45 L357.77,209.93 L359.12,208.76 L360.44,207.61 L362.05,206.20 L363.30,205.09 L364.83,203.72 L366.02,202.64 L367.48,201.32 L368.62,200.26 L370.02,198.96 L371.38,197.70 L372.71,196.48 L374.00,195.28 L375.27,194.09 L376.52,192.91 L377.73,191.76 L378.92,190.62 L380.09,189.49 L381.23,188.39 L382.57,187.09 L383.67,186.02 L384.74,184.97 L386.00,183.74 L387.03,182.74 L388.25,181.54 L389.43,180.37 L390.41,179.42 L391.55,178.29 L392.67,177.17 L393.77,176.08 L394.85,175.00 L395.91,173.94 L396.95,172.91 L397.97,171.89 L398.97,170.89 L399.96,169.91 L401.09,168.77 L402.04,167.81 L403.13,166.72 L404.04,165.79 L405.10,164.73 L405.98,163.84 L407.00,162.82 L408.00,161.81 L408.84,160.97 L409.81,160.00 L410.76,159.05 L411.69,158.11 L412.61,157.19 L413.52,156.28 L414.41,155.39 L415.29,154.52 L416.28,153.54 L417.13,152.69 L417.97,151.86 L418.91,150.91 L419.72,150.09 L420.63,149.16 L421.42,148.36 L422.31,147.47 L423.18,146.58 L424.04,145.72 L424.89,144.86 L425.62,144.12 L426.45,143.29 L427.26,142.48 L428.16,141.57 L428.95,140.78 L429.73,139.99 L430.50,139.22 L431.25,138.46 L432.09,137.61 L432.83,136.87 L433.65,136.05 L434.37,135.33 L435.16,134.54 L435.95,133.76 L436.72,132.99 L437.40,132.31 L438.16,131.55 L438.90,130.80 L439.64,130.07 L440.36,129.35 L441.08,128.64 L441.87,127.86 L442.57,127.17 L443.26,126.48 L443.94,125.81 L444.69,125.07 L445.35,124.42 L446.08,123.70 L446.80,123.00 L447.44,122.38 L448.15,121.69 L448.84,121.02 L449.53,120.35 L450.21,119.70 L450.88,119.06 L451.54,118.42 L452.20,117.80 L452.84,117.19 L453.48,116.58 L454.12,116.00 L454.81,115.36 L455.43,114.79 L456.10,114.16 L456.70,113.61 L457.36,113.00 L457.95,112.45 L458.60,111.86 L459.24,111.28 L459.87,110.70 L460.49,110.13 L461.10,109.57 L461.71,109.01 L462.32,108.46 L462.91,107.91 L463.51,107.38 L464.09,106.85 L464.72,106.29 L465.29,105.78 L465.91,105.23 L466.47,104.73 L467.08,104.20 L467.63,103.71 L468.22,103.19 L468.81,102.67 L469.39,102.16 L469.96,101.65 L470.53,101.15 L471.10,100.66 L471.66,100.17 L472.21,99.69 L472.76,99.22 L473.30,98.75 L473.88,98.25 L474.41,97.79 L474.98,97.30 L475.51,96.86 L476.07,96.38 L476.58,95.95 L477.13,95.50 L477.67,95.05 L478.21,94.60 L478.75,94.17 L479.28,93.74 L479.80,93.31 L480.32,92.89 L480.83,92.47 L481.34,92.07 L481.89,91.63 L482.39,91.23 L482.89,90.84 L483.42,90.42 L483.90,90.03 L484.42,89.62 L484.94,89.22 L485.42,88.84 L485.92,88.44 L486.42,88.05 L486.92,87.66 L487.42,87.27 L487.91,86.89 L488.39,86.51 L488.87,86.14 L489.35,85.77 L489.86,85.38 L490.33,85.01 L490.83,84.63 L491.29,84.28 L491.78,83.90 L492.23,83.56 L492.71,83.19 L493.19,82.83 L493.63,82.50 L494.10,82.15 L494.57,81.81 L495.03,81.47 L495.49,81.13 L495.95,80.80 L496.43,80.45 L496.88,80.13 L497.32,79.81 L497.79,79.47 L498.23,79.15 L498.69,78.82 L499.12,78.51 L499.58,78.19 L500.03,77.87 L500.45,77.57 L500.90,77.26 L501.34,76.95 L501.78,76.64 L502.21,76.34 L502.65,76.04 L503.08,75.74 L503.50,75.45 L503.95,75.14 L504.37,74.86 L504.81,74.56 L505.22,74.28 L505.66,73.98 L506.06,73.71 L506.49,73.42 L506.92,73.14 L507.32,72.87 L507.74,72.60 L508.15,72.32 L508.57,72.05 L508.98,71.78 L509.39,71.52 L509.81,71.23 L510.22,70.97 L510.61,70.71 L511.01,70.46 L511.43,70.19 L511.82,69.93 L512.23,69.67 L512.64,69.41 L513.02,69.17 L513.42,68.91 L513.82,68.66 L514.22,68.41 L514.61,68.16 L515.00,67.91 L515.39,67.67 L515.78,67.43 L516.16,67.20 L516.56,66.95 L516.94,66.72 L517.31,66.49 L517.71,66.26 L518.08,66.03 L518.47,65.80 L518.85,65.57 L519.21,65.36 L519.60,65.14 L519.97,64.91 L520.35,64.70 L520.72,64.48 L521.09,64.26 L521.46,64.05 L521.83,63.84 L522.21,63.62 L522.57,63.41 L522.93,63.21 L523.31,62.99 L523.66,62.79 L524.03,62.59 L524.40,62.38 L524.75,62.18 L525.11,61.98 L525.47,61.78 L525.83,61.58 L526.19,61.38 L526.55,61.19 L526.90,61.00 L527.25,60.81 L527.61,60.61 L527.96,60.42 L528.30,60.24 L528.66,60.05 L529.00,59.87 L529.36,59.68 L529.69,59.50 L530.04,59.32 L530.39,59.14 L530.74,58.96 L531.08,58.78 L531.42,58.60 L531.76,58.43 L532.10,58.26 L532.44,58.09 L532.77,57.92 L533.10,57.75 L533.45,57.57 L533.78,57.41 L534.12,57.24 L534.44,57.07 L534.78,56.91 L535.12,56.74 L535.43,56.58 L535.77,56.42 L536.10,56.26 L536.42,56.10 L536.75,55.94 L537.07,55.78 L537.40,55.62 L537.73,55.46 L538.05,55.31 L538.37,55.15 L538.70,55.00 L539.01,54.85 L539.34,54.69 L539.65,54.55 L539.97,54.39 L540.29,54.24 L540.61,54.09 L540.93,53.95 L541.23,53.81 L541.54,53.66 L541.87,53.51 L542.18,53.37 L542.48,53.23 L542.79,53.09 L543.11,52.94 L543.41,52.80 L543.71,52.67 L544.03,52.53 L544.34,52.38 L544.64,52.25 L544.94,52.11 L545.25,51.98 L545.56,51.84 L545.86,51.71 L546.16,51.58 L546.46,51.45 L546.76,51.32 L547.06,51.19 L547.36,51.06 L547.66,50.93 L547.95,50.81 L548.25,50.68 L548.54,50.56 L548.84,50.43 L549.14,50.31 L549.42,50.18 L549.72,50.06 L550.01,49.94 L550.31,49.82 L550.60,49.70 L550.89,49.58 L551.17,49.46 L551.46,49.34 L551.76,49.22 L552.04,49.11 L552.33,48.99 L552.61,48.88 L552.90,48.76 L553.18,48.65 L553.47,48.54 L553.75,48.42 L554.03,48.31 L554.31,48.20 L554.59,48.09 L554.87,47.98 L555.15,47.87 L555.44,47.76 L555.72,47.65 L555.99,47.54 L556.27,47.44 L556.55,47.33 L556.82,47.23 L557.10,47.12 L557.38,47.01 L557.64,46.91 L557.92,46.80 L558.20,46.70 L558.47,46.60 L558.74,46.49 L559.01,46.39 L559.28,46.29 L559.55,46.19 L559.82,46.09 L560.09,45.99 L560.36,45.89 L560.62,45.80 L560.89,45.70 L561.15,45.60 L561.42,45.50 L561.69,45.41 L561.96,45.31 L562.21,45.22 L562.48,45.13 L562.74,45.03 L563.00,44.94 L563.26,44.85 L563.53,44.75 L563.79,44.66 L564.05,44.57 L564.31,44.48 L564.57,44.39 L564.83,44.30 L565.08,44.22 L565.34,44.13 L565.60,44.04 L565.85,43.95 L566.11,43.87 L566.36,43.78 L566.62,43.69 L566.87,43.61 L567.12,43.52 L567.37,43.44 L567.63,43.35 L567.88,43.27 L568.13,43.19 L568.38,43.10 L568.63,43.02 L568.88,42.94 L569.13,42.85 L569.38,42.77 L569.63,42.69 L569.87,42.61 L570.12,42.53 L570.37,42.45 L570.61,42.37 L570.86,42.29 L571.11,42.21 L571.35,42.14 L571.59,42.06 L571.84,41.99 L572.08,41.91 L572.33,41.83 L572.56,41.76 L572.81,41.68 L573.05,41.60 L573.29,41.53 L573.53,41.46 L573.77,41.38 L574.00,41.31 L574.25,41.24 L574.49,41.16 L574.72,41.09 L574.96,41.02 L575.20,40.94 L575.43,40.87 L575.67,40.80 L575.90,40.73 L576.14,40.66 L576.37,40.59 L576.61,40.52 L576.84,40.45 L577.07,40.38 L577.31,40.31 L577.54,40.24 L577.77,40.18 L578.00,40.11 L578.24,40.04 L578.46,39.98 L578.69,39.91 L578.92,39.84 L579.15,39.78 L579.38,39.71 L579.61,39.64 L579.83,39.58 L580.06,39.52 L580.29,39.45 L580.52,39.39 L580.74,39.33 L580.97,39.26 L581.19,39.20 L581.42,39.13 L581.64,39.07 L581.87,39.01 L582.09,38.94 L582.31,38.88 L582.54,38.82 L582.76,38.76 L582.98,38.70 L583.20,38.64 L583.43,38.58 L583.65,38.52 L583.86,38.46 L584.09,38.40 L584.31,38.34 L584.52,38.28 L584.74,38.23 L584.96,38.17 L585.18,38.11 L585.39,38.06 L585.61,38.00 L585.83,37.95 L586.04,37.89 L586.26,37.83 L586.48,37.78 L586.69,37.72 L586.90,37.66 L587.12,37.61 L587.33,37.55 L587.55,37.50 L587.76,37.44 L587.97,37.39 L588.18,37.34 L588.40,37.29 L588.61,37.24 L588.82,37.18 L589.04,37.13 L589.24,37.08 L589.45,37.02 L589.66,36.97 L589.87,36.92 L590.08,36.86 L590.29,36.81 L590.50,36.76 L590.71,36.71 L590.91,36.67 L591.12,36.62 L591.33,36.57 L591.54,36.52 L591.74,36.47 L591.95,36.42 L592.15,36.37 L592.36,36.33 L592.56,36.28 L592.77,36.23 L592.97,36.18 L593.18,36.13 L593.38,36.08 L593.58,36.03 L593.78,35.99 L593.98,35.94 L594.19,35.90 L594.39,35.85 L594.59,35.81 L594.79,35.76 L594.99,35.72 L595.20,35.67 L595.39,35.63 L595.59,35.59 L595.79,35.54 L595.99,35.50 L596.19,35.45 L596.39,35.41 L596.59,35.36 L596.79,35.31 L596.98,35.27 L597.18,35.22 L597.38,35.18 L597.57,35.14 L597.77,35.10 L597.96,35.06 L598.16,35.02 L598.35,34.98 L598.55,34.94 L598.74,34.90 L598.94,34.86 L599.13,34.82 L599.33,34.78 L599.52,34.73 L599.71,34.69 L599.91,34.65 L600.10,34.61 L600.29,34.57 L600.48,34.53 L600.67,34.49 L600.86,34.45 L601.05,34.41 L601.24,34.37 L601.43,34.32 L601.62,34.28 L601.81,34.24 L602.00,34.21 L602.19,34.17 L602.38,34.14 L602.57,34.10 L602.76,34.07 L602.94,34.03 L603.13,33.99 L603.32,33.96 L603.51,33.92 L603.69,33.89 L603.88,33.85 L604.06,33.81 L604.25,33.78 L604.44,33.74 L604.62,33.70 L604.81,33.67 L604.99,33.63 L605.17,33.59 L605.36,33.56 L605.54,33.52 L605.73,33.48 L605.91,33.45 L606.09,33.41 L606.28,33.37 L606.46,33.34 L606.64,33.30 L606.82,33.26 L607.00,33.23 L607.19,33.20 L607.37,33.17 L607.55,33.14 L607.72,33.11 L607.91,33.08 L608.09,33.05 L608.27,33.01 L608.44,32.98 L608.62,32.95 L608.80,32.92 L608.98,32.89 L609.16,32.86 L609.34,32.82 L609.51,32.79 L609.70,32.76 L609.87,32.73 L610.05,32.70 L610.22,32.66 L610.40,32.63 L610.58,32.60 L610.75,32.57 L610.93,32.54 L611.10,32.50 L611.28,32.47 L611.45,32.44 L611.63,32.41 L611.80,32.37 L611.98,32.34 L612.15,32.31 L612.32,32.28 L612.50,32.24 L612.67,32.21 L612.84,32.18 L613.02,32.15 L613.19,32.12 L613.36,32.10 L613.53,32.07 L613.70,32.04 L613.88,32.02 L614.05,31.99 L614.22,31.97 L614.39,31.94 L614.56,31.91 L614.73,31.88 L614.90,31.86 L615.07,31.83 L615.24,31.80 L615.41,31.78 L615.58,31.75 L615.75,31.72 L615.92,31.70 L616.08,31.67 L616.25,31.64 L616.42,31.62 L616.59,31.59 L616.75,31.56 L616.92,31.53 L617.09,31.51 L617.25,31.48 L617.42,31.45 L617.59,31.42 L617.75,31.40 L617.92,31.37 L618.08,31.34 L618.25,31.31 L618.41,31.29 L618.58,31.26 L618.74,31.23 L618.91,31.20 L619.07,31.18 L619.24,31.15 L619.40,31.12 L619.56,31.09 L619.72,31.07 L619.89,31.04 L620.05,31.01 L620.21,30.99 L620.38,30.97 L620.54,30.95 L620.70,30.93 L620.86,30.91 L621.02,30.88 L621.18,30.86 L621.35,30.84 L621.51,30.82 L621.67,30.80 L621.83,30.78 L621.99,30.76 L622.15,30.73 L622.31,30.71 L622.46,30.69 L622.63,30.67 L622.79,30.65 L622.94,30.63 L623.10,30.61 L623.26,30.58 L623.42,30.56 L623.58,30.54 L623.74,30.52 L623.89,30.50 L624.05,30.48 L624.21,30.45 L624.36,30.43 L624.52,30.41 L624.68,30.39 L624.83,30.37 L624.99,30.34 L625.15,30.32 L625.30,30.30 L625.46,30.28 L625.61,30.26 L625.77,30.23 L625.92,30.21 L626.08,30.19 L626.23,30.17 L626.39,30.14 L626.54,30.12 L626.70,30.10 L626.85,30.08 L627.00,30.06 L627.15,30.03 L627.31,30.01 L627.46,29.99 L627.61,29.97 L627.77,29.94 L627.92,29.92 L628.07,29.90 L628.22,29.88 L628.38,29.85 L628.53,29.83 L628.68,29.81 L628.83,29.78 L628.98,29.76 L629.13,29.74 L629.28,29.72 L629.43,29.69 L629.58,29.67 L629.73,29.66 L629.88,29.64 L630.03,29.63 L630.18,29.61 L630.33,29.59 L630.48,29.58 L630.63,29.56 L630.78,29.55 L630.93,29.53 L631.08,29.52 L631.22,29.50 L631.37,29.49 L631.52,29.47 L631.67,29.46 L631.82,29.44 L631.96,29.42 L632.11,29.41 L632.26,29.39 L632.40,29.38 L632.55,29.36 L632.70,29.35 L632.84,29.33 L632.99,29.31 L633.13,29.30 L633.28,29.28 L633.43,29.27 L633.57,29.25 L633.72,29.23 L633.86,29.22 L634.01,29.20 L634.15,29.19 L634.30,29.17 L634.44,29.15 L634.58,29.14 L634.73,29.12 L634.87,29.11 L635.02,29.09 L635.16,29.07 L635.30,29.06 L635.44,29.04 L635.59,29.03 L635.73,29.01 L635.87,28.99 L636.01,28.98 L636.16,28.96 L636.30,28.95 L636.44,28.93 L636.58,28.91 L636.73,28.90 L636.87,28.88 L637.01,28.86 L637.15,28.85 L637.29,28.83 L637.43,28.81 L637.57,28.80 L637.71,28.78 L637.85,28.76 L637.99,28.75 L638.13,28.73 L638.27,28.72 L638.41,28.70 L638.55,28.68 L638.69,28.67 L638.83,28.65 L638.97,28.63 L639.11,28.62 L639.25,28.60 L639.38,28.58 L639.52,28.56 L639.66,28.55 L639.80,28.53 L639.94,28.51 L640.07,28.50 L640.21,28.48 L640.35,28.46 L640.49,28.45 L640.62,28.43 L640.76,28.41 L640.90,28.40 L641.03,28.38 L641.17,28.36 L641.31,28.35 L641.44,28.33 L641.58,28.31 L641.72,28.29 L641.85,28.28 L641.99,28.26 L642.12,28.24 L642.26,28.23 L642.39,28.21 L642.53,28.19 L642.66,28.17 L642.80,28.16 L642.93,28.14 L643.06,28.12 L643.20,28.10 L643.33,28.09 L643.47,28.07 L643.60,28.05 L643.73,28.03 L643.87,28.02 L644.00,28.00 L644.00,318 L66,318 Z" fill="rgba(47, 111, 115, 0.1)" stroke="none"></path><path d="M66.00,311.82 L105.52,308.70 L128.63,306.02 L145.03,303.89 L157.75,301.99 L168.15,300.16 L176.94,298.73 L184.55,297.31 L191.26,295.89 L197.27,294.50 L202.70,293.15 L207.66,291.88 L216.45,289.36 L220.38,288.22 L224.06,287.10 L227.52,286.00 L230.78,284.91 L236.79,282.79 L239.57,281.76 L242.22,280.73 L247.18,278.69 L249.51,277.70 L253.89,275.75 L257.97,273.96 L259.90,273.08 L263.58,271.50 L267.04,269.99 L270.30,268.51 L273.38,267.05 L276.30,265.61 L279.08,264.20 L281.74,262.82 L284.27,261.46 L286.70,260.15 L289.02,258.86 L291.26,257.62 L294.46,255.81 L296.49,254.64 L299.42,252.91 L301.29,251.77 L303.98,250.11 L305.71,249.07 L308.21,247.55 L310.60,246.05 L312.14,245.06 L314.37,243.61 L316.53,242.20 L318.60,240.81 L320.60,239.43 L322.53,238.08 L324.40,236.75 L326.21,235.43 L327.97,234.15 L330.22,232.48 L331.86,231.24 L333.45,230.03 L335.51,228.43 L337.00,227.25 L338.93,225.71 L340.34,224.59 L342.17,223.13 L343.93,221.72 L345.65,220.33 L346.90,219.29 L348.53,217.94 L350.11,216.60 L351.65,215.28 L353.15,213.97 L354.62,212.70 L356.04,211.45 L357.77,209.93 L359.12,208.76 L360.44,207.61 L362.05,206.20 L363.30,205.09 L364.83,203.72 L366.02,202.64 L367.48,201.32 L368.62,200.26 L370.02,198.96 L371.38,197.70 L372.71,196.48 L374.00,195.28 L375.27,194.09 L376.52,192.91 L377.73,191.76 L378.92,190.62 L380.09,189.49 L381.23,188.39 L382.57,187.09 L383.67,186.02 L384.74,184.97 L386.00,183.74 L387.03,182.74 L388.25,181.54 L389.43,180.37 L390.41,179.42 L391.55,178.29 L392.67,177.17 L393.77,176.08 L394.85,175.00 L395.91,173.94 L396.95,172.91 L397.97,171.89 L398.97,170.89 L399.96,169.91 L401.09,168.77 L402.04,167.81 L403.13,166.72 L404.04,165.79 L405.10,164.73 L405.98,163.84 L407.00,162.82 L408.00,161.81 L408.84,160.97 L409.81,160.00 L410.76,159.05 L411.69,158.11 L412.61,157.19 L413.52,156.28 L414.41,155.39 L415.29,154.52 L416.28,153.54 L417.13,152.69 L417.97,151.86 L418.91,150.91 L419.72,150.09 L420.63,149.16 L421.42,148.36 L422.31,147.47 L423.18,146.58 L424.04,145.72 L424.89,144.86 L425.62,144.12 L426.45,143.29 L427.26,142.48 L428.16,141.57 L428.95,140.78 L429.73,139.99 L430.50,139.22 L431.25,138.46 L432.09,137.61 L432.83,136.87 L433.65,136.05 L434.37,135.33 L435.16,134.54 L435.95,133.76 L436.72,132.99 L437.40,132.31 L438.16,131.55 L438.90,130.80 L439.64,130.07 L440.36,129.35 L441.08,128.64 L441.87,127.86 L442.57,127.17 L443.26,126.48 L443.94,125.81 L444.69,125.07 L445.35,124.42 L446.08,123.70 L446.80,123.00 L447.44,122.38 L448.15,121.69 L448.84,121.02 L449.53,120.35 L450.21,119.70 L450.88,119.06 L451.54,118.42 L452.20,117.80 L452.84,117.19 L453.48,116.58 L454.12,116.00 L454.81,115.36 L455.43,114.79 L456.10,114.16 L456.70,113.61 L457.36,113.00 L457.95,112.45 L458.60,111.86 L459.24,111.28 L459.87,110.70 L460.49,110.13 L461.10,109.57 L461.71,109.01 L462.32,108.46 L462.91,107.91 L463.51,107.38 L464.09,106.85 L464.72,106.29 L465.29,105.78 L465.91,105.23 L466.47,104.73 L467.08,104.20 L467.63,103.71 L468.22,103.19 L468.81,102.67 L469.39,102.16 L469.96,101.65 L470.53,101.15 L471.10,100.66 L471.66,100.17 L472.21,99.69 L472.76,99.22 L473.30,98.75 L473.88,98.25 L474.41,97.79 L474.98,97.30 L475.51,96.86 L476.07,96.38 L476.58,95.95 L477.13,95.50 L477.67,95.05 L478.21,94.60 L478.75,94.17 L479.28,93.74 L479.80,93.31 L480.32,92.89 L480.83,92.47 L481.34,92.07 L481.89,91.63 L482.39,91.23 L482.89,90.84 L483.42,90.42 L483.90,90.03 L484.42,89.62 L484.94,89.22 L485.42,88.84 L485.92,88.44 L486.42,88.05 L486.92,87.66 L487.42,87.27 L487.91,86.89 L488.39,86.51 L488.87,86.14 L489.35,85.77 L489.86,85.38 L490.33,85.01 L490.83,84.63 L491.29,84.28 L491.78,83.90 L492.23,83.56 L492.71,83.19 L493.19,82.83 L493.63,82.50 L494.10,82.15 L494.57,81.81 L495.03,81.47 L495.49,81.13 L495.95,80.80 L496.43,80.45 L496.88,80.13 L497.32,79.81 L497.79,79.47 L498.23,79.15 L498.69,78.82 L499.12,78.51 L499.58,78.19 L500.03,77.87 L500.45,77.57 L500.90,77.26 L501.34,76.95 L501.78,76.64 L502.21,76.34 L502.65,76.04 L503.08,75.74 L503.50,75.45 L503.95,75.14 L504.37,74.86 L504.81,74.56 L505.22,74.28 L505.66,73.98 L506.06,73.71 L506.49,73.42 L506.92,73.14 L507.32,72.87 L507.74,72.60 L508.15,72.32 L508.57,72.05 L508.98,71.78 L509.39,71.52 L509.81,71.23 L510.22,70.97 L510.61,70.71 L511.01,70.46 L511.43,70.19 L511.82,69.93 L512.23,69.67 L512.64,69.41 L513.02,69.17 L513.42,68.91 L513.82,68.66 L514.22,68.41 L514.61,68.16 L515.00,67.91 L515.39,67.67 L515.78,67.43 L516.16,67.20 L516.56,66.95 L516.94,66.72 L517.31,66.49 L517.71,66.26 L518.08,66.03 L518.47,65.80 L518.85,65.57 L519.21,65.36 L519.60,65.14 L519.97,64.91 L520.35,64.70 L520.72,64.48 L521.09,64.26 L521.46,64.05 L521.83,63.84 L522.21,63.62 L522.57,63.41 L522.93,63.21 L523.31,62.99 L523.66,62.79 L524.03,62.59 L524.40,62.38 L524.75,62.18 L525.11,61.98 L525.47,61.78 L525.83,61.58 L526.19,61.38 L526.55,61.19 L526.90,61.00 L527.25,60.81 L527.61,60.61 L527.96,60.42 L528.30,60.24 L528.66,60.05 L529.00,59.87 L529.36,59.68 L529.69,59.50 L530.04,59.32 L530.39,59.14 L530.74,58.96 L531.08,58.78 L531.42,58.60 L531.76,58.43 L532.10,58.26 L532.44,58.09 L532.77,57.92 L533.10,57.75 L533.45,57.57 L533.78,57.41 L534.12,57.24 L534.44,57.07 L534.78,56.91 L535.12,56.74 L535.43,56.58 L535.77,56.42 L536.10,56.26 L536.42,56.10 L536.75,55.94 L537.07,55.78 L537.40,55.62 L537.73,55.46 L538.05,55.31 L538.37,55.15 L538.70,55.00 L539.01,54.85 L539.34,54.69 L539.65,54.55 L539.97,54.39 L540.29,54.24 L540.61,54.09 L540.93,53.95 L541.23,53.81 L541.54,53.66 L541.87,53.51 L542.18,53.37 L542.48,53.23 L542.79,53.09 L543.11,52.94 L543.41,52.80 L543.71,52.67 L544.03,52.53 L544.34,52.38 L544.64,52.25 L544.94,52.11 L545.25,51.98 L545.56,51.84 L545.86,51.71 L546.16,51.58 L546.46,51.45 L546.76,51.32 L547.06,51.19 L547.36,51.06 L547.66,50.93 L547.95,50.81 L548.25,50.68 L548.54,50.56 L548.84,50.43 L549.14,50.31 L549.42,50.18 L549.72,50.06 L550.01,49.94 L550.31,49.82 L550.60,49.70 L550.89,49.58 L551.17,49.46 L551.46,49.34 L551.76,49.22 L552.04,49.11 L552.33,48.99 L552.61,48.88 L552.90,48.76 L553.18,48.65 L553.47,48.54 L553.75,48.42 L554.03,48.31 L554.31,48.20 L554.59,48.09 L554.87,47.98 L555.15,47.87 L555.44,47.76 L555.72,47.65 L555.99,47.54 L556.27,47.44 L556.55,47.33 L556.82,47.23 L557.10,47.12 L557.38,47.01 L557.64,46.91 L557.92,46.80 L558.20,46.70 L558.47,46.60 L558.74,46.49 L559.01,46.39 L559.28,46.29 L559.55,46.19 L559.82,46.09 L560.09,45.99 L560.36,45.89 L560.62,45.80 L560.89,45.70 L561.15,45.60 L561.42,45.50 L561.69,45.41 L561.96,45.31 L562.21,45.22 L562.48,45.13 L562.74,45.03 L563.00,44.94 L563.26,44.85 L563.53,44.75 L563.79,44.66 L564.05,44.57 L564.31,44.48 L564.57,44.39 L564.83,44.30 L565.08,44.22 L565.34,44.13 L565.60,44.04 L565.85,43.95 L566.11,43.87 L566.36,43.78 L566.62,43.69 L566.87,43.61 L567.12,43.52 L567.37,43.44 L567.63,43.35 L567.88,43.27 L568.13,43.19 L568.38,43.10 L568.63,43.02 L568.88,42.94 L569.13,42.85 L569.38,42.77 L569.63,42.69 L569.87,42.61 L570.12,42.53 L570.37,42.45 L570.61,42.37 L570.86,42.29 L571.11,42.21 L571.35,42.14 L571.59,42.06 L571.84,41.99 L572.08,41.91 L572.33,41.83 L572.56,41.76 L572.81,41.68 L573.05,41.60 L573.29,41.53 L573.53,41.46 L573.77,41.38 L574.00,41.31 L574.25,41.24 L574.49,41.16 L574.72,41.09 L574.96,41.02 L575.20,40.94 L575.43,40.87 L575.67,40.80 L575.90,40.73 L576.14,40.66 L576.37,40.59 L576.61,40.52 L576.84,40.45 L577.07,40.38 L577.31,40.31 L577.54,40.24 L577.77,40.18 L578.00,40.11 L578.24,40.04 L578.46,39.98 L578.69,39.91 L578.92,39.84 L579.15,39.78 L579.38,39.71 L579.61,39.64 L579.83,39.58 L580.06,39.52 L580.29,39.45 L580.52,39.39 L580.74,39.33 L580.97,39.26 L581.19,39.20 L581.42,39.13 L581.64,39.07 L581.87,39.01 L582.09,38.94 L582.31,38.88 L582.54,38.82 L582.76,38.76 L582.98,38.70 L583.20,38.64 L583.43,38.58 L583.65,38.52 L583.86,38.46 L584.09,38.40 L584.31,38.34 L584.52,38.28 L584.74,38.23 L584.96,38.17 L585.18,38.11 L585.39,38.06 L585.61,38.00 L585.83,37.95 L586.04,37.89 L586.26,37.83 L586.48,37.78 L586.69,37.72 L586.90,37.66 L587.12,37.61 L587.33,37.55 L587.55,37.50 L587.76,37.44 L587.97,37.39 L588.18,37.34 L588.40,37.29 L588.61,37.24 L588.82,37.18 L589.04,37.13 L589.24,37.08 L589.45,37.02 L589.66,36.97 L589.87,36.92 L590.08,36.86 L590.29,36.81 L590.50,36.76 L590.71,36.71 L590.91,36.67 L591.12,36.62 L591.33,36.57 L591.54,36.52 L591.74,36.47 L591.95,36.42 L592.15,36.37 L592.36,36.33 L592.56,36.28 L592.77,36.23 L592.97,36.18 L593.18,36.13 L593.38,36.08 L593.58,36.03 L593.78,35.99 L593.98,35.94 L594.19,35.90 L594.39,35.85 L594.59,35.81 L594.79,35.76 L594.99,35.72 L595.20,35.67 L595.39,35.63 L595.59,35.59 L595.79,35.54 L595.99,35.50 L596.19,35.45 L596.39,35.41 L596.59,35.36 L596.79,35.31 L596.98,35.27 L597.18,35.22 L597.38,35.18 L597.57,35.14 L597.77,35.10 L597.96,35.06 L598.16,35.02 L598.35,34.98 L598.55,34.94 L598.74,34.90 L598.94,34.86 L599.13,34.82 L599.33,34.78 L599.52,34.73 L599.71,34.69 L599.91,34.65 L600.10,34.61 L600.29,34.57 L600.48,34.53 L600.67,34.49 L600.86,34.45 L601.05,34.41 L601.24,34.37 L601.43,34.32 L601.62,34.28 L601.81,34.24 L602.00,34.21 L602.19,34.17 L602.38,34.14 L602.57,34.10 L602.76,34.07 L602.94,34.03 L603.13,33.99 L603.32,33.96 L603.51,33.92 L603.69,33.89 L603.88,33.85 L604.06,33.81 L604.25,33.78 L604.44,33.74 L604.62,33.70 L604.81,33.67 L604.99,33.63 L605.17,33.59 L605.36,33.56 L605.54,33.52 L605.73,33.48 L605.91,33.45 L606.09,33.41 L606.28,33.37 L606.46,33.34 L606.64,33.30 L606.82,33.26 L607.00,33.23 L607.19,33.20 L607.37,33.17 L607.55,33.14 L607.72,33.11 L607.91,33.08 L608.09,33.05 L608.27,33.01 L608.44,32.98 L608.62,32.95 L608.80,32.92 L608.98,32.89 L609.16,32.86 L609.34,32.82 L609.51,32.79 L609.70,32.76 L609.87,32.73 L610.05,32.70 L610.22,32.66 L610.40,32.63 L610.58,32.60 L610.75,32.57 L610.93,32.54 L611.10,32.50 L611.28,32.47 L611.45,32.44 L611.63,32.41 L611.80,32.37 L611.98,32.34 L612.15,32.31 L612.32,32.28 L612.50,32.24 L612.67,32.21 L612.84,32.18 L613.02,32.15 L613.19,32.12 L613.36,32.10 L613.53,32.07 L613.70,32.04 L613.88,32.02 L614.05,31.99 L614.22,31.97 L614.39,31.94 L614.56,31.91 L614.73,31.88 L614.90,31.86 L615.07,31.83 L615.24,31.80 L615.41,31.78 L615.58,31.75 L615.75,31.72 L615.92,31.70 L616.08,31.67 L616.25,31.64 L616.42,31.62 L616.59,31.59 L616.75,31.56 L616.92,31.53 L617.09,31.51 L617.25,31.48 L617.42,31.45 L617.59,31.42 L617.75,31.40 L617.92,31.37 L618.08,31.34 L618.25,31.31 L618.41,31.29 L618.58,31.26 L618.74,31.23 L618.91,31.20 L619.07,31.18 L619.24,31.15 L619.40,31.12 L619.56,31.09 L619.72,31.07 L619.89,31.04 L620.05,31.01 L620.21,30.99 L620.38,30.97 L620.54,30.95 L620.70,30.93 L620.86,30.91 L621.02,30.88 L621.18,30.86 L621.35,30.84 L621.51,30.82 L621.67,30.80 L621.83,30.78 L621.99,30.76 L622.15,30.73 L622.31,30.71 L622.46,30.69 L622.63,30.67 L622.79,30.65 L622.94,30.63 L623.10,30.61 L623.26,30.58 L623.42,30.56 L623.58,30.54 L623.74,30.52 L623.89,30.50 L624.05,30.48 L624.21,30.45 L624.36,30.43 L624.52,30.41 L624.68,30.39 L624.83,30.37 L624.99,30.34 L625.15,30.32 L625.30,30.30 L625.46,30.28 L625.61,30.26 L625.77,30.23 L625.92,30.21 L626.08,30.19 L626.23,30.17 L626.39,30.14 L626.54,30.12 L626.70,30.10 L626.85,30.08 L627.00,30.06 L627.15,30.03 L627.31,30.01 L627.46,29.99 L627.61,29.97 L627.77,29.94 L627.92,29.92 L628.07,29.90 L628.22,29.88 L628.38,29.85 L628.53,29.83 L628.68,29.81 L628.83,29.78 L628.98,29.76 L629.13,29.74 L629.28,29.72 L629.43,29.69 L629.58,29.67 L629.73,29.66 L629.88,29.64 L630.03,29.63 L630.18,29.61 L630.33,29.59 L630.48,29.58 L630.63,29.56 L630.78,29.55 L630.93,29.53 L631.08,29.52 L631.22,29.50 L631.37,29.49 L631.52,29.47 L631.67,29.46 L631.82,29.44 L631.96,29.42 L632.11,29.41 L632.26,29.39 L632.40,29.38 L632.55,29.36 L632.70,29.35 L632.84,29.33 L632.99,29.31 L633.13,29.30 L633.28,29.28 L633.43,29.27 L633.57,29.25 L633.72,29.23 L633.86,29.22 L634.01,29.20 L634.15,29.19 L634.30,29.17 L634.44,29.15 L634.58,29.14 L634.73,29.12 L634.87,29.11 L635.02,29.09 L635.16,29.07 L635.30,29.06 L635.44,29.04 L635.59,29.03 L635.73,29.01 L635.87,28.99 L636.01,28.98 L636.16,28.96 L636.30,28.95 L636.44,28.93 L636.58,28.91 L636.73,28.90 L636.87,28.88 L637.01,28.86 L637.15,28.85 L637.29,28.83 L637.43,28.81 L637.57,28.80 L637.71,28.78 L637.85,28.76 L637.99,28.75 L638.13,28.73 L638.27,28.72 L638.41,28.70 L638.55,28.68 L638.69,28.67 L638.83,28.65 L638.97,28.63 L639.11,28.62 L639.25,28.60 L639.38,28.58 L639.52,28.56 L639.66,28.55 L639.80,28.53 L639.94,28.51 L640.07,28.50 L640.21,28.48 L640.35,28.46 L640.49,28.45 L640.62,28.43 L640.76,28.41 L640.90,28.40 L641.03,28.38 L641.17,28.36 L641.31,28.35 L641.44,28.33 L641.58,28.31 L641.72,28.29 L641.85,28.28 L641.99,28.26 L642.12,28.24 L642.26,28.23 L642.39,28.21 L642.53,28.19 L642.66,28.17 L642.80,28.16 L642.93,28.14 L643.06,28.12 L643.20,28.10 L643.33,28.09 L643.47,28.07 L643.60,28.05 L643.73,28.03 L643.87,28.02 L644.00,28.00" fill="none" stroke="#2f6f73" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"></path><line x1="197.2695145882545" y1="294.49680642283676" x2="217.5495145882545" y2="269.5368064228368" stroke="#2f6f73" stroke-width="1" stroke-opacity="0.75"></line><circle cx="197.2695145882545" cy="294.49680642283676" r="4" fill="#2f6f73" stroke="#ffffff" stroke-width="1.4"></circle><text x="223.2695145882545" y="262.49680642283676" text-anchor="start" dominant-baseline="middle" fill="#514c45" stroke="#ffffff" stroke-width="4" paint-order="stroke" stroke-linejoin="round" font-size="12.5" font-weight="550">top 10: 8.1%</text> <line x1="328.539029176509" y1="233.72918567605456" x2="347.259029176509" y2="200.96918567605456" stroke="#2f6f73" stroke-width="1" stroke-opacity="0.75"></line><circle cx="328.539029176509" cy="233.72918567605456" r="4" fill="#2f6f73" stroke="#ffffff" stroke-width="1.4"></circle><text x="352.539029176509" y="191.72918567605456" text-anchor="start" dominant-baseline="middle" fill="#514c45" stroke="#ffffff" stroke-width="4" paint-order="stroke" stroke-linejoin="round" font-size="12.5" font-weight="550">top 100: 29.1%</text> <line x1="459.80854376476356" y1="110.7520377214222" x2="413.00854376476354" y2="73.3120377214222" stroke="#b2603c" stroke-width="1" stroke-opacity="0.75"></line><circle cx="459.80854376476356" cy="110.7520377214222" r="4.8" fill="#b2603c" stroke="#ffffff" stroke-width="1.4"></circle><text x="399.80854376476356" y="62.7520377214222" text-anchor="end" dominant-baseline="middle" fill="#23211e" stroke="#ffffff" stroke-width="4" paint-order="stroke" stroke-linejoin="round" font-size="13.5" font-weight="650">top 1,000: 71.5%</text> <line x1="591.078058353018" y1="36.62704727921499" x2="572.358058353018" y2="83.427047279215" stroke="#2f6f73" stroke-width="1" stroke-opacity="0.75"></line><circle cx="591.078058353018" cy="36.62704727921499" r="4" fill="#2f6f73" stroke="#ffffff" stroke-width="1.4"></circle><text x="567.078058353018" y="96.62704727921499" text-anchor="end" dominant-baseline="middle" fill="#514c45" stroke="#ffffff" stroke-width="4" paint-order="stroke" stroke-linejoin="round" font-size="12.5" font-weight="550">top 10,000: 97.0%</text></svg>

MGnify cluster-size distribution after removing size-1 clusters from the visualization. The cumulative plot uses the remaining multi-member fragments as its denominator.

That changes what "sampling from MGnify" means. Sampling fragments uniformly mostly revisits the same common neighborhoods. Sampling clusters uniformly goes too far the other way and gives the smallest repeated neighborhoods too much influence. The sampler needs to live somewhere between those two extremes.

## Sampling from a redundant world

If we are training a generative model on MGnify, how should we sample from these clusters? The standard recipe is: pick a cluster uniformly, then pick a member uniformly from inside it. For data this skewed, that overshoots in the opposite direction. With uniform cluster sampling, the top 1,000 MGnify clusters — which hold 71.5% of multi-member fragments — would be sampled only about 4% of the time. We instead use a balancing exponent γ (implemented as `cluster_size_exponent`), where the aggregate sampling probability of a cluster scales like N <sup>γ</sup> with N the cluster size. γ = 1 recovers the dataset distribution; γ = 0 weights every cluster equally; values in between trade off natural abundance against fold diversity.

### Sampling mass under γ-reweighting

Per-cluster aggregate weight scales as N <sup>γ</sup>.

**10,462** effective clusters **22.2%** sampling mass in top 1,000

top 10

data 7.05% sample 0.81%

top 100

data 26.0% sample 4.80%

top 1,000

data 64.3% sample 22.2%

Gray shows how much of the raw dataset sits in the largest clusters. Teal shows how much sampling mass those clusters receive after reweighting. Effective clusters are the inverse-Simpson count, 1 / ∑ <sub>i</sub> p <sub>i</sub> <sup>2</sup>, where p <sub>i</sub> is the sampling mass assigned to cluster i.

The right γ depends on what the downstream model is supposed to learn. A generative model trying to *cover* fold space wants lower γ, since it benefits from seeing rare folds more than once per epoch. A folding model trying to *match* natural conditional distributions wants higher γ. We don't have a settled answer, but γ around 0.5 has been a reasonable starting point in our setups — it preserves the head's dominance while flattening the long tail. The effective-cluster count in the figure is a useful sanity check: it's the number of clusters you would need if they were all equally weighted to give the same diversity as your reweighted distribution.

## Conclusion

What surprised us is how redundant natural fold space looks once you pick the right unit of clustering. After cleaning up predicted structures, cutting away obvious noise, splitting multi-domain chains, auditing Foldseek singletons, and clustering the resulting fragments, most of the mass sits in a small number of structural neighborhoods. **Natural proteins do not appear to be exploring backbone space uniformly.** They seem to reuse a relatively small set of fold solutions over and over.

Natural enzymes often evolve by modifying existing proteins: duplication, divergence, loop changes, active-site mutations, cofactors, metals, and changes in the local environment around a substrate. What surprised us was not that nature reuses folds, but how strongly that reuse shows up once we process predicted structures into training units and cluster them at scale.

For enzyme design, this leaves two different possibilities. One is the nature-like route: choose a familiar scaffold and learn how to engineer the active-site neighborhood with much higher precision. In that view, the loops, first-shell residues, ligand pose, cofactors, and interaction geometry matter more than making the backbone globally novel. If that is the right regime, then simply adding more natural sequence-derived structures may not help much by itself; it may mostly give us more examples of the same scaffold families.

The other possibility is more speculative. Evolution is historically constrained; new enzymes do not appear from nowhere, and natural fold space may be shaped by what was easy to reach through duplication and divergence. If design models become good enough, there may be useful backbone space that nature never explored. But that raises a harder question: can models trained mostly on natural folds learn to explore outside the natural fold manifold, or do they inherit the same redundancy we are measuring here?

We will find out in the lab as we try to design enzymes, seeing which designs actually express, fold, and catalyze. More on this later.

## Supplementary info

### Where the MGnify distillation advantage actually shows up

One reason I am suspicious of treating MGnify as just more sequence data: the performance advantage does not appear uniformly across every interface benchmark. It shows up strongly in antibody-antigen prediction, while most of the broader cofolding benchmarks remain closer together. This is not a clean causal experiment — architecture, compute, and training details all move at once — but it fits the intuition that protein-protein interaction accuracy improves when the model has seen much more of natural protein space.

![Antibody-antigen scaling analysis comparing AlphaFold3, OF3p2, Protenix-v1, Boltz-1, and Chai-1 by number of seeds and mean DockQ](https://research.ligo.bio/posts/unreasonable-redundancy-of-natural-protein-folds/assets/antibody-antigen-scaling.png)

In this comparison, AlphaFold3, OF3p2, and Protenix-v1 use MGnify-scale protein distillation; Boltz-1 and Chai-1 do not. The separation is most visible on antibody-antigen docking, where the antibody and antigen do not share coevolutionary history.

![FoldBench interface benchmark success rates for AlphaFold3, OF3p2, Protenix-v1, Boltz-1, and Chai-1 across protein-protein, protein-peptide, protein-DNA, and protein-RNA interfaces](https://research.ligo.bio/posts/unreasonable-redundancy-of-natural-protein-folds/assets/Foldbench-all-cofolding.png)

The broader interface benchmarks are much more compressed. Across protein-protein, protein-peptide, protein-DNA, and protein-RNA cofolding, the same split between MGnify-distilled and non-MGnify-distilled models is not nearly as clean.

### Spectral linker split

This is a standalone version of the graph split used above. It assumes you have already filtered out low-confidence residues, and that `ca_coords` contains only the C-alpha coordinates you still want to consider. The function returns the C-alpha indices that sit closest to Fiedler sign-change boundaries; in our pipeline those residues become linker/cut residues before fragment IDs are assigned.

```python
import numpy as np
from scipy.sparse import csr_matrix
from scipy.spatial import KDTree

def spectral_linker_indices(
    ca_coords: np.ndarray,
    *,
    k: int = 15,
    sigma: float = 8.0,
    connectivity_threshold: float = 0.05,
    boundary_size: int = 4,
    min_partition_size: int = 50,
) -> np.ndarray:
    """
    Find linker-like C-alpha positions with recursive spectral bisection.

    Parameters
    ----------
    ca_coords:
        Array with shape (N, 3), containing only the C-alpha coordinates that
        survived whatever filtering you want to apply first, usually pLDDT.
    k:
        Number of spatial nearest neighbors used to build the residue graph.
    sigma:
        Gaussian bandwidth for edge weights: exp(-d^2 / (2 sigma^2)).
    connectivity_threshold:
        Stop splitting when the Fiedler value is above this threshold.
    boundary_size:
        Number of residues closest to each sign-change boundary to mark.
    min_partition_size:
        Do not try to split partitions smaller than this.

    Returns
    -------
    np.ndarray
        Sorted indices into ca_coords. These are the residues to treat as
        linkers/cuts before assigning final fragments.
    """
    coords = np.asarray(ca_coords, dtype=float)
    if coords.ndim != 2 or coords.shape[1] != 3:
        raise ValueError("ca_coords must have shape (N, 3)")

    n = len(coords)
    if n < min_partition_size:
        return np.array([])

    k_eff = min(k, n - 1)
    if k_eff < 1:
        return np.array([])

    tree = KDTree(coords)
    distances, neighbors = tree.query(coords, k=k_eff + 1)

    # Skip the self-neighbor in column 0.
    row = np.repeat(np.arange(n), k_eff)
    col = neighbors[:, 1:].ravel()
    weights = np.exp(-(distances[:, 1:] ** 2).ravel() / (2 * sigma**2))

    W = csr_matrix((weights, (row, col)), shape=(n, n))
    W = W.maximum(W.T)

    linker_indices: set[int] = set()

    def split(node_indices: np.ndarray) -> None:
        if len(node_indices) < min_partition_size:
            return

        idx = np.sort(node_indices)
        sub_W = W[idx][:, idx].toarray()

        degree = sub_W.sum(axis=1)
        if np.count_nonzero(degree) < 2:
            return

        d_inv_sqrt = np.zeros_like(degree)
        nonzero = degree > 0
        d_inv_sqrt[nonzero] = 1.0 / np.sqrt(degree[nonzero])

        # Normalized graph Laplacian: L_sym = I - D^-1/2 W D^-1/2.
        L_sym = np.eye(len(idx)) - d_inv_sqrt[:, None] * sub_W * d_inv_sqrt[None, :]

        evals, evecs = np.linalg.eigh(L_sym)
        if len(evals) < 2:
            return

        fiedler_value = evals[1]
        fiedler_vector = evecs[:, 1]
        if fiedler_value > connectivity_threshold:
            return

        boundary_order = np.argsort(np.abs(fiedler_vector))[:boundary_size]
        linker_indices.update(idx[boundary_order].tolist())

        keep = np.ones(len(idx), dtype=bool)
        keep[boundary_order] = False

        partition_a = idx[keep & (fiedler_vector < 0)]
        partition_b = idx[keep & (fiedler_vector >= 0)]

        split(partition_a)
        split(partition_b)

    split(np.arange(n))
    return np.array(sorted(linker_indices))
```

### Foldseek command

For the fragment clustering pass, this is the Foldseek command we used before the representative-level structural audit.

```bash
# Foldseek command for reproducibility
$FOLDSEEK cluster "$DB_DIR/fragDB" "$DB_DIR/fragCluDB" "$TMP_DIR" \
  --threads "$THREADS" \
  -c 0.8 --cov-mode 0 \
  --tmscore-threshold 0.7 \
  --tmscore-threshold-mode 1 \
  --lddt-threshold 0.6 \
  --max-seqs 2000 \
  -e 0.001 \
  --alignment-type 2 \
  --cluster-reassign 1 \
  -v 2
```

## Citation

Please cite this work as:

```
Arda Goreci, "The Unreasonable Redundancy of Nature's Protein Folds",
Ligo Biosciences Blog, May 20, 2026.
```

Or use the BibTeX citation:

```
@article{goreci2026naturesproteinfolds,
  author = {Arda Goreci},
  title = {The Unreasonable Redundancy of Nature's Protein Folds},
  journal = {Ligo Biosciences Blog},
  year = {2026},
  month = may,
  day = {20},
  publisher = {Ligo Biosciences}
}
```