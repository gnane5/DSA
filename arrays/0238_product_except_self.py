"""
LC 238 - Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Pattern: prefix x suffix scan   (NOT two pointers - see the note at the bottom)

Brute force:
    For each position, an inner loop multiplies everything except it.
    Accumulator starts at 1, not 0 - 0 makes every answer 0, because 1 is the
    identity for multiplication the way 0 is for addition.
    Time O(n^2)   Space O(1)
    Bug on the way: c.append(p) was INSIDE the inner loop, so it appended the
    half-built product at every step - 12 entries instead of 4. Third time I
    made that mistake (217, 49, 238). The final answer goes AFTER the loop.

The insight:
    Division would make this trivial, which is exactly why the problem bans it
    (and it would break on zeros anyway).

    For ANY position, the answer splits in two:
        everything to its LEFT  x  everything to its RIGHT

        nums:        1    2    3    4
        left of i:   1    1    2    6      <- running product, forwards
        right of i:  24   12   4    1      <- running product, backwards
        answer:      24   12   8    6      <- left[i] * right[i]

    The brute force recomputes 3x4 twice and 1x2 twice. Every sub-product gets
    rebuilt from scratch - that is where the O(n^2) hides. A running product
    computes each one once.

Version 1 - two arrays, O(n) time / O(n) space:

    left  = [1] * n
    right = [1] * n
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    out[i] = left[i] * right[i]

    Why those two lines are exact mirrors:
      left[i]  = "product of everything BEFORE i". To extend it one step, take
                 the previous answer and multiply in the element you just
                 stepped over -> nums[i-1].
      right[i] = "product of everything AFTER i". Same sentence backwards:
                 take right[i+1] and multiply in nums[i+1].
    i-1 <-> i+1 is the whole swap.

    left[0] and right[n-1] stay 1 because there is nothing on that side - which
    is why the loops start at 1 and at n-2, not 0 and n-1.

Version 2 - the follow-up, O(n) time / O(1) EXTRA space (below):
    The output array does not count toward space complexity, so build both
    passes into it with a single running variable instead of two arrays.
    After pass 1, out holds the left column. Pass 2 walks backwards
    multiplying in the right column.

Zeros need no special handling: [-1,1,0,-3,3] -> [0,0,9,0,0] falls out.

Two bugs when I typed this from memory - both one word, both silent:
    n = len(num)            -> NameError. It's `nums`.
    prefix *= out[i]        -> WRONG. out[i] was just set to the OLD prefix,
                               so prefix never changes and pass 1 leaves
                               [1,1,1,1] instead of [1,1,2,6]. The final
                               answer came out as [24,12,4,1] - the right
                               column alone.
                               It must be prefix *= nums[i]: prefix accumulates
                               the INPUT, not the output.

Why this is not two pointers:
    In a two-pointer problem, at every step you DECIDE which pointer to move,
    based on a comparison. Here there is no comparison and no choice - just two
    full passes that accumulate. Walking forwards and then backwards is not the
    same thing as two converging pointers.

The tell:
    "product / sum of everything EXCEPT this one" -> split it into
    (everything before) x (everything after) -> two running passes, one
    forward, one backward, then combine.
    Generalises to running sums, min-to-the-left, max-to-the-right - any
    "all the others" question.
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        out = [1] * n

        prefix = 1
        for i in range(n):
            out[i] = prefix          # everything to the left, so far
            prefix *= nums[i]        # nums, not out

        suffix = 1
        for i in range(n - 1, -1, -1):
            out[i] *= suffix         # multiply in everything to the right
            suffix *= nums[i]

        return out

    # ---- version 1, kept for reference: two arrays, O(n) space ----
    def productExceptSelfTwoArrays(self, nums):
        n = len(nums)
        left = [1] * n
        right = [1] * n
        out = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            out[i] = left[i] * right[i]

        return out


if __name__ == "__main__":
    import math

    sol = Solution()
    cases = [[1, 2, 3, 4], [-1, 1, 0, -3, 3], [0, 0], [2, 3], [5]]
    for xs in cases:
        want = [math.prod(xs[:i] + xs[i + 1:]) for i in range(len(xs))]
        a = sol.productExceptSelf(list(xs))
        b = sol.productExceptSelfTwoArrays(list(xs))
        flag = "PASS" if a == b == want else "FAIL"
        print(f"{flag}  {str(xs):18} -> {a}")
