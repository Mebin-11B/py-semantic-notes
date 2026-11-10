---
title: "The Unix Pipe Card Game"
url: https://punkx.org/unix-pipe-game/
clipped: 2026-06-17 01:55:49
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [The Unix Pipe Card Game](https://punkx.org/unix-pipe-game/)

## Digest Summary
The UNIX Pipe Card Game is a tabletop activity that uses Unix command‑line tools (cat, grep, tail, head, wc, sort, uniq) to solve text‑processing tasks. Players first decide whether the round is won by the smallest or largest pipe chain required to complete a task. The youngest player selects a task card (e.g., “print the second line”, “print the most common line”, “count lines containing ‘rises’”, “show two random lines”, “make a command chain that prints nothing”, etc.) and cannot repeat tasks. Cards are shuffled face‑down; each player draws the top card in turn and attempts the command pipeline. The first to complete the task scores a point. Play continues until tasks are exhausted, then the game repeats. The description also lists related educational games that teach programming concepts such as Python basics, C pointers, machine code, process substitution, paste/tr/cut/bc, run‑length encoding, function composition, and RISC‑V assembly.

## Discussion Summary
Comments show a blend of enthusiasm and skepticism. Many appreciate the novelty of a physical card game that references Unix pipes, noting its charm, affordability, and suitability as a novelty gift, while some recall similar DIY attempts. However, several point out that the tactile format reduces instant, visual feedback essential for learning, limits replay value, and may be less engaging than a digital or terminal‑based version. Requests for an online version, broader command sets, and extensions for advanced topics also appear, reflecting both interest and concern about its educational effectiveness.

---

## Full Article

The UNIX Pipe Card Game
=======================

This is a card game for teaching kids how to combine unix commands through pipes.  
  
This game assumes the parent knows the basic unix commands: `cat, grep, tail, head, wc, sort, uniq`. The parent should show also show those commands in action the computer as well, if you do not have any UNIX system you can use [jslinux](https://bellard.org/jslinux/vm.html?url=alpine-x86.cfg&mem=192) in your browser.
[![](https://punkx.org/unix-pipe-game/photos/deck.jpg)](https://punkx.org/unix-pipe-game/photos/deck.jpg)  
[~~Buy now: €5,00 EUR~~ [ soldout ]](https://punkx.org/unix-pipe-game/#)
  
If you want to play the **more difficult** version, you can also get the Expansion pack: [UNIX Pipe Game - Process Substitution](https://punkx.org/unix-pipe-game/ext-0.1/index.html)  
  
Example game round:

task: **print the most common line from a file**, we need to first cat the file (in our case the file is card 03.txt), then sort it, uniq count it, then do numeric sort, then tail -1:
  
  
**cat 03.txt | sort | uniq -c | sort -n | tail -1**

[![](https://punkx.org/unix-pipe-game/photos/example.jpg)](https://punkx.org/unix-pipe-game/photos/example.jpg)
  

```
                 RULES:

> 0. The youngest player chooses one of
  two formats for the game:

* Whoever has the smallest pipe chain to 
  complete the task wins the round.
* Whoever has the largest pipe chain to 
  complete the task wins the round.

> 1. The youngest player picks a task
  from the tasks card. You can not pick
  the same task twice.

> 2. Shuffle the cards.

> 3. Put the cards face down on the
  table.

> 4. Going clockwise each player picks
  the top card from the deck and tries 
  to complete the task.

> 5. The first player who completes the
  task gets a point.

> 6. IF there are no more tasks, GOTO 8

> 7. GOTO 1.

> 8. GAME OVER. INSERT COIN. GOTO 8

TASKS

  * print the second line

  * print the second to last line

  * print the 7th line

  * print the most common line

  * print the least common line

  * count how many lines have "rises"

  * print the first line that has W in it

  * count the lines that have "in" in them

  * show two random lines

  * count the words on the last two lines

  * print the 7th and 8th line

  * count the lines with !

  * count the lines without !

  * make a command chain that does not
    print anything
```

This is how the card decks look:
[![](https://punkx.org/unix-pipe-game/photos/many-decks.jpg)](https://punkx.org/unix-pipe-game/photos/many-decks.jpg)
If you are a parent teaching your kid, and is exploring more tools to help you, I made few other card games:  

[![](https://punkjazz.org/programming-time/photos/b-800.jpg)](https://punkjazz.org/programming-time/)

[Programming Time](https://punkjazz.org/programming-time/), which is a game to teach python and some more fundamental algorithms, from hash tables to RSA

[![](https://punkx.org/c-pointer-game/photos/deck.jpg)](https://punkx.org/c-pointer-game/)

[The C Pointer Game - Pointers, Arrays and Strings](https://punkx.org/c-pointer-game/), a game to teach kids to look at the computer memory and understand references and values

[![](https://punkx.org/4917/photos/a.jpg)](https://punkx.org/4917/)

[4917](https://punkx.org/4917/), a game to teach kids machine code and how the CPU works with memory and registers

[![](https://punkx.org/unix-pipe-game/ext-0.1/photos/deck.jpg)](https://punkx.org/unix-pipe-game/ext-0.1)

[The Unix Pipes Game - Process Substitution](https://punkx.org/unix-pipe-game/ext-0.1), an expansion of the Unix Pipes Game to teach process substitution and also: `paste, tr, cut, bc`

[![](https://punkx.org/runlength-for-kids/photos/deck.jpg)](https://punkx.org/runlength-for-kids/)

[RunLength Encoding for Kids](https://punkx.org/runlength-for-kids/), small cards "game" to explain runlength encoding

[![](https://punkx.org/punk0/photos/deck.jpg)](https://punkx.org/punk0/)

[PUNK0 - The Function Composition Card Game](https://punkx.org/punk0/), use cards to manipulate a list and use its values to win the game

[![](https://punkx.org/overflow/logo.svg)](https://punkx.org/overflow/)

[PROJEKT: OVERFLOW](https://punkx.org/overflow/), RISCV assembler boardgame

[![](https://punkx.org/github.png)](https://github.com/jackdoe/programming-for-kids/blob/master/book.md)

[Programming for kids](https://github.com/jackdoe/programming-for-kids/blob/master/book.md), a log of my journey of teaching my daughter how to code