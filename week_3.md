# Week 3 — Sep 21 to Sep 27, 2026

The week that started with nothing and ended with the most output so far.

---

## What was supposed to happen

**Nothing was planned.** Weeks 1 and 2 each had a written plan; week 3 didn't,
because `week_2.md` expired on Sep 20 and nothing replaced it.

That is not a footnote — it's the finding of the week. **Mon 21 to Thu 24
produced zero.** Work restarted on Fri 25, the day the planning documents got
rebuilt, and then three days produced more than the previous fortnight.

Carried in from week 2:

- LC 238 — brute force only, O(n) version unfinished since Sep 10
- LC 125 — started Sep 20 and abandoned at `s.lower()`
- `notes/pattern_tells.md` — 3 of 5 sections still empty comments
- the production numbers — two weeks overdue at the start of this week

## What actually happened

| day | output |
|-----|--------|
| Mon 21 – Thu 24 | nothing |
| Fri 25 | **238** — read the solution after 15 days open, typed it from memory |
| Sat 26 | **The entire Phase 1 system design write-up** — 13 sections + combined file. Plus `progress.md`, the two tracking artifacts, `week_1.md` / `week_2.md` |
| Sun 27 | **125** finished after a week stuck. **167 solved unaided.** Folder reorganised, everything committed |

### DSA — 3 problems

| # | Problem | Pattern | unaided |
|---|---------|---------|---------|
| 238 | Product of Array Except Self | prefix × suffix | N — read the editorial |
| 125 | Valid Palindrome | converging two pointers | N — four rounds of hints |
| 167 | Two Sum II | converging two pointers | **Y** |

**167 is the first Y in the log.** Seven problems in, the first one solved with
no hint about the approach — only about the output format. And the safety
argument (why it's safe to discard the largest remaining value forever) is
written down, which is the part that transfers.

### The pattern page is complete

All six sections of `notes/pattern_tells.md` now written: set/seen, hash of
seen, counter, canonical key, prefix × suffix, converging two pointers. That
was supposed to be the **week 1** deliverable. Three weeks late, but it exists —
and it's the only artefact in this repo that will still be earning in December.

### Track 2 — Phase 1 done, unprompted

Thirteen numbered sections in `system_design/` plus a 22 KB combined file,
written without being asked, with a `[N]` / `[CONFIRM]` convention that
separates "look this up" from "verify in code". Three hardest-problem stories
identified: billing engine, RM tracker, campaign auto-pause.

## What still didn't happen

- **`09_prod_numbers.md`** — still `[N]` on almost every row. **Three weeks
  overdue.** The only item on any list that becomes impossible later.
- **The `[CONFIRM]` markers** — not yet verified against the code
- **No re-solves.** Six problems are marked `unaided = N` and none has been
  re-solved from an empty file. The Sunday slot has never once been used for
  what it's for.
- **128, 347, 271, 36** — Arrays & Hashing is still 5/9

## The lesson, and it's a real one

Compare the three weeks:

| week | plan written? | problems |
|------|---------------|----------|
| 1 | yes | 5 |
| 2 | yes, but an unrealistic 3h weeknight | 1 |
| 3 | **no plan for 4 days, then a plan** | 0, then 3 in 3 days |

Week 2 failed because the plan was wrong. **Week 3's first four days failed
because there was no plan at all.** Both failure modes are cheap to avoid: a
realistic plan, written down, before the week starts.

Which is why `week_4.md` exists before Monday this time.

## Running total

**7 of 150 done** (+ 1 extra: 169). Arrays & Hashing 5/9, Two Pointers 2/5.
Six patterns documented. Phase 1 of track 2 written.
