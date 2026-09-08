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
