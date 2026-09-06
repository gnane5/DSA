"""
LC 217 - Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Pattern: set / seen-so-far

Brute force:
    Two nested loops - compare every element against every element after it.
    My first version looped over VALUES not positions, so it compared each
    element with itself and returned True for any non-empty list. Fixing that
    means range(len(nums)) outside and range(i+1, len(nums)) inside - the
    i+1 is what stops self-comparison and stops re-checking pairs backwards.
    Time O(n^2)   Space O(1)

Final:
    One pass. Keep a set of everything seen so far; if the current value is
    already in it, that's the duplicate.
    Two things that have to be right:
      - check BEFORE adding. Add first and every element matches itself.
      - `return False` goes AFTER the loop. You only know there is no
        duplicate once you have looked at everything.
    Time O(n)     Space O(n) - the set can grow to hold every element

    The trade: I spent memory to buy time. O(n^2)/O(1) became O(n)/O(n).
    That trade is the answer an interviewer is listening for.

The tell:
    "contains any duplicate" = a yes/no question about repeats -> I need to
    know whether I have met this value before -> a set, because `in` on a set
    is O(1). On a list `in` is O(n) and this collapses straight back to O(n^2).
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 4, 5, 1]))   # True
    print(sol.containsDuplicate([1, 2, 3]))            # False
    print(sol.containsDuplicate([]))                   # False
