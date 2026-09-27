# Week 4 — Sep 28 to Oct 4, 2026

**The goal: finish Phases 1 and 2 completely.** Arrays & Hashing 9/9,
Two Pointers 5/5. That is 14 of the 150 and two whole sections closed.

Written on Sunday Sep 27, before the week starts — because week 3 proved that
four days with no plan produce nothing.

---

## Where you start the week

| | |
|---|---|
| Done | 7 of 150 (+169 as an extra) |
| Arrays & Hashing | 5 / 9 — need **128, 347, 271, 36** |
| Two Pointers | 2 / 5 — need **15, 11, 42** |
| Patterns documented | 6 of 6 for what's learned so far |
| Track 2 Phase 1 | written; blocked on `09_prod_numbers.md` |

## The DSA week — 6 new problems

Order is deliberate: highest-value first, fiddliest last, the hard one on
Saturday when you're fresh.

| day | problem | diff | what it teaches |
|-----|---------|------|-----------------|
| **Mon 28** | **15 3Sum** *(or 11, if you finished 3Sum on Sun 27)* | M | sort + fix one + converge. The one that actually shows up in interviews. Budget 60–75 min and expect to read the duplicate handling |
| **Tue 29** | **11 Container With Most Water** | M | the **proof** matters more than the code: why is it always safe to move the *shorter* side? Same argument shape you already wrote down for 167 |
| **Wed 30** | **128 Longest Consecutive Sequence** | M | best problem left in Arrays & Hashing. The insight: only start counting a run from a number whose predecessor isn't in the set. That one condition is what makes it O(n) |
| **Thu Oct 1** | **347 Top K Frequent Elements** | M | bucket sort, **not** a heap. Heaps are Phase 6 — the bucket version is O(n) anyway. Know the heap version exists and why you didn't need it |
| **Fri Oct 2** | drop night / catch-up | | protected. Take it if work eats the evening — that is the plan working, not failing |
| **Sat Oct 3** | **42 Trapping Rain Water** (H) + **36 Valid Sudoku** (M) | H+M | 42 defeats almost everyone cold — the 25-minute rule applies with force. Learn the two-pointer version; the stack version can wait. 36 is just three sets of constraints in one pass |
| **Sun Oct 4** | no new problems | | re-solves + week close (see below) |

**271 Encode and Decode Strings** is the one to drop if the week gets tight.
It's LeetCode Premium (solve it on neetcode.io or Lintcode 659) and it's
secretly a protocol-design question — length-prefix each string so any
character can appear in the payload. You've written serializers; it's a 20
minute problem when you get to it.

### Two extras worth 30 minutes total, not on the 150

- **977 Squares of a Sorted Array** (E) — pointers from the outside in,
  **filling the result backwards**
- **88 Merge Sorted Array** (E) — merge in place from the back; the backwards
  fill is the only reason it's O(1) space

Neither advances the 150 count. Both teach the backwards-fill trick, which is
genuinely useful and appears in real interviews constantly. Do them as a warm-up
on a low-energy night rather than skipping the night entirely.

## Sunday Oct 4 — the slot that has never been used

Three weeks in, the Sunday re-solve has happened **zero** times, and six
problems sit marked `unaided = N`. This week it actually happens:

- [ ] Re-solve from an empty file, no notes: **238** and **1** (the two you
      had to read). One hour, both, log each as a new row.
- [ ] If a re-solve fails twice, flag it for December revision rather than
      grinding a third attempt.
- [ ] Update `progress.md` and tick the tracker artifact
- [ ] Write `week_5.md` **before Monday**. That is the whole lesson of week 3.

## Track 2 — backend depth (Sat 1–2 h, Sun 1 h)

**Saturday's first hour is `09_prod_numbers.md`, and nothing else until it's
done.** Three weeks overdue. Every other item on every list in this repo can be
done in any order at any time; this one stops being possible the day you resign.

What it needs: tenant/client counts, top 5 tables by rows, DB size,
requests/day and peak QPS, p95 (or "not instrumented" plus what you'd add),
Celery tasks/day, and **one slow query fixed with before/after timings**.

Then, in order:

1. Clear the `[CONFIRM]` markers — verify each against the code, delete the marker
2. Make sure some section explains **why ~50% of the GPS pings don't arrive**.
   25–30k/day with half dropped is one of your best stories and right now it's
   a statistic, not an explanation.
3. Start Phase 2 topic 1: **Postgres indexes** — B-tree internals, composite
   column order and the leftmost-prefix rule, partial, covering, and reading
   `EXPLAIN (ANALYZE, BUFFERS)`. Run the unused-index query on your own DB and
   count what you're paying write cost for.

## Cadence (unchanged — it's the one that works)

| | track 1 — DSA | track 2 |
|---|---|---|
| Weeknights | one problem, 30–45 min. Open the laptop **before** dinner | nothing |
| Saturday | 2 problems, 3 h | 1–2 h |
| Sunday | re-solves only, 1 h | 1 h |

## Done looks like

- [ ] **Arrays & Hashing 9/9** (or 8/9 with 271 deferred)
- [ ] **Two Pointers 5/5**
- [ ] 14 of 150 (or 13)
- [ ] 238 and 1 re-solved cold and logged as new rows
- [ ] `09_prod_numbers.md` has real numbers in it
- [ ] `week_5.md` written before Mon Oct 5

Two sections finished, and the first Y-heavy week if the re-solves land.
