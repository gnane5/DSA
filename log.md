# Attempt log

One row per attempt. Failed attempts count. Re-solves get their own row.

`unaided` - Y if you got there with no editorial, no hints, no notes.
`min` - wall-clock minutes on the attempt.
`the tell` - **the column that matters.** What in the question's *wording* told
you which pattern to reach for. In your own words, every time, even the easy
ones. In week 13 you reread this column, not the code.

| date  | #   | problem           | pattern          | unaided | min | the tell |
|-------|-----|-------------------|------------------|---------|-----|----------|
| 09-05 | 217 | Contains Duplicate | brute: 2 loops  | Y       | ?   | first instinct - compare everything to everything. O(n^2), too slow, and I was comparing elements with themselves |
| 09-06 | 217 | Contains Duplicate | set / seen       | N       | ?   | "does the array contain any duplicate" = a yes/no about repeats. Repeats -> I need to remember what I've already seen -> set, because `in` on a set is O(1) |
| 09-06 | 242 | Valid Anagram | frequency map | N | 30min | i had taken the hind on dict to solve this first i was comaparing it with 2 for loop no the dict|
| 09-06 | 1   | Two Sum | brute: 2 loops (O(n) TODO) | N | 30min   | "two numbers that add up to target", unsorted, wants the INDICES back -> for each x find target-x elsewhere. Brute force checks every pair. Parked the O(n) hash version for a re-solve - I could not see how one pass finds a pair that is far apart |
| 09-08 | 169 | Majority Element | frequency map | N | ?   | "appears more than n/2 times" -> counts, not presence -> same dict I built for 242. max(c, key=c.get) picks the key with the biggest value. O(n) time, O(n) space |
| 09-08 | 169 | Majority Element | boyer-moore vote | N | ?   | "MORE THAN half" is a stronger promise than "most frequent" - cancel any two differing elements and the majority can never be fully cancelled. Candidate + counter, O(n)/O(1), which is optimal here |
| 09-09 | 49  | Group Anagrams | canonical key | N | ?   | "group the ones that are the SAME in some sense" -> do NOT compare pairs, compute one value every member of a group produces identically and let a dict group them for free. "".join(sorted(word)) is just one way to build that key - a 26-length count tuple works too and is faster. The pattern is the key, not the sorting |
| 09-10 | 238 | Product Except Self | brute: 2 loops | Y | ?   | "product of everything except this one" -> for each position, multiply all the others. Accumulator starts at 1 not 0 (identity for multiplication). Bug: append was inside the inner loop, so it appended the half-built product - third time I've done that |
| 09-14 | 1   | Two Sum | hash of seen (value -> index) | N | ?   | needs the INDICES back, so a set is not enough - I need WHERE I saw it, which means a dict. Took 4 attempts and reading the solution: I kept searching `nums` itself (`in nums`, `nums.index()`), both O(n) scans. The dict IS an index on the array - same reason you index a Postgres table that already has the rows |
| 09-25 | 238 | Product Except Self | prefix x suffix | N | ?   | "everything EXCEPT this one" -> the answer at i splits into (everything left) x (everything right), and each side is a running accumulator computed in one pass. Division is banned, which is the hint that this is the intended shape. Typed it from memory and had `prefix *= out[i]` instead of `nums[i]` - the accumulator accumulates the INPUT |

| 09-27 | 125 | Valid Palindrome | converging two pointers | N | ?   | "same forwards and backwards" -> a pair from opposite ends -> one pointer each end, walking inward. What makes it two pointers and not two passes: each step I decide WHICH pointer to move, from a comparison. Four rounds: forgot to compare at all, indexed s instead of c, handled only the match branch (infinite loop on "race a car"), and print(True) inside the loop for the 7th time |
| 09-27 | 167 | Two Sum II | converging two pointers | Y | ?   | "two numbers that add to target" AND the array is SORTED -> two pointers, not a hash map. Sortedness replaces the dict: unsorted I must remember what I passed (O(n) space), sorted the array itself tells me which way is bigger (O(1) space). Safe to discard because numbers[y] is the LARGEST left - if that sum is already too big, y pairs with nothing remaining. FIRST ONE UNAIDED; only hints were the 1-indexed output format (LC 1 is 0-indexed, 167 is not) |
| 09-27 | 977 | Squares of a Sorted Array *(extra)* | converging + backwards fill | N | ?   | sorted input, but squaring breaks the order symmetrically -> the extremes become the largest -> two pointers from the ends, filling the answer BACKWARDS, because the only thing I can ever name is the largest remaining. Six rounds, five of them spent trying to swap in place: a swap needs BOTH destinations and I only ever know one. No free space in nums = build a new array. Also: this is a MERGE of two ordered runs, not a sort - which is why it's O(n) and not O(n log n) |
---

## Still open

- **Re-solve from an empty file**, everything marked `unaided = N`:
  217, 242, 1, 169, 49, 238, 125. That is all of them but two.
- **128 Longest Consecutive Sequence** - best remaining problem in Arrays &
  Hashing, and the only one left there that teaches something new.
- **09_prod_numbers.md** in the system_design folder - still `[N]` on almost
  every row, and the only thing on any of these lists that expires.

## My recurring bug

**The final answer placed inside the loop instead of after it.** Four times
now: `return False` on 217, `print` on 49, `append` on 238, `break` on Two Sum.
Check the indentation of the last line of every solution before running it.
