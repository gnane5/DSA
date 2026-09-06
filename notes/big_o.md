# Complexity — the reference

Interactive version (slider, live numbers):
https://claude.ai/code/artifact/c5a7d15f-5480-45e0-b414-c40b7f9079d2

---

## 1. What the O means

It's the **letter O**, not a zero. It stands for **order** — as in *order of
growth*. `O(n)` is read "order n".

It answers exactly one question:

> **When the input gets bigger, how fast does the work grow?**

Not seconds. Not how fast your laptop is. Just the shape of the curve.

| input doubles, and the work...     | that's   |
|------------------------------------|----------|
| doesn't change                     | O(1)     |
| goes up by one step                | O(log n) |
| doubles                            | O(n)     |
| a bit more than doubles            | O(n log n) |
| goes up 4x                         | O(n^2)   |
| squares                            | O(2^n)   |

This is why constants get thrown away. `2n` and `n` both double when the input
doubles — same shape, so both are O(n). A solution 3x slower with a better
shape beats a faster one with a worse shape on every input that matters.

---

## 2. The four-step recipe

**1. Name your n.**
Usually `len(nums)`. Say it out loud. If there are two inputs you have an `n`
AND an `m`, and you can't pretend otherwise.

**2. Count how many times the innermost work runs, in terms of n.**
Not lines of code — iterations.
One loop over the input = n. A loop inside a loop = n x n.
A loop that halves its range each step = log n.

**3. Drop constants and smaller terms.**
`3n^2 + 5n + 100` -> **O(n^2)**. At n = 1,000,000 the n^2 term is a million
times bigger than the n term. Nothing else is worth writing down.

**4. Check what's INSIDE the loop.**
The step everyone skips and the one that gets them. A single `for` loop
containing an operation that is itself O(n) is **O(n^2)**. See section 5.

---

## 3. The numbers, so it stops being abstract

Operations performed, by shape and input size:

|         n | O(log n) |         O(n) |   O(n log n) |             O(n^2) | O(n^2) takes |
|----------:|---------:|-------------:|-------------:|-------------------:|-------------:|
|       100 |        7 |          100 |          665 |             10,000 |      instant |
|     1,000 |       10 |        1,000 |        9,966 |          1,000,000 |        10 ms |
|    10,000 |       14 |       10,000 |      132,878 |        100,000,000 |        1.0 s |
|   100,000 |       17 |      100,000 |    1,660,965 |     10,000,000,000 |      1.7 min |
| 1,000,000 |       20 |    1,000,000 |   19,931,569 |  1,000,000,000,000 |    2.8 hours |

Look at the O(log n) column. **Going from 100 items to a million costs you
13 extra steps.** That's what a btree index buys you, and it's why binary
search matters.

**Rule of thumb: ~10^8 operations is about one second.**

### The constraints are telling you the answer

Every LeetCode problem lists constraints. `n <= 10^5` means O(n^2) is 10^10
operations — it will time out, and that's deliberate. The constraint is the
problem quietly telling you which shape it wants.

**Read the constraints before you write a line.**

---

## 4. Worked: LC 217, both of my solutions

### Version A — nested loops

    for i in range(len(nums)):            # runs n times
        for j in range(i + 1, len(nums)): # runs ~n times for each i
            if nums[i] == nums[j]:        # <- the work
                return True
    return False

Outer runs n times. Inner runs (n-1), then (n-2), ... down to 1.
Total = n(n-1)/2 comparisons = n^2/2 - n/2.
Drop the constant and the lower term -> **O(n^2) time**.
Allocates nothing that grows -> **O(1) space**.

### Version B — the set

    s = set()             # 1 op
    for i in nums:        # runs n times
        if i in s:        # O(1) each  -> n
            return True
        s.add(i)          # O(1) each  -> n
    return False

2n + 1 operations -> **O(n) time**.
The set can grow to hold every element -> **O(n) space**.

Step 4 is what makes this true: `in` on a **set** is O(1). If `s` were a list
it would be O(n), and this identical-looking code would be O(n^2).

### Name the trade

O(n^2) time / O(1) space  ->  O(n) time / O(n) space.

There's no free lunch here — **I spent memory to buy time.** Every good
data-structure choice is a trade like this, and saying which one you made is
most of what separates "solved it" from "understands it".

---

## 5. Hidden costs — not every loop has a `for`

| operation                | cost      | why |
|--------------------------|-----------|-----|
| `x in my_list`           | O(n)      | a list doesn't know what it holds; it walks from the front |
| `x in my_set` / `dict`   | O(1)      | hashes straight to a bucket address, no scan |
| `my_list.pop(0)`         | O(n)      | shifts every remaining element left one slot; use `deque` |
| `my_list.pop()`          | O(1)      | removing from the end shifts nothing |
| `nums[a:b]`              | O(b-a)    | a slice **copies**; inside a loop this makes O(n) into O(n^2) |
| `s += t` in a loop       | O(n^2)    | strings are immutable — each += builds a whole new string |
| `sorted(nums)`           | O(n log n)| Timsort. Often worth paying — sorting buys you two pointers |
| `min/max/sum(nums)`      | O(n)      | one pass each; three of them in a loop is 3x O(n^2), not O(n) |

**The one-word demo.** Take my working 217 solution and change `s = set()` to
`s = []`. Still runs. Still correct. Still one visible `for` loop. Now O(n^2) —
100,000 elements goes from 10 ms to about 100 seconds.

That is why `python_costs.md` exists.

---

## 6. I already know this from Postgres

| what the plan says      | shape      | same idea as |
|-------------------------|------------|--------------|
| Seq Scan                | O(n)       | reads every row — exactly `x in my_list` |
| Index Scan (btree)      | O(log n)   | halves the search space per level; 2M rows ~ 21 steps. This is binary search |
| Nested Loop join        | O(n x m)   | my first 217 attempt, with tables instead of arrays |
| Hash Join               | O(n + m)   | builds a hash table of one side, streams the other past it — **literally my set solution** |
| Sort node               | O(n log n) | same cost as `sorted()`; why `ORDER BY` on an unindexed column shows up in slow queries |

Adding a composite index so a Seq Scan becomes an Index Scan is converting
O(n) into O(log n) on a two-million-row table. Same move as swapping a list
for a set. I've done this at work — I just haven't had to name it in an
interview yet.

---

## 7. Space complexity

Same recipe, but count **extra memory allocated**, as a function of n.

- a set that can hold every element -> O(n)
- three integer variables -> O(1), however big the input

Two conventions, so nobody corrects me mid-round:

- the **output** I'm asked to return usually doesn't count — I had no choice
- the **recursion stack** always does — n frames deep is O(n) space
  (starts mattering in week 6 when trees arrive)

---

## 8. What to say in a round

Before writing any code:

> "Brute force is nested loops — O(n^2) time, O(1) space.
>  I think I can get O(n) time with a set, at the cost of O(n) space.
>  Want me to go straight to that?"

Three sentences. Most candidates can't produce them under pressure.
Say them every single time until they're automatic.
