# About

After watching "Dune: Part 2", I was curious how much dialogue and subplots were cut from the book.
I have not read the book, and am unlikely to (at least in order to answer this question).
Instead, I want to consider a more general question -- how much dialogue needs to be cut to fit a reasonable runtime?

Let's count it with some code!

Assumptions:
* Dune (Part 1) and Dune: Part 2 cover about the same amount of major plot as Dune (the book)
* all words take an equal amount of time to say
* the director has a preferred words-per-minute they want to maintain
* there was no more wiggle-room in terms of extending the runtime[1]

# Dune the Book
We can get this information from an epub of Dune (the book)[2]. Note that "Dune" (part 1) and "Dune: Part 2" both are extracted from the plot of this book.

The attached notebook likely slightly overestimates the words of dialogue because there are some non-dialogue phrases between quote marks (eg: “Manual of Muad’Dib”). Fortunately, opening and closing quotes use different unicode symbols, which help increase confidences dialogue is consistently delimited.

* words of dialogue: ~71985

# Dune Part 1 (movie)

I initally asked chatgpt-4 for an estimate, and after some coaxing it said Daniel Villeneuve movies typically run at around 100-120 words per minute.

This is very wrong.

I found a screenplay (pdf) online[3], and was able to find lines of dialogue based on the x-coordinate of the first character in a line (there are no space/tab characters to indicate indentation in this document). From this, I was able to count words of dialogue by counting words on each line.

* words of dialogue: 6614
* runtime: 2h35m
* words/minute: 42.7

# Dune: Part 2 (movie)

I couldn't find a screenplay, so let's assume a similar words/minute:

* words of dialogue (derived): 7083
* runtime: 2h46m
* words/minute (copied): 42.7

# Thoughts

It seems that about 20% of the dialogue is retained (`(6614 + 7083)/71985`) (one digit of precision).

What does this mean in terms of subplots?
Prior to doing this analysis I thought the movie is a great visual spectacle[4] whose plot development felt very jagged and incomplete.
It's clear that dialogue cannot be the vehicle to fill these gaps.
As a viewer who had not read the book, many visual elements alluded to a larger world-building exercise outside the immediate plot. And this seems to have been taken at the expense of using that runtime/visual stimulus to move the plot forward.
A picture may be worth a thousand words, but in these films, the director seems content with a sort of stoic silence.

... but they are still a good, meditative experience overall.

# Setup

Use the `venv`, eg with a shell:
```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

# Running

```
(venv) PS C:\Users\Arthur\r\dunewords> python .\screenplay_dialogue.py .\dune-2021.pdf
6614
(venv) PS C:\Users\Arthur\r\dunewords> python .\dunewords.py .\dune.epub
C:\Users\Arthur\r\dunewords\venv\lib\site-packages\ebooklib\epub.py:1423: FutureWarning: This search incorrectly ignores the root element, and will be fixed in a future version.  If you rely on the current behaviour, change it to './/xmlns:rootfile[@media-type]'
  for root_file in tree.findall('//xmlns:rootfile[@media-type]', namespaces={'xmlns': NAMESPACES['CONTAINERNS']}):
Number of dialogue words: 71985
```

# Footnotes

[1] From my perspective, it seems a number of subplots are abridged in the theatrical release of Dune: Part 2. For example, Paul's surival jaunt in the desert is essentially entirely skipped.

[2] Not linked due to copyright restrictions

[3] https://d2bu9v0mnky9ur.cloudfront.net/academy2021/scripts/duneMxFtT98NYwBsMltl20211109/dune_final_shooting_script_6_19_20.pdf

[4] ... except for one 10-second shot near the end which stands out like a sore thumb.