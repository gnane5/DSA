# Pattern tells

You write this page, from your own log, in your own words.
The first pattern below is filled in as a worked example - that's the shape.
The other three are yours, and by Sunday Sep 13 this page is the real
deliverable of week 1.

| what the question says | reach for |
|------------------------|-----------|
| "has any duplicate", "seen before", "count of each" | set / Counter |
| "pair that sums to k" on an *unsorted* array | hash of seen |
| array is *sorted*, want a pair or a window from both ends | two pointers |

**The first question to ask about any array problem:**
*is it sorted, and am I allowed to sort it?*
Sorting costs O(n log n) and buys you two pointers - often a straight win over
an O(n^2) scan, and almost always the thing the interviewer is waiting to hear.

---

## Templates

Five to eight lines you can type from memory, plus the problems that taught it.

### set / seen-so-far          [worked example]

**The tell.** The question asks whether something has *already appeared*.
Words like "duplicate", "seen before", "already exists", "repeated". Any time
the answer to "have I met this before?" would solve it.

**Why it works.** Checking "have I seen this?" against a list is O(n) - the
list scans. Against a set it's O(1) - it hashes straight to the answer. That
single difference turns a nested loop into one pass.

**The template.**

    seen = set()
    for x in nums:
        if x in seen:
            return True        # or: do the thing
        seen.add(x)
    return False

**The two moving parts.** Check *before* you add - flip those two lines and
every input matches itself. And the negative answer (`return False`) goes
*after* the loop, because you only know there's no duplicate once you've seen
everything.

**Cost.** O(n) time, O(n) space. You are spending memory to buy time. Say that
trade out loud in an interview.

**Taught by.** LC 217 Contains Duplicate.

### hash of seen-so-far  (value -> where I saw it)

<!-- Two Sum will teach you this one. It's the same idea as above, except you
     store *where* you saw each value, not just that you saw it. Write this
     section after you solve LC 1. -->

### counter / frequency map

**The tell.** The question is about *how many of each*, not just *whether*.
Words like "anagram", "same characters", "appears k times", "most frequent",
"majority", "rearranged to form". The moment presence isn't enough and you
need the count, it's this.

**Why it works.** One pass builds a dict of `value -> count`, O(n). After that
every "how many x?" is O(1). The alternative is calling `.count()` per element,
which re-scans the whole input every time — O(n^2) with one visible `for`.

**The template.**

    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1

    # once you trust yourself:
    from collections import Counter
    counts = Counter(items)

**Comparing two of them.** `a == b` on two dicts compares keys *and* values in
one operator - and it catches "one side has an extra key" for free, so you
don't need a separate length check.

**Cost.** O(n) time. Space is O(k) where k = number of *distinct* values.
When the problem says lowercase English letters only, k <= 26, which doesn't
grow with n - so that's **O(1) space**. Saying that out loud is a good answer.

**Taught by.** LC 242 Valid Anagram.

### prefix x suffix scan

<!-- LC 238 Product of Array Except Self. Write it after that. -->

### converging two pointers

<!-- LC 125, 167, 977, 15. Write it Wednesday-Thursday. -->
