---
title: "Lent and Lisp"
url: https://leancrew.com/all-this/2026/02/lent-and-lisp/
clipped: 2026-06-17 01:29:52
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
---

# [Lent and Lisp](https://leancrew.com/all-this/2026/02/lent-and-lisp/)

## Digest Summary
The author expands a previous post on coinciding religious dates by adding Ash Wednesday and Chinese New Year, using calendar algorithms from Reingold & Dershowitz’s *Calendrical Calculations*. The original Common Lisp source (calendar.l) fails to load in SBCL/CLISP due to package/export declarations; removing the duplicated `(in-package "CC4")` and export list allows the file to load as `calendar.lisp`. A CLISP script (`ramadan‑lent`) loads this library, defines weekday and month name vectors, a `gregorian-date-string` formatter, and iterates 500 Islamic years (±250 years from the current year). For each year it computes Ramadan 1 (fixed‑date) and the corresponding Ash Wednesday (`easter(gyear) - 46`). When the dates match it prints the Gregorian date. Output shows nine matches between 1799 and 2253, with typical intervals of 98 years and occasional 31‑ or 67‑year gaps. A second script adds a check for Chinese New Year using `chinese-new-year-on-or-before`; matches occur in 1799, 2026, 2124, and 2222, confirming a triple coincidence after a 227‑year gap and predicting the next after 98 years. The author plans further exploration of the calendrical library.

## Discussion Summary
The discussion proposes replacing the calendar.l header with a package definition that explicitly lists a large number of exported symbols, using a defpackage form followed by an in-package declaration. It notes that symbols can be referenced as symbols, uninterned symbols, or strings, with string‑designators offering advantages when many symbols are involved. The comment also clarifies that “package” in Common Lisp already denotes a namespace, making the phrase “packages and namespaces” redundant, and suggests the underlying issue likely relates to package handling.

---

## Full Article

[Next post](https://leancrew.com/all-this/2026/03/port-ability/)
[Previous post](https://leancrew.com/all-this/2026/02/my-omnigraffle-ticks/)

February 25, 2026 at 9:13 AM by Dr. Drang

After writing [last week’s post](https://leancrew.com/all-this/2026/02/chinese-new-year-and-ramadan/) about the start of Ramadan and Chinese New Year, I expected to hear from people asking why I didn’t include the further coincidence of Ash Wednesday. I was surprised that the only such feedback I got was an email from [TJ Luoma](https://rhymeswithdiploma.com/). It makes sense that Lent would be on TJ’s mind—it’s a big part of his business calendar—but I had an answer prepared, and I wrote him back with my reasons.

As I typed out the reply, though, the reasons seemed weaker. Yes, it’s true that the full moon that determines this year’s [date of Easter](https://aa.usno.navy.mil/faq/easter) (and therefore Ash Wednesday) isn’t part of the same lunation that determines the start of Ramadan and Chinese New Year, so there was an astronomical reason to keep Ash Wednesday out of the post. But it’s also true that both Ramadan and Lent represent periods of self-denial, so there’s a cultural connection.

Adding a new bit of Emacs Lisp code to what I’d already written to include a check for Ash Wednesday wouldn’t be hard, but another thought was buzzing in my head: switching from Emacs Lisp to Common Lisp. The ELisp calendar functions were written by Edward Reingold and Nachum Dershowitz, authors of the well-known [*Calendrical Calculations*](https://lccn.loc.gov/2017024295). That book includes [a lot of code](https://www.cambridge.org/us/universitypress/subjects/computer-science/computing-general-interest/calendrical-calculations-ultimate-edition-4th-edition?format=HB#resources) that isn’t in the Emacs implementation, code that does astronomical calculations I’d like to explore. So it seemed like a good idea to write a Ramadan/Lent/Chinese New Year script in Common Lisp and use the functions from the book.

The problem with that idea was that the Common Lisp code I downloaded from the [Cambridge University Press site](https://www.cambridge.org/us/universitypress/subjects/computer-science/computing-general-interest/calendrical-calculations-ultimate-edition-4th-edition?format=HB#resources), `calendar.l`, didn’t work. I tried it in both [SBCL](https://www.sbcl.org/) and [CLISP](https://clisp.sourceforge.io/), and calling

```
(load "calendrical.l")
```

threw a huge number of errors. I was, it turned out, not the first to have [run into this problem](https://stackoverflow.com/questions/72716454/start-working-with-large-lisp-library-calendrical-calculations). The workarounds suggested there on Stack Overflow didn’t help. There’s [a port to Clojure](https://elangocheran.com/2023/12/06/calendars-and-usable-calendrical-calculations-code/) that apparently works, but I was reluctant to use [Clojure](https://clojure.org/) and have to maintain both it and a Java Virtual Machine.

What I found, though, was that Reingold & Dershowitz’s code would load in CLISP with one simple change. After many lines of comments, the working part of `calendar.l` starts with these lines:

```
(in-package "CC4")

(export '(
          acre
          advent
          akan-day-name
          akan-day-name-on-or-before

          [and so on for a few hundred lines]

          yom-ha-zikkaron
          yom-kippur
          zone
          ))
```

Deleting these lines got me a file that would load without errors in CLISP,[1](https://leancrew.com/all-this/2026/02/lent-and-lisp/#fn:sbcl) so I named the edited version `calendar.lisp` and saved it in my `~/lisp/` directory. I believe the problem with the unedited code has something to do with packages and namespaces, and if I keep using Common Lisp long enough, I may learn how to make a better fix. Until then, this will do.

With a working library of calendar code, I wrote the following script, `ramadan-lent`, to get the dates for which Ramadan 1 and Ash Wednesday correspond over a 500-year period:

```
 1:  #! /usr/bin/env clisp -q
 2:  
 3:  ;; The edited Calendrical Calculations code by Reingold and Dershowitz
 4:  (load "calendar.lisp")
 5:  
 6:  ;; Names
 7:  (setq
 8:    weekday-names
 9:    '("Sunday" "Monday" "Tuesday" "Wednesday" "Thursday" "Friday" "Saturday")
10:  
11:    gregorian-month-names
12:    '("January" "February" "March" "April" "May" "June"
13:      "July" "August" "September" "October" "November" "December"))
14:  
15:  ;; Date string function
16:  (defun gregorian-date-string (date)
17:    (let ((g-date (gregorian-from-fixed date))
18:          (weekday (day-of-week-from-fixed date)))
19:      (format nil "~a, ~a ~d, ~d"
20:        (nth weekday weekday-names)
21:        (nth (1- (second g-date)) gregorian-month-names)
22:        (third g-date)
23:        (first g-date))))
24:  
25:  ;; Get today's (Gregorian) date.
26:  (multiple-value-setq
27:    (t-second t-minute t-hour t-day t-month t-year t-weekday t-dstp t-tz)
28:    (get-decoded-time))
29:    
30:  ;; Loop through 500 Islamic years, from 250 years ago to 250 years in
31:  ;; the future and find each Ramadan 1 that corresponds to Ash Wednesday.
32:  ;; Print as a Gregorian date.
33:  (setq
34:    f (fixed-from-gregorian (list t-year t-month t-day))
35:    ti-year (first (islamic-from-fixed f)))
36:  (dotimes (i 500)
37:    (setq iy (+ (- ti-year 250) i)
38:          r (fixed-from-islamic (list iy 9 1))
39:          g-year (gregorian-year-from-fixed r)
40:          aw (- (easter g-year) 46))
41:    (if (equal aw r)
42:      (format t "~a~%" (gregorian-date-string r))))
```

The `-q` in the shebang line tells CLISP not to put up its typical welcome banner. I had to write my own `gregorian-date-string` function (Lines 16–23) because `calendrical.lisp` doesn’t have one, but it was pretty easy.

In fact, it was all pretty easy. I haven’t programmed in Lisp or Scheme in quite a while, but I quickly remembered how fun it is. The only tricky bits were:

* learning how to handle the multiple value output of `get-decoded-time` (Lines 26–28);
* remembering how to handle more than one variable assignment in `setq`; and
* recognizing that what the ELisp calendar library calls “absolute” dates, the Common Lisp calendar library calls “fixed” dates.

R&D’s library has an `easter` function for getting the date of Easter for a given (Gregorian) year; Line 40 gets the date of the associated Ash Wednesday by going back 46 days from Easter.

The output of `ramadan-lent` was

```
Wednesday, February 6, 1799
Wednesday, February 24, 1830
Wednesday, February 22, 1928
Wednesday, February 18, 2026
Wednesday, March 7, 2057
Wednesday, February 16, 2124
Wednesday, March 5, 2155
Wednesday, February 13, 2222
Wednesday, March 2, 2253
```

The most common gap between successive correspondences was 98 years, but there were occasional gaps of 31 and 67 years.

It took only a few extra lines at the end to include a check for Chinese New Year. Here’s `ramadan-lent-new-year`:

```
 1:  #! /usr/bin/env clisp -q
 2:  
 3:  ;; The edited Calendrical Calculations code by Reingold and Dershowitz
 4:  (load "calendar.lisp")
 5:  
 6:  ;; Names
 7:  (setq
 8:    weekday-names
 9:    '("Sunday" "Monday" "Tuesday" "Wednesday" "Thursday" "Friday" "Saturday")
10:  
11:    gregorian-month-names
12:    '("January" "February" "March" "April" "May" "June"
13:      "July" "August" "September" "October" "November" "December"))
14:  
15:  ;; Date string function
16:  (defun gregorian-date-string (date)
17:    (let ((g-date (gregorian-from-fixed date))
18:          (weekday (day-of-week-from-fixed date)))
19:      (format nil "~a, ~a ~d, ~d"
20:        (nth weekday weekday-names)
21:        (nth (1- (second g-date)) gregorian-month-names)
22:        (third g-date)
23:        (first g-date))))
24:  
25:  ;; Get today's (Gregorian) date.
26:  (multiple-value-setq
27:    (t-second t-minute t-hour t-day t-month t-year t-weekday t-dstp t-tz)
28:    (get-decoded-time))
29:    
30:  ;; Loop through 500 Islamic years, from 250 years ago to 250 years in
31:  ;; the future and find each Ramadan 1 that corresponds to Ash Wednesday
32:  ;; and Chinese New Year.
33:  ;; Print as a Gregorian date.
34:  (setq
35:    f (fixed-from-gregorian (list t-year t-month t-day))
36:    ti-year (first (islamic-from-fixed f)))
37:  (dotimes (i 500)
38:    (setq iy (+ (- ti-year 250) i)
39:          r (fixed-from-islamic (list iy 9 1))
40:          g-year (gregorian-year-from-fixed r)
41:          aw (- (easter g-year) 46))
42:    (if (equal aw r)
43:      (let ((ny (chinese-new-year-on-or-before r)))
44:        (if (equal ny (1- r))
45:          (format t "~a~%" (gregorian-date-string r))))))
```

The `chinese-new-year-on-or-before` function (Line 43), which is in the library to aid in the writing of the typically more useful `chinese-from-fixed` function, turned out to be just what I needed here. It gets me the fixed date of Chinese New Year that’s on or before Ramadan 1. I then check to see if that’s exactly one day before Ramadan 1 in Line 44.

This script’s output was

```
Wednesday, February 6, 1799
Wednesday, February 18, 2026
Wednesday, February 16, 2124
Wednesday, February 13, 2222
```

We see that last week’s triple correspondence hadn’t occurred in 227 years, and it’ll be another 98 years before the next one. Thanks to TJ for getting me to look into this rare event.

I’ve had a copy of the second edition of *Calendrical Calculations* (called the *Millenium Edition* because it came out in 2001) for over twenty years. As I was fiddling with `ramadan-lent` and `ramadan-lent-new-year`, I ordered the fourth (or *Ultimate*) edition so I’d have the best reference on the functions in `calendar.lisp`. You can expect more posts on calendars and astronomical events as I dig into it.

[Next post](https://leancrew.com/all-this/2026/03/port-ability/)
[Previous post](https://leancrew.com/all-this/2026/02/my-omnigraffle-ticks/)