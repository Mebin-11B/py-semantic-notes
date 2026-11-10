---
title: "ajratnam/image-to-ascii: A python program to convert an image into an ascii image"
source: "https://github.com/ajratnam/image-to-ascii"
author:
published:
created: 2026-05-31
description: "A python program to convert an image into an ascii image - ajratnam/image-to-ascii"
tags:
  - "clippings"
processed: true
processed_at: 2026-05-31
summary_status: done
concepts:
  - CLI Tools
  - Developer Tools
  - Image Processing
  - ASCII Art
related:
  - "[[tobiqmd mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local.md]]"
  - "[[Software Development Tools]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A Python program to convert images into customized ASCII art with controls for scaling, brightness, sharpness, and characters.
>
> **Key points:**
> - The utility converts standard digital images into text-based ASCII art representations.
> - Users can configure the output by specifying custom character sets, resizing dimensions, and adjusting image properties like brightness and sharpness.
> - Supports advanced features such as color rendering and converting the generated ASCII art back into an image file.
> - Includes dependency management using Poetry and verification via pytest coverage.
>
> **Concept links:** [[CLI Tools]], [[Developer Tools]], [[Image Processing]], [[ASCII Art]]
>
> **Suggested connections:**
> - [[tobiqmd mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local.md]] — another Python-based local CLI utility in the vault.
> - [[Software Development Tools]] — relates to utility programs that assist developers with formatting, conversions, or local scripting.
<!-- ai-summary:end -->

## image-to-ascii

A python program to convert an image into an ascii image

## Introduction

This program allows you to convert images into ASCII art. It uses various parameters to control the conversion process, including image scaling, sharpness adjustment, brightness adjustment, character set, and more.

## Installation

1. Clone this repository to your local machine.
	```
	git clone https://www.github.com/ajratnam/image-to-ascii.git
	```
2. Activate the poetry environment.
	```
	poetry shell
	```
3. Install the dependencies.
	```
	poetry install
	```

## Usage

The documentation for the program can be read [here](https://ajratnam.github.io/image-to-ascii/).

## Examples

Here are some examples of how to use the program:

### Convert an image to ASCII art.

```
from converter import image_to_ascii
print(image_to_ascii('images/angry_bird.jpg'))
```

This converts the image to ASCII art and prints it to the console. [![ascii_angry_bird](https://raw.githubusercontent.com/ajratnam/image-to-ascii/main/images/angry_bird_ascii.jpg)](https://raw.githubusercontent.com/ajratnam/image-to-ascii/main/images/angry_bird_ascii.jpg)

### Save the ASCII art to an image.

```
from converter import image_to_ascii, ascii_to_image
ascii_art = image_to_ascii('images/angry_bird.jpg')
ascii_art_image = ascii_to_image(ascii_art)
ascii_art_image.save('images/angry_bird_ascii.jpg')
```

This saves the ASCII art to an image file on your computer.

### Change the size of the ascii art by absolute pixels.

```
from converter import image_to_ascii
print(image_to_ascii("images/angry_bird.jpg", size=(30, 30)))
```

This resizes the ASCII art to look like 30x30 characters(but it is actually 60x30 pixels). [![ascii_angry_bird_resized](https://raw.githubusercontent.com/ajratnam/image-to-ascii/main/images/angry_bird_ascii_resized.jpg)](https://raw.githubusercontent.com/ajratnam/image-to-ascii/main/images/angry_bird_ascii_resized.jpg)

### Change the size of the ascii art by absolute pixels but do not try to maintain visual aspect ratio.

```
from converter import image_to_ascii
print(image_to_ascii("images/angry_bird.jpg", size=(30, 30), fix_scaling=False))
```

This resizes the ASCII art to 30x30 characters.### Change the size of the ascii art by relative scaling.

```
from converter import image_to_ascii
print(image_to_ascii("images/angry_bird.jpg", scale=0.5))
```

This resizes the ASCII art to 50% of the original size.### Brighten the ascii art.

```
from converter import image_to_ascii
print(image_to_ascii("images/angry_bird.jpg", brightness=3))
```

This increases the brightness of the ASCII art to 3 times the original.### Darken the ascii art.

```
from converter import image_to_ascii
print(image_to_ascii("images/angry_bird.jpg", brightness=0.2))
```

This decreases the brightness of the ASCII art to 20% of the original.### Sharpen the ascii art.

```
from converter import image_to_ascii
print(image_to_ascii("images/angry_bird.jpg", sharpness=3))
```

This increases the sharpness of the ASCII art to 3 times the original.### Blur the ascii art.

```
from converter import image_to_ascii
print(image_to_ascii("images/angry_bird.jpg", sharpness=0.2))
```

This decreases the sharpness of the ASCII art to 20% of the original.### Change the character set used to generate the ascii art.

```
from converter import image_to_ascii
print(image_to_ascii("images/angry_bird.jpg", charset=' ░▒▓█'))
```

Changes the characters used to generate the ASCII art.### Print colored ascii art to the console.

```
from converter import image_to_ascii
print(image_to_ascii("images/angry_bird.jpg", colorful=True))
```

Prints the ASCII art colorfully to the console.## License

This project is licensed under the [MIT License](https://raw.githubusercontent.com/ajratnam/image-to-ascii/main/LICENSE).

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create an issue or a pull request. Install the additional development dependencies with `poetry install --dev`. Run coverage test with `python -m pytest --cov`