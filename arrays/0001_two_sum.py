"""
LC 1 - Two Sum
https://leetcode.com/problems/two-sum/

Pattern: hash of seen-so-far   (NOT DONE YET - see TODO below)

Status: brute force works. O(n) version parked for a re-solve.

Brute force:                                      <- this is what's written
    Check every pair once. Outer loop walks each position i, inner loop
    starts at i+1 so a pair is never revisited and an element is never
    added to itself.
    Two mistakes I made getting here, both worth remembering:
      - looped over VALUES (`for i in nums`) when I needed POSITIONS.
        `range(len(nums))` gives positions; `enumerate(nums)` gives both.
      - then compared `i + j` (the positions) instead of
        `nums[i] + nums[j]` (the values at those positions).
        Rule: add the values, report where they were.
    Time O(n^2)   Space O(1)

Final:  TODO
    Time O(n)     Space O(n)

The tell:
    "two numbers that add up to target" on an UNSORTED array, and it wants
    the indices back -> for each x I need to find target - x somewhere else
    -> searching a list is O(n), so store what I've seen in a dict and the
    search becomes O(1). A set won't do here: it tells me WHETHER I've seen
    a value, and I need WHERE.
"""


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []



class Solution(object):
    def twoSum(self, nums, target):
        seen = {}                      # value -> index
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:           # O(1). looks BACKWARD only
                return [seen[need], i]
            seen[nums[i]] = i          # remember AFTER checking
        return []



# ---------------------------------------------------------------------------
# TODO - the O(n) version. Come back to this cold, from an empty file.
#
# The idea in one line: never look forward, only backward.
# Walk the array once. At each element ask "have I ALREADY seen the number
# that completes this one?" Every pair gets found at its SECOND member.
#
# Trace, nums = [2, 5, 7, 3, 4], target = 6  -> answer is [0, 4]:
#
#   at | value | I need | seen it?      | then
#   ---+-------+--------+---------------+---------------------
#    0 |   2   |   4    | no            | remember  2 -> 0
#    1 |   5   |   1    | no            | remember  5 -> 1
#    2 |   7   |  -1    | no            | remember  7 -> 2
#    3 |   3   |   3    | no            | remember  3 -> 3
#    4 |   4   |   2    | YES, at 0     | answer [0, 4]
#
# Indices 0 and 4 are as far apart as possible and it still finds them in
# one pass - that was the thing I couldn't see.
#
# Two questions to answer when I come back:
#   1. What goes in the dict - the value as the key or the index as the key?
#      (Which one am I looking things up BY?)
#   2. Do I check before storing, or store before checking?
#      Get it backwards and nums = [3, 3], target = 6 breaks. Why?
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))    # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))         # [1, 2]
    print(sol.twoSum([3, 3], 6))            # [0, 1]
    print(sol.twoSum([2, 5, 7, 3, 4], 6))   # [0, 4]
