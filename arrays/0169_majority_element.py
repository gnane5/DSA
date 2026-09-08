"""
LC 169 - Majority Element
https://leetcode.com/problems/majority-element/

Pattern: frequency map, then Boyer-Moore majority vote

THE GUARANTEE - read this first:
    The majority element appears STRICTLY MORE than n/2 times, and the problem
    promises one always exists. Both halves of that matter. Version 2 below is
    only correct BECAUSE of that promise.

    I tested [2,4,5,6,4,4,4,7,8,7,2,1] - n=12, so a majority needs a count > 6,
    and the best is 4 appearing 4 times. No majority exists. Boyer-Moore returns
    2 on it, which appears twice. That is not a bug in the algorithm, it is a
    VIOLATED PRECONDITION. Constraints are the contract the algorithm relies on.

    If I ever needed to handle "maybe no majority": run version 2 to get a
    candidate, then one more pass counting how often it actually appears.
    Still O(n) time, still O(1) space.

Version 1 - frequency dict:
    Count every value, return the key with the largest count.
    `max(c, key=c.get)` walks the keys but RANKS each one by its value
    instead of by the key itself. Same `key=` argument as sorted().
    Time O(n)   Space O(n) - one dict entry per distinct value

    Careful: this actually answers "most frequent element", which is a
    DIFFERENT question from "majority element". They only coincide when a
    majority exists.

Version 2 - Boyer-Moore majority vote:
    The idea, which I got to from the pairing hint rather than looking it up:
    repeatedly delete any TWO elements that differ from each other. Each
    deletion removes at most ONE majority element, and the majority is more
    than half the array - so it can never be fully cancelled out. Whatever
    survives is the majority.

    In code that's a candidate + a counter. Count hits zero -> the current
    element becomes the new candidate.
    Time O(n)   Space O(1)

    This is OPTIMAL. You must read every element to answer (skip one and it
    could have been the answer), so O(n) time is the floor for this problem.
    O(1) space is as low as space goes. Nothing better exists.

Three near-misses on the decrement, all silent:
    c+-1   -> Python reads this as c + (-1). It computes the value and throws
              it away. No error, no warning. The count never went down, so the
              candidate was never replaced. It still passed my one test case
              by luck, because the majority happened to come first.
              -> One passing test proves nothing. Find the failing case.
    c=-1   -> assigns minus one instead of subtracting. Count never reaches 0
              again, so a new candidate is never picked.
    c-=1   -> correct.

Also tried putting c and d in the method signature as `def f(self, nums, c=0,
d=0)`. It passes, but it changes the function's CONTRACT - it now advertises
three inputs when the problem defines one. And defaults are evaluated once at
definition time, so `seen=[]` would be shared across every call forever.
Defaults are for optional inputs, never for local variables.

The tell:
    "the element that appears more than n/2 times" -> I need counts, not
    presence -> frequency map. Then: "more than half" is a much stronger
    promise than "most frequent", and that extra strength is what buys the
    O(1) space version.
"""


class Solution(object):

    # ---- version 2: Boyer-Moore. O(n) time, O(1) space. The one to submit. ----
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for x in nums:
            if x == candidate:
                count += 1
            elif count == 0:
                candidate = x
                count = 1
            else:
                count -= 1
        return candidate

    # ---- version 1: frequency dict. O(n) time, O(n) space. Kept for reference. ----
    def majorityElementDict(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = dict()
        for i in nums:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
        return max(c, key=c.get)


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([3, 2, 3], 3),
        ([1, 2, 2, 2], 2),      # this one broke both buggy decrements
        ([1], 1),
        ([6, 5, 5], 5),
        ([0, 0, 1], 0),         # 0 as the answer - why candidate=None, not 0
    ]
    for xs, want in cases:
        a, b = sol.majorityElement(list(xs)), sol.majorityElementDict(list(xs))
        flag = "PASS" if a == b == want else "FAIL"
        print(f"{flag}  {str(xs):22} boyer={a}  dict={b}  want={want}")
