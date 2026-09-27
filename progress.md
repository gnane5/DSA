# NeetCode 150 — progress

Single source of truth. One row per problem. Update the status the same night
you solve it.

**Status:** `done` · `partial` (brute force only, or optimal not reached) ·
`—` (not started)

**Score: 6 done, 0 partial, 144 to go.** Plus 1 extra (169) that isn't on the
list.

Last updated: Sep 27, 2026

---

## Where the time actually goes — read this before the lists

Three weeks in, the pattern is clear and the plan was wrong, not you.

A 3h15 weeknight block starting at 20:15, after nine hours as the only backend
engineer on a production ERP, is a plan for a person who doesn't exist by
9pm. Two full weeks of zero is the evidence. A plan you don't follow isn't a
plan — it's a thing to feel bad about.

**The replacement:**

| | track 1 — DSA | track 2 — backend depth |
|---|---|---|
| **Weeknights** | **one problem, 30–45 min.** Non-negotiable but small — small enough that "I'm tired" is not a reason to skip. | — nothing. Two tracks on a weeknight is how both end up at zero. |
| **Saturday** | 3–4 problems, 3–4 hours. Where the volume lives — you already proved a 5-hour Saturday works. | **1–2 h** |
| **Sunday** | 1 hour: re-solve one problem marked `N`, update this file. No new problems. | **1 h** |

That's **6–8 problems a week** plus 2–3 hours of backend depth, and it survives
a bad Tuesday.

**Track 2 lives in `../system_design/_track_plan.md`**, next to the write-up itself. It replaces the separate "Postgres
evening block" that has had zero hours in three weeks — one track, one slot,
covering Postgres, transactions, caching, queues and system design together.
At 2–4 years for product companies that round usually carries *more* weight
than the algorithms round, and it's the one where being the sole engineer on a
live multi-tenant platform is an advantage almost nobody else has.

First four weekends of track 2: write up your own system. Not a course, not
"design Twitter." The outline is in `system_design.md`.

Two rules that make the weeknight actually happen:

1. **Open the file before you sit down to eat**, not after. The hardest part is
   opening the laptop, so do it while you're still moving.
2. **One problem means one problem.** Finish it, log it, close the laptop. Don't
   let it become "well I've only done one" — one a night is nine a fortnight,
   and you've done zero in the last fortnight.

**The honest December maths.** 145 problems at 7/week is about 21 weeks — that's
March, not December. So the 150 is not the December target and pretending
otherwise is how you end up with nothing.

**Realistic December target: the first six sections — about 45 problems.**
Arrays & Hashing, Two Pointers, Stack, Sliding Window, Binary Search, Linked
List. Those patterns cover the large majority of what actually gets asked at
2–4 years. Trees and graphs in January, DP after that. Forty-five problems with
a real pattern map beats a hundred and fifty half-remembered.

---

## Phase 1 — Arrays & Hashing (5 / 9)

| # | Problem | Diff | Pattern | Status |
|---|---------|------|---------|--------|
| 217 | Contains Duplicate | E | set / seen | **done** |
| 242 | Valid Anagram | E | frequency map | **done** |
| 1 | Two Sum | E | hash of seen (value→index) | **done** |
| 49 | Group Anagrams | M | canonical key | **done** |
| 238 | Product of Array Except Self | M | prefix × suffix | **done** |
| 347 | Top K Frequent Elements | M | bucket sort | — |
| 271 | Encode and Decode Strings | M | length-prefix framing | — |
| 36 | Valid Sudoku | M | 3 × set | — |
| 128 | Longest Consecutive Sequence | M | set | — |

**Next up here:** 128 first — it's the best problem in the section and the only
remaining one that teaches something new. Then 347. 36 and 271 are fiddly and
low-value; do them last or skip them this pass.

## Phase 2 — Two Pointers (1 / 5)

| # | Problem | Diff | Pattern | Status |
|---|---------|------|---------|--------|
| 125 | Valid Palindrome | E | converging | **done** |
| 167 | Two Sum II | M | converging on sorted | — |
| 15 | 3Sum | M | sort + converge | — |
| 11 | Container With Most Water | M | converging + proof | — |
| 42 | Trapping Rain Water | H | converging | — |

**15 (3Sum) is the one that actually shows up in real interviews.** Budget
60–75 min for it and expect to need the editorial.

## Phase 2 — Stack (0 / 7)

| # | Problem | Diff | Status |
|---|---------|------|--------|
| 20 | Valid Parentheses | E | — |
| 155 | Min Stack | M | — |
| 150 | Evaluate Reverse Polish Notation | M | — |
| 22 | Generate Parentheses | M | — |
| 739 | Daily Temperatures | M | — |
| 853 | Car Fleet | M | — |
| 84 | Largest Rectangle in Histogram | H | — |

## Phase 3 — Sliding Window (0 / 6)

| # | Problem | Diff | Status |
|---|---------|------|--------|
| 121 | Best Time to Buy and Sell Stock | E | — |
| 3 | Longest Substring Without Repeating Characters | M | — |
| 424 | Longest Repeating Character Replacement | M | — |
| 567 | Permutation in String | M | — |
| 76 | Minimum Window Substring | H | — |
| 239 | Sliding Window Maximum | H | — |

Sliding window is two pointers with a condition attached — do Phase 2 first.

## Phase 3 — Binary Search (0 / 7)

| # | Problem | Diff | Status |
|---|---------|------|--------|
| 704 | Binary Search | E | — |
| 74 | Search a 2D Matrix | M | — |
| 875 | Koko Eating Bananas | M | — |
| 153 | Find Minimum in Rotated Sorted Array | M | — |
| 33 | Search in Rotated Sorted Array | M | — |
| 981 | Time Based Key-Value Store | M | — |
| 4 | Median of Two Sorted Arrays | H | — |

This is the O(log n) section — the same shape as a btree index scan.
`-7 // 2 == -4` in Python bites on midpoints here; it's in `notes/gotchas.py`.

## Phase 4 — Linked List (0 / 11)

| # | Problem | Diff | Status |
|---|---------|------|--------|
| 206 | Reverse Linked List | E | — |
| 21 | Merge Two Sorted Lists | E | — |
| 141 | Linked List Cycle | E | — |
| 143 | Reorder List | M | — |
| 19 | Remove Nth Node From End of List | M | — |
| 138 | Copy List with Random Pointer | M | — |
| 2 | Add Two Numbers | M | — |
| 287 | Find the Duplicate Number | M | — |
| 146 | LRU Cache | M | — |
| 23 | Merge k Sorted Lists | H | — |
| 25 | Reverse Nodes in k-Group | H | — |

**146 LRU Cache is worth doing properly** — it's a real interview favourite and
it's basically a cache eviction policy, which is your world.

---

## The rest — after December

Titles only; add the LeetCode numbers as you reach each section
(neetcode.io/practice has them).

| Phase | Section | Count | Status |
|-------|---------|-------|--------|
| 5 | Trees | 15 | — |
| 6 | Tries | 3 | — |
| 6 | Heap / Priority Queue | 7 | — |
| 6 | Backtracking | 9 | — |
| 7 | Graphs | 19 | — |
| 7 | Dynamic Programming | 23 | — |
| 8 | Intervals | 6 | — |
| 8 | Greedy | 8 | — |
| 9 | Math & Geometry | 8 | — |
| 9 | Bit Manipulation | 7 | — |

**Trees (15)** — Invert Binary Tree · Maximum Depth · Diameter · Balanced ·
Same Tree · Subtree of Another Tree · LCA of a BST · Level Order Traversal ·
Right Side View · Count Good Nodes · Validate BST · Kth Smallest in a BST ·
Construct Tree from Preorder+Inorder · Max Path Sum · Serialize and Deserialize

**Intervals (6)** — Insert Interval · Merge Intervals · Non-overlapping
Intervals · Meeting Rooms · Meeting Rooms II · Minimum Interval to Include Each
Query. *Closest section to real backend work — scheduling and booking overlap.*

**Greedy (8)** — Maximum Subarray · Jump Game · Jump Game II · Gas Station ·
Hand of Straights · Merge Triplets · Partition Labels · Valid Parenthesis String

---

## Extra problems (not on the 150)

| # | Problem | Diff | Pattern | Status |
|---|---------|------|---------|--------|
| 169 | Majority Element | E | frequency map **and** Boyer-Moore O(1) space | **done**, both |

---

## Patterns owned so far

From `notes/pattern_tells.md` — 4 of 5 sections written.

1. **set / seen-so-far** — 217
2. **hash of seen (value → index)** — 1
3. **counter / frequency map** — 242, 169
4. **canonical key** — 49
5. **prefix × suffix** — 238
6. **converging two pointers** — 125

## Still owed

- [ ] Re-solve from an empty file, everything marked `unaided = N` in `log.md`:
      217, 242, 1, 169, 49, 238
- [ ] **Pull the production numbers** — tenants, table sizes, QPS, p95, and one
      slow query fixed with a before/after. Three weeks overdue and the only
      item on any of these lists that becomes impossible later, because prod
      access goes away the day you resign.
