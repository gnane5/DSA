"""
LC 167 - Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Pattern: converging two pointers

FIRST PROBLEM SOLVED UNAIDED. The only hints were about the output format,
not about the approach.

Brute force:
    Every pair, two nested loops. Ignores the one word that matters.
    Time O(n^2)   Space O(1)

LC 1 vs LC 167 - the whole difference is one word:
    UNSORTED (LC 1): I have no idea where a bigger or smaller value lives,
    so I have to remember everything I have already passed.
        -> dict of seen -> O(n) time, O(n) space
    SORTED (LC 167): the array itself tells me which direction is bigger and
    which is smaller, so I do not need to remember anything at all.
        -> two pointers -> O(n) time, O(1) space
    Sortedness replaces the hash map. That is what it buys you.

Final:
    A pointer at each end. Their sum is too big, too small, or exact.
        too big    -> y -= 1    (need a smaller total)
        too small  -> x += 1    (need a bigger total)
        exact      -> return
    Time O(n)   Space O(1)

WHY it is safe to discard an element forever - the actual interview content:
    The pointers span everything still in play, so numbers[y] is the LARGEST
    remaining value. If numbers[x] + numbers[y] is already too big, then
    pairing numbers[y] with anything at least as large as numbers[x] is also
    too big - and because the array is SORTED, every value left in the range
    is at least numbers[x]. So numbers[y] cannot be part of ANY remaining
    answer. Drop it permanently.

    Mirror image when the sum is too small: numbers[x] is the smallest value
    left, pairing it with anything up to numbers[y] still falls short, so
    numbers[x] is out.

    Each comparison eliminates a whole element from every future pairing, not
    just the one tested. That is why one pass is enough.

    Same argument shape as LC 11 Container With Most Water, where the
    question is why it is safe to discard the SHORTER wall.

The output format trap:
    LC 1 wants 0-indexed. LC 167 wants 1-INDEXED - it describes the input as
    a 1-indexed array and asks for the indices "added by one".
        [2,7,11,15], target 9  ->  [1,2], NOT [0,1]
    Same shape of question, opposite convention. The loop stays 0-based
    because Python is; only the returned answer shifts. Read the output
    section of every problem.

Cleanups from the first draft:
    - `break` after a `return` is unreachable; return already exits
    - the `continue`s were redundant here, because each branch is the last
      statement in the loop body. In 125 they WERE load-bearing, because the
      comparison came after the skip checks. Worth knowing the difference.
    - computed numbers[x] + numbers[y] three times per pass before naming it

The tell:
    "two numbers that add up to target" AND the array is SORTED -> two
    pointers, not a hash map. The word "sorted" in an array problem is almost
    always the hint: it means one comparison lets you throw away part of the
    search space for good.
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = 0
        y = len(numbers) - 1

        while x < y:
            total = numbers[x] + numbers[y]
            if total == target:
                return [x + 1, y + 1]      # 1-indexed, per the problem
            elif total > target:
                y -= 1                     # drop the largest remaining
            else:
                x += 1                     # drop the smallest remaining

        return []                          # the problem guarantees one answer


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),   # duplicates
        ([0, 0, 3, 4], 0, [1, 2]),
    ]
    for arr, t, want in cases:
        got = sol.twoSum(list(arr), t)
        print(f"{'PASS' if got == want else 'FAIL'}  {str(arr):26} t={t:<3} -> {got}")
