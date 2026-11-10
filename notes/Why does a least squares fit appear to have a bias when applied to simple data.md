---
title: "Why does a least squares fit appear to have a bias when applied to simple data?"
url: https://stats.stackexchange.com/questions/674129/why-does-a-linear-least-squares-fit-appear-to-have-a-bias-when-applied-to-simple
clipped: 2026-06-17 02:03:35
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Why does a least squares fit appear to have a bias when applied to simple data?](https://stats.stackexchange.com/questions/674129/why-does-a-linear-least-squares-fit-appear-to-have-a-bias-when-applied-to-simple)

## Digest Summary
- The data are generated as a linear transformation of a 2‑D standard normal, then shifted by **μ**; the resulting cloud has strong anisotropy (large variance along one direction).  
- Ordinary least‑squares (OLS) regression fits **y = a x + b** by minimizing the sum of squared **vertical** residuals. Its slope is  

\[
a = \frac{\operatorname{Cov}(x,y)}{\operatorname{Var}(x)},
\]

and the fitted line always passes through the sample mean \((\bar x,\bar y)\).  
- Principal‑component analysis (PCA) finds the eigenvector of the covariance matrix with the largest eigenvalue. That eigenvector gives the direction that maximizes total variance, i.e. it minimizes **orthogonal** distances to the line. Its slope is the ratio of the eigenvector components and depends on both \(\operatorname{Var}(x)\) and \(\operatorname{Var}(y)\).  
- When \(\operatorname{Var}(x) \neq \operatorname{Var}(y)\) (as in the code, where the x‑direction is stretched), the OLS slope differs from the PCA direction, producing the apparent “bias” or tilt.  
- The discrepancy is not a mistake; it reflects the different error assumptions: OLS assumes errors only in *y* (vertical), while PCA/total‑least‑squares assumes errors in both variables (isotropic). Using orthogonal regression would align the fitted line with the PCA eigenvector.

## Discussion Summary
The comments explain that ordinary least‑squares regression assumes error only in the response variable, while many practical situations involve measurement error in both predictors and outcomes, prompting use of total‑least‑squares, Deming regression, or PCA‑based approaches. They note that OLS provides unbiased predictions of Y given X under its assumptions but can exhibit regression‑dilution bias when X is noisy. Normalisation, visual checks of residual symmetry, and awareness of differing loss functions are suggested to mitigate bias, and the overall tone acknowledges the need for alternative methods without claiming novelty.

---

## Full Article

The answer lies in the data generating process. As other answers have pointed out, the simple OLS model assumes

$$
Y = \beta\_0 + \beta\_1 X + \varepsilon
$$

and that $X$ and $\varepsilon$ are independent. It also assumes that we know $X$ with certainty.

Let’s consider the case where we have a perfectly fit regression and all error terms are zero. Because all the data points lie along the regression line, there is no variance in any other direction. So if we were to do PCA on this, the principal component would be in exactly the same direction as our regression line, matching your intuition. Once we start to add noise (i.e. increase the error term), which is strictly in the vertical direction, PCA is going to capture some of that for the first principal component, and leave what’s left over for the second. That is, the direction of maximum variance is going to be more extreme in the $Y$ direction. That’s what you’re observing in your own plots (only talking about the slope discrepancy here, not the centroid, which is covered by other answers).

Now consider the opposite extreme, when error dominates. Here it’s useful to pull apart the variance of $Y$:

$$
\operatorname{Var}(Y) = \operatorname{Var}(\beta\_1 X + \varepsilon)
= \operatorname{Var}(\beta\_1 X) + \operatorname{Var}(\varepsilon)
= \beta\_1^2 \operatorname{Var}(X) + \operatorname{Var}(\varepsilon)
$$

So in the case where

$$
\operatorname{Var}(\varepsilon) \gg \beta\_1^2 \operatorname{Var}(X),
$$

nearly all variation is vertical. The principal component direction approaches vertical as error variance increases.

[![variance domination](https://i.sstatic.net/zchHXY5n.jpg)](https://i.sstatic.net/zchHXY5n.jpg)

Another source of confusion may be that the covariance ellipse only serves as a meaningful data contour when $(X, Y)$ are jointly normal. Here are examples where $X$ has different distributions:

[![enter image description here](https://i.sstatic.net/bOMMgEUr.jpg)](https://i.sstatic.net/bOMMgEUr.jpg)

Again, we see the same pattern: when the $X$ variance dominates, the principal component lines up far more with the regression line. But when the ellipsoid doesn’t coincide with such a tight contour of the data, we can more easily see that we’re dealing with different things in PCA and OLS.

Notice that when

$$
\operatorname{Var}(X) \gg \operatorname{Var}(\varepsilon),
$$

PCA and OLS align. But the ellipse no longer describes the data's shape. It indicates direction, not density.

Here’s the code used to generate this data. Notice that the `make_y_from_x` function follows the precise assumptions of OLS. $Y$ is a linear function of $X$ plus i.i.d. Gaussian noise (if you want to have correlated residuals to try to violate the assumption, you can create that in the data generating process). Importantly, $X$ isn’t necessarily a random variable. $X$ could be from an experiment we designed with fixed values, or non-random for any other reason. It can also be random (but still known with certainty), so it’s important to think about this when specifying a model. (See [What is a random variable and what isn't in regression models](https://stats.stackexchange.com/questions/485011/what-is-a-random-variable-and-what-isnt-in-regression-models)). Notice that the covariance ellipse treats $X$ and $Y$ symmetrically, but the data generating process is quite different.

Quick summary:

* When $\operatorname{Var}(X) \gg \operatorname{Var}(\varepsilon)$: PCA aligns with OLS (the textbook case)
* When $\operatorname{Var}(\varepsilon) \gg \operatorname{Var}(X)$: PCA approaches vertical
* $X$ is not necessarily random, and definitely doesn’t have to be normally distributed.

```
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

SLOPE = 1.0
INTERCEPT = -100.0
X_MEAN = 150.0
X_SCALE = 50.0


def make_y_from_x(x, noise_std, slope=SLOPE, intercept=INTERCEPT):
    return intercept + slope * x + np.random.randn(len(x)) * noise_std


def deterministic_binary_x(n):
    x_low = X_MEAN - X_SCALE
    x_high = X_MEAN + X_SCALE
    x = np.repeat([x_low, x_high], n // 2)
    if len(x) < n:
        x = np.append(x, x_high)
    return x


def deterministic_uniform_x(n):
    return np.linspace(X_MEAN - X_SCALE, X_MEAN + X_SCALE, n)


def bimodal_x(n):
    mix = np.random.rand(n) < 0.5
    x = np.empty(n)
    x[mix] = np.random.randn(mix.sum()) * (X_SCALE / 3) + (X_MEAN - X_SCALE)
    x[~mix] = np.random.randn((~mix).sum()) * (X_SCALE / 3) + (X_MEAN + 3 * X_SCALE)
    return x


def triangular_x(n):
    return np.random.triangular(
        X_MEAN - X_SCALE,
        X_MEAN + X_SCALE,
        X_MEAN + X_SCALE,
        size=n
    )


def plot_from_cov(ax, x, y, title):
    x = (x - np.mean(x)) / np.std(x)
    y = (y - np.mean(y)) / np.std(y)

    mu_x, mu_y = np.mean(x), np.mean(y)

    cov = np.cov(x, y)
    eigvals, eigvecs = np.linalg.eigh(cov)
    idx = np.argmax(eigvals)

    v = eigvecs[:, idx]
    angle = np.degrees(np.arctan2(v[1], v[0]))

    a = 3 * np.sqrt(eigvals[idx])
    b = 3 * np.sqrt(eigvals[1 - idx])

    ax.plot(x, y, '.', alpha=0.05)

    slope, intercept = np.polyfit(x, y, 1)
    xs = np.array([x.min(), x.max()])
    ax.plot(xs, slope * xs + intercept, lw=2)

    ax.quiver(
        mu_x, mu_y,
        a * v[0], a * v[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        width=0.01,
        color='black',
        zorder=20
    )

    ell = Ellipse((mu_x, mu_y), 2 * a, 2 * b,
                  angle=angle, edgecolor='red',
                  facecolor='none', lw=2)
    ax.add_patch(ell)

    xmin = min(x.min(), mu_x - a)
    xmax = max(x.max(), mu_x + a)
    ymin = min(y.min(), mu_y - a)
    ymax = max(y.max(), mu_y + a)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect('equal', adjustable='box')

    ax.text(0.02, 0.98, title,
            transform=ax.transAxes,
            ha='left', va='top',
            fontsize=11, weight='bold')


# -------- Joint normal: variance domination --------
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.ravel()

n = 20000
beta = 1.0

settings = [
    (0.3, "var(X) >> var(ε)"),
    (5.0, "var(ε) >> var(X)")
]

for ax, (sigma, label) in zip(axs, settings):
    X = np.random.randn(n)
    Y = beta * X + np.random.randn(n) * sigma
    plot_from_cov(ax, X, Y, label)

for ax in axs[len(settings):]:
    ax.axis("off")

plt.tight_layout()


# -------- Different X distributions --------
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.ravel()

make_xs = [
    deterministic_binary_x,
    deterministic_uniform_x,
    bimodal_x,
    triangular_x
]

sigma = 30.0

for ax, make_x in zip(axs, make_xs):
    X = make_x(n)
    Y = beta * X + np.random.randn(n) * sigma
    plot_from_cov(ax, X, Y, make_x.__name__)

plt.tight_layout()
plt.show()
```