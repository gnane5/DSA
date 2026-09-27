# Week 2 — Sep 14 to Sep 20, 2026

Two pointers. Plus closing out what week 1 left half-done.

---

## Why two pointers, not sliding window

The original Runway had sliding window here. It is being pushed to week 3,
because sliding window **is** two pointers with a condition attached — and
week 1 did not get to a single two-pointer problem. Building on a foundation
that isn't there is how week 5 falls apart.

Nothing is lost. The whole plan slides one week; it does not skip a rung.

## The target

**8 new problems**, every one teaching a distinct pattern. Plus 2 unfinished
optimal solutions carried over from week 1.

| | | |
|---|---|---|
| **Mon 14** | close week 1 | 238 O(n), Two Sum O(n), pattern page |
| **Tue 15** | 125 Valid Palindrome · 167 Two Sum II | the basic converging shape |
| **Wed 16** | 977 Squares of a Sorted Array · 88 Merge Sorted Array | reinforcement, both easy |
| **Thu 17** | 128 Longest Consecutive Sequence | best hashing problem on the sheet |
| **Fri 18** | drop night / catch-up | protected — take it if work eats the evening |
| **Sat 19** | 15 **3Sum** · 11 Container With Most Water | 3Sum is the one that shows up in real rounds |
| **Sun 20** | no new problems | pattern page + re-solve everything marked `N` |

### What each one is for

| # | Problem | Diff | Teaches |
|---|---------|------|---------|
| 125 | Valid Palindrome | E | converging pointers, the basic shape. Plus `str.isalnum()` |
| 167 | Two Sum II | M | *sortedness* is the whole difference from Two Sum — why it lets you discard half the search space each step |
| 977 | Squares of a Sorted Array | E | pointers from the outside in, filling the result **backwards** |
| 88 | Merge Sorted Array | E | merge in place from the back. Asked constantly in real rounds |
| 128 | Longest Consecutive | M | only start counting a run from a number whose predecessor isn't in the set. That one condition is what makes it O(n) |
| 15 | 3Sum | M | sort, fix one number, converge on the rest — then duplicates in all three positions, which is where everyone loses it |
| 11 | Container With Most Water | M | the *proof* matters more than the code: why is it always safe to move the shorter side? |

Budget **60–75 minutes for 3Sum** and expect to need the editorial. That is a
normal outcome for that problem, not a bad night.

## The one thing that cannot slip again

**Pull the production numbers.** It was week 1's non-negotiable and it did not
happen. It goes at lunch on Monday or Tuesday, at a desk, with prod access —
because that access disappears the day you resign.

Needed: tenant count, top tables by rows, DB size, requests/day, peak QPS,
p95 latency, Celery tasks/day, and **one slow query fixed with a before/after
timing**. The SQL is in the Runway Week One artifact.

"A tenant-scoped report went from 4.2 s to 90 ms after a composite index on
(tenant_id, created_at)" is a resume line and an answer in every backend round
this year. It cannot be reconstructed later.

## Rules carried forward

- **Start at 20:15.** Week 1 lost roughly five hours to late starts. This is
  the single highest-leverage change available.
- **Look it up before asking.** `enumerate`, `.values()`, `defaultdict` were
  all 30-second searches. Looked up, they stick; asked, they don't.
- **The 25-minute rule.** Stuck with *no approach at all* for 25 minutes →
  read the editorial, mark `unaided = N`, re-solve cold the next day. It is
  not "25 minutes then give up" — if you have an approach and you're
  debugging it, keep going, that's the valuable part.
- **Every attempt gets a log row**, and the `tell` column describes the
  **question's wording**, not what you did during the attempt.
- **Watch the recurring bug:** the final answer goes *after* the loop.
  Three times in week 1.
- **One commit per problem.** `git add .` / commit / push, from PowerShell.

## Done looks like

By Sunday Sep 20:

- [ ] 8 new problems solved and logged
- [ ] Two Sum O(n) and 238 O(n) finished
- [ ] `notes/pattern_tells.md` — all five sections written, in your own words
- [ ] Production numbers pulled and written as sentences you'd say out loud
- [ ] Everything marked `unaided = N` re-solved from an empty file on Sunday

The pattern page is the one that matters most. Ninety problems with a pattern
map beats a hundred and fifty without one.
