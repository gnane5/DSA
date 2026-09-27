# Pattern tells

One section per pattern. The tell, why it works, a template you can type from
memory, the cost, and the problems that taught it.

This page is the revision asset. In December you reread this, not the code.

| what the question says | reach for |
|------------------------|-----------|
| "has any duplicate", "seen before", "count of each" | set / Counter |
| "pair that sums to k" on an *unsorted* array | hash of seen |
| "group the ones that are the same in some sense" | canonical key |
| "everything except this one" | prefix x suffix |
| array is *sorted*, want a pair or a window from both ends | two pointers |

**The first question to ask about any array problem:**
*is it sorted, and am I allowed to sort it?*
Sorting costs O(n log n) and buys you two pointers - often a straight win over
an O(n^2) scan, and almost always the thing the interviewer is waiting to hear.

---

## Templates

### set / seen-so-far

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

**The tell.** Same as above, except the answer needs *which position*, not just
*whether*. "Return the indices", "return the pair", "how far apart were they".
A set can't do this - a set only remembers that a value existed.

**Why it works.** For each element you need to find some *other* element -
usually `target - x`. Searching the array for it is O(n) (`x in nums` and
`nums.index(x)` are both full scans), which makes the whole thing O(n^2).
A dict of what you have already passed makes that search O(1).

Frame it the way it actually is: **the dict is an index on the array.** A
Postgres table already contains every row, and you still add an index - having
the data and having fast access to it are different things. `nums.index(x)` is
a Seq Scan.

**The key insight that took me longest.** You never look forward. You only
look backward, at what you have already stored - and every pair still gets
found, at the moment you reach its SECOND member. So two elements at opposite
ends of the array are found in one pass, when you arrive at the later one.

    nums = [2, 5, 7, 3, 4], target = 6   ->  answer [0, 4]

    at | value | I need | seen it?   | then
    ---+-------+--------+------------+------------------
     0 |   2   |   4    | no         | remember 2 -> 0
     1 |   5   |   1    | no         | remember 5 -> 1
     2 |   7   |  -1    | no         | remember 7 -> 2
     3 |   3   |   3    | no         | remember 3 -> 3
     4 |   4   |   2    | YES, at 0  | answer [0, 4]

**The template.**

    seen = {}                        # value -> index
    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return [seen[need], i]
        seen[nums[i]] = i            # store AFTER checking
    return []

**Which way round the dict goes.** You search by the *value* (`is need in
seen?`), and a dict searches by its KEY - so the key is the value. What you
want back is the position, so the value is the index.

**Check before storing.** Store first and `nums=[3,3], target=6` returns
`[0,0]` - the same element used twice.

**Cost.** O(n) time, O(n) space.

**Taught by.** LC 1 Two Sum.

### counter / frequency map

**The tell.** The question is about *how many of each*, not just *whether*.
Words like "anagram", "same characters", "appears k times", "most frequent",
"majority", "rearranged to form". The moment presence isn't enough and you
need the count, it's this.

**Why it works.** One pass builds a dict of `value -> count`, O(n). After that
every "how many x?" is O(1). The alternative is calling `.count()` per element,
which re-scans the whole input every time - O(n^2) with one visible `for`.

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

**Taught by.** LC 242 Valid Anagram, LC 169 Majority Element.

### canonical key

**The tell.** "Group the ones that are the SAME in some sense." Anagrams,
duplicates by content, files with identical bytes, shapes that match after
rotation.

**Why it works.** The instinct is to compare every item against every other -
n^2/2 comparisons. Instead, compute for each item ONE value that every member
of its group produces identically, and use that as a dict key. The dict does
all the matching, O(1) per item, zero comparisons.

**The template.**

    from collections import defaultdict
    groups = defaultdict(list)
    for item in items:
        key = fingerprint(item)      # same for every member of a group
        groups[key].append(item)
    return list(groups.values())

For anagrams the fingerprint is `"".join(sorted(word))` - eat, tea and ate all
give `aet`. `sorted()` returns a LIST, which is unhashable, so join it into a
string (or `tuple(sorted(word))`).

**Sorting is not the point.** A 26-length tuple of letter counts is also a
valid fingerprint and it's O(k) instead of O(k log k). The pattern is "compute
a canonical key"; sorting is one implementation of it.

**Cost.** O(n * cost of one fingerprint). For anagrams, O(n * k log k) time,
O(n * k) space.

**Taught by.** LC 49 Group Anagrams.

### prefix x suffix scan

**The tell.** "Sum / product / max of everything EXCEPT this one", for every
position. Or anything where the answer at position i depends on one side of it
and the other side separately.

**Why it works.** The brute force recomputes the same sub-products over and
over - for `[1,2,3,4]` it multiplies 3x4 twice and 1x2 twice. A running
accumulator computes each sub-product once. Two passes replace n^2 work.

**The idea.** For any position the answer splits in two:
*everything to its left* x *everything to its right*.

    nums:        1    2    3    4
    left of i:   1    1    2    6      <- running product, forwards
    right of i:  24   12   4    1      <- running product, backwards
    answer:      24   12   8    6      <- left[i] * right[i]

**The template** (O(1) extra space - the output array doesn't count):

    out = [1] * n

    prefix = 1
    for i in range(n):
        out[i] = prefix              # everything to the left so far
        prefix *= nums[i]            # nums, NOT out

    suffix = 1
    for i in range(n-1, -1, -1):
        out[i] *= suffix             # multiply in everything to the right
        suffix *= nums[i]

    return out

**The mirror.** With two explicit arrays the two lines are exact reflections:
`left[i] = left[i-1] * nums[i-1]` and `right[i] = right[i+1] * nums[i+1]`.
Each says "take the previous answer and multiply in the element I just stepped
over". `i-1` <-> `i+1` is the whole swap. The first and last cells stay at the
identity (1 for products, 0 for sums) because there is nothing on that side.

**The bug to watch.** `prefix *= out[i]` instead of `prefix *= nums[i]`. It
runs, it's silent, and it leaves pass 1 as all 1s. The accumulator accumulates
the INPUT.

**This is not two pointers.** Two pointers means at every step you DECIDE
which pointer to move based on a comparison. Here there is no comparison and
no choice - just two full passes. Walking forwards then backwards is not the
same as two converging pointers.

**Cost.** O(n) time, O(1) extra space.

**Taught by.** LC 238 Product of Array Except Self.

### converging two pointers

**The tell.** "Is it the same forwards and backwards." "A pair that sums to
k" on a *sorted* array. "The largest area between two lines." Anything where
the answer comes from a pair taken from opposite ends of a sequence, and you
can throw one candidate away after looking at it.

**What makes it two pointers and not two passes.** At each step you DECIDE
which pointer to move, and that decision comes from a comparison. If there's
no decision - you just walk forwards, then backwards - that's prefix x suffix,
not this. That is the line 238 sits on the other side of.

**Why it works.** Sorted input (or symmetry, as in a palindrome) means one
comparison tells you which end cannot possibly be part of the answer, so you
discard it. Each element is looked at once: O(n) instead of the O(n^2) of
checking every pair.

**The template.**

    x, y = 0, len(a) - 1
    while x < y:
        if <skip condition on x>:
            x += 1
            continue
        if <skip condition on y>:
            y -= 1
            continue
        if <the pair is what I want>:
            return / record, then move both
        else:
            move whichever side the comparison says to discard

**Three things that are always the same.**

1. `while x < y`, not `<=`. At x == y both pointers are on the same element,
   which always matches itself. Stopping there handles odd length, even
   length, and empty input with zero special cases.
2. `continue` after a skip. The next character might be junk too ("a,,b") -
   go back to the top and re-check rather than comparing blind.
3. The negative answer returns from *inside* the loop, the positive answer
   from *after* it. You only know it IS a palindrome once you've looked at
   everything; you know it isn't the moment one pair fails.

**The proof half.** For 11 Container With Most Water the code is four lines
and the interesting part is the argument: why is it always safe to move the
*shorter* side? Be able to say that in two sentences - the proof is the
question, not the code.

**In place, or build a new array?** This decides whether you need a third
index, and it caught me for five rounds on LC 977.

A swap requires knowing BOTH destinations. Walking from the ends you only ever
know ONE - where the largest goes, which is last. You have no idea yet where
anything else belongs. So:

    every slot still holds data I need   ->  write into a NEW array
    destination known, or free space     ->  in place

LC 977 needs a new array (every slot in nums is still live). LC 88 Merge Sorted
Array does NOT - the padding at the end is already free. LC 283 Move Zeroes
does not either. Same backwards-fill trick, opposite answer on the array.

When you do build a new array you get a third index - a WRITE CURSOR. It is not
a third pointer: it moves by one every pass, unconditionally, and no comparison
touches it. Two pointers decide; the cursor just counts.

**Cost.** O(n) time, O(1) space. The naive version of a palindrome check
builds a reversed copy, which is O(n) space - that's the trade this pattern
removes.

**Taught by.** LC 125 Valid Palindrome (symmetry) and LC 167 Two Sum II
(sortedness). Next: 15 3Sum, 11 Container With Most Water.

**The 167 lesson, worth keeping separate.** Unsorted, I must remember what I
have passed -> hash map, O(n) space. Sorted, the array itself tells me which
direction is bigger -> two pointers, O(1) space. *Sortedness replaces the hash
map.* The word "sorted" in an array problem is almost always the hint.
