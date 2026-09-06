"""
Four Python gotchas that bite in DSA and never in Django.

Write your prediction on the PREDICT line FIRST. Then run the file.
Anywhere you were wrong is a bug you would have shipped into a live round.

    python gotchas.py
"""

print("=" * 60)
print("1. list-of-lists aliasing")
print("=" * 60)

n, m = 3, 2
wrong = [[0] * n] * m
wrong[0][0] = 9
# PREDICT: wrong ==
print("wrong  ->", wrong)

right = [[0] * n for _ in range(m)]
right[0][0] = 9
# PREDICT: right ==
print("right  ->", right)
print("same row object?", wrong[0] is wrong[1], "|", right[0] is right[1])
# Bites in week 12 DP, and it reads like a logic bug, not a syntax one.


print()
print("=" * 60)
print("2. slicing copies")
print("=" * 60)

nums = [1, 2, 3, 4, 5]
part = nums[1:4]
part[0] = 99
# PREDICT: nums ==
print("nums   ->", nums)
print("part   ->", part)
# nums[a:b] is O(b-a) and allocates. A slice inside a loop silently turns
# your O(n) solution into O(n^2). Pass indices instead: lo, hi.


print()
print("=" * 60)
print("3. floor division on negatives")
print("=" * 60)

# PREDICT: -7 // 2 ==
print("-7 // 2   ->", -7 // 2)
# PREDICT: int(-7 / 2) ==
print("int(-7/2) ->", int(-7 / 2))
# PREDICT: -7 % 3 ==
print("-7 % 3    ->", -7 % 3)
# Python floors toward -inf; C and Java truncate toward zero.
# Bites on binary-search midpoints and on any index arithmetic that can go
# negative.


print()
print("=" * 60)
print("4. min / max initialisation")
print("=" * 60)

def largest_bad(xs):
    best = xs[0]
    for x in xs:
        best = max(best, x)
    return best

def largest_good(xs):
    best = float("-inf")
    for x in xs:
        best = max(best, x)
    return best

print("good on []  ->", largest_good([]))
# PREDICT: largest_bad([]) does what?
try:
    print("bad  on []  ->", largest_bad([]))
except Exception as e:
    print("bad  on []  ->", type(e).__name__, e)
# Empty input is the first edge case an interviewer reaches for.


print()
print("=" * 60)
print("the five-minute ones")
print("=" * 60)

# tuples are hashable, lists are not -> this is your dict key on Sunday
print('tuple(sorted("eat")) ->', tuple(sorted("eat")))
try:
    {sorted("eat"): 1}
except TypeError as e:
    print("list as key          ->", "TypeError:", e)

print("ord('a'), chr(97)    ->", ord("a"), chr(97))

a, b = {1, 2, 3}, {2, 3, 4}
print("a & b, a | b, a - b  ->", a & b, a | b, a - b)

d = {"x": 1}
print('d.get("y", 0)        ->', d.get("y", 0))

print("empty containers are falsy ->", bool([]), bool({}), bool(""))

import sys
print("recursion limit      ->", sys.getrecursionlimit(), "(matters from week 6)")
