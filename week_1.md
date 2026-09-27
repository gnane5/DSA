# Week 1 — Sep 5 to Sep 13, 2026

Arrays & Hashing. Started from zero on DSA.

---

## Target vs actual

|                    | target | actual |
|--------------------|--------|--------|
| New problems       | 19     | **6 touched, 4 finished** |
| Patterns learned   | 4      | **4** |
| Postgres blocks    | 5 evenings | **1 (15 min reading)** |
| Production numbers pulled | yes — "cannot slip" | **no** |

Problem count came in at about a quarter of target. Pattern count came in at
100%. Those two facts together are the whole story of the week.

## What got solved

| # | Problem | Brute force | Optimal | Status |
|---|---------|-------------|---------|--------|
| 217 | Contains Duplicate | O(n²) / O(1) | set, O(n) / O(n) | done |
| 242 | Valid Anagram | `.count()` O(n²) | freq dict, O(n) / O(1) | done |
| 1 | Two Sum | O(n²) / O(1) | hash of seen | **brute only** |
| 169 | Majority Element | — | dict O(n)/O(n) **and** Boyer-Moore O(n)/O(1) | done, both |
| 49 | Group Anagrams | O(n²·k) | canonical key, O(n·k log n) | done |
| 238 | Product Except Self | O(n²) / O(1) | prefix × suffix | **brute only** |

Four patterns now in hand:

1. **set / seen-so-far** — 217
2. **counter / frequency map** — 242, 169
3. **canonical key** — 49
4. **hash of seen (value → index)** — Two Sum, *not finished*
5. **prefix × suffix** — 238, *not finished*

## What actually got learned

None of this was in the 19-problem target, and all of it was missing on Sep 5.

- **Big-O from nothing** — what the O means, the four-step recipe, time vs
  space as two separate questions answered with the same notation
- **Lower bounds** — if you must read every element, O(n) is the floor and
  you stop optimising. Knowing when to stop is half of it.
- **Preconditions** — tested LC 169's algorithm on an array with no majority
  element and watched it return garbage. Constraints are the contract the
  algorithm relies on, not decoration.
- **Index arithmetic** — `range(len(nums))` vs `enumerate`, positions vs
  values, `j = i + 1` to stop self-pairing and duplicate pairs
- **Dicts three ways** — explicit if/else, `.get(k, 0)`, `defaultdict`
- **Hashable vs unhashable** — why a list can't be a dict key and a tuple or
  string can
- **Boyer-Moore majority vote** — derived from a hint about cancelling pairs,
  not looked up. First algorithm built from an idea rather than a template.

That bill is paid once. It does not come again in week 2.

## Recurring bugs — worth watching for

1. **The final answer placed inside the loop instead of after it.**
   Three times: `return False` on 217, `print` on 49, `append` on 238.
   Rule: the answer is only known once the loop has finished.
2. **Silent no-op arithmetic.** `c+-1` is `c + (-1)`, computed and thrown
   away — no error. `c=-1` assigns instead of subtracting. Only `c-=1` works.
3. **Values where positions belong, and vice versa.** Added `i + j` (two
   indices) instead of `nums[i] + nums[j]`, then reversed it.
4. **One passing test proves nothing.** The broken decrement on 169 passed
   the first test case by luck. `[1,2,2,2]` was what exposed it.

## Speed — the real signal

| problem | time |
|---------|------|
| Two Sum (brute) | ~2 hours, heavy hints |
| 242 | ~1 hour |
| 169, both versions | ~45 min |
| 49 — a **medium** | ~45 min, concept found unaided |

That is real acceleration, and it is the reason the low problem count is not
the alarm it looks like.

## What did not happen

- **Two Sum O(n)** — parked Sep 6, still parked
- **238 O(n)** — brute force only
- **`notes/pattern_tells.md`** — 3 of 5 sections still empty comments
- **The production numbers pull** — the one item the Runway flagged as
  unable to slip, because prod access disappears the day you resign.
  Still not done. Goes at the top of week 2.
- The Postgres evening blocks (composite indexes, EXPLAIN plans)

## Two diagnoses, both fixable

1. **Late starts.** Sessions began 21:30–22:00 against a 20:15 plan. That is
   an hour a night, five hours a week — more than a whole problem-evening,
   lost before sitting down.
2. **Asking before attempting.** The 25-minute rule barely fired all week.
   Roughly half of what got asked — `enumerate`, `.values()`, `defaultdict` —
   was a 30-second search. Looked up yourself, those stick. Asked, they don't.

## Verdict

Week 1 was a foundations week wearing a problem-count week's clothing. The
foundation is real and now built. Week 2 has no such excuse in it — the test
is whether 8 problems land, and whether the pattern page gets written.
