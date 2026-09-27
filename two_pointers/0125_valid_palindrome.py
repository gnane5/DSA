"""
LC 125 - Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Pattern: converging two pointers

Brute force:
    Keep only the alphanumerics, lowercase them, compare the result to its
    reverse. Correct, and almost a one-liner - but it builds a WHOLE NEW
    STRING, so it costs O(n) extra space.
    Time O(n)   Space O(n)

Final:
    One pointer at each end, walking inward. Three jobs per pass, in order:
      1. left pointer on a non-alphanumeric? step it and `continue`
      2. same for the right pointer
      3. both now on real characters -> compare them
    Mismatch -> return False immediately. Survive the whole loop -> True.
    Time O(n)   Space O(1) - two integers, whatever the size of the input

    Why `continue` matters: after skipping one character the next one might
    be junk too ("a,,b"). Without it you compare before re-checking.

    Why `while x < y` and not `<=`: at x == y both pointers sit on the same
    character, which always equals itself. Stopping there handles odd length,
    even length, the empty string and an all-punctuation string with no
    special cases at all.

Four rounds to get here. The bug each time, because the pattern in them
matters more than the problem:
    1. Skipped junk but never compared anything. The skipping is only
       preparation - the comparison IS the algorithm.
    2. Lowercased into `c`, then indexed `s`. So "A" != "a".
    3. Handled only the matching branch. On a mismatch nothing happened and
       neither pointer moved -> infinite loop on "race a car".
       Every comparison has two outcomes; both need a branch.
    4. print(True) inside the loop, so "race a car" printed
       True True True False. SEVENTH time for that one (217, 49, 238, Two
       Sum, and three rounds of this). The answer is only known once the
       loop has FINISHED. Mechanical fix: before running anything, look at
       the indentation of the last line.

The tell:
    "is it the same forwards and backwards", or any question about a pair
    taken from opposite ends of a sequence -> one pointer at each end,
    walking inward.
    What makes it two pointers and not two passes: at each step you DECIDE
    which pointer to move, and that decision comes from a comparison.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = s.lower()
        x = 0
        y = len(c) - 1

        while x < y:
            if not c[x].isalnum():
                x += 1
                continue
            if not c[y].isalnum():
                y -= 1
                continue

            if c[x] == c[y]:
                x += 1
                y -= 1
            else:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("0P", False),          # digit vs letter
        (".,", True),           # nothing but punctuation
        ("a.b", False),
        ("..1..1..", True),
    ]
    for s, want in cases:
        got = sol.isPalindrome(s)
        print(f"{'PASS' if got == want else 'FAIL'}  {s!r:34} -> {got}")
