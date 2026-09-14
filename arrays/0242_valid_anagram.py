"""
LC 242 - Valid Anagram
https://leetcode.com/problems/valid-anagram/

Pattern: counter / frequency map

Brute force:
    For each char in s, compare s.count(c) with t.count(c).
    .count() rescans the WHOLE string on every call, inside a loop over n -
    so this is O(n^2) with only one visible for loop. That is step 4 of
    counting complexity: check what is inside the loop.
    Two wrong turns before that:
      - `if i not in t` checks PRESENCE, not counts. "aab" vs "abb" passes
        it, and they are not anagrams.
      - only looping over s's characters never checks extras in t, so
        "ab" vs "abc" returned True.
    Time O(n^2)   Space O(1)

Final:
    One pass over each string builds a frequency dict. Compare the two dicts.
    Dict equality checks keys AND values, so it also catches t having an
    extra character - no separate length check needed. That is why the
    length guard I was about to add turned out to be unnecessary.
    Time O(n)   Space O(1) - at most 26 keys (lowercase only), and 26 does
                             not grow with n

    Shorthand for the counting loop:  c[ch] = c.get(ch, 0) + 1
    One-liner once I trust it:        Counter(s) == Counter(t)

    Style note for next time: `if X: return True else: return False` is just
    `return X`. The ending below collapses to one line.

The tell:
    "anagram" = same letters rearranged -> I need how MANY of each letter,
    not just which ones are present -> count both, compare the counts
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c = dict()
        o = dict()
        for i in s:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1

        for i in t:
            if i in o:
                o[i] += 1
            else:
                o[i] = 1

        if c == o:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    for s, t, want in [("anagram", "nagaram", True), ("rat", "car", False),
                       ("ab", "abc", False), ("aab", "abb", False),
                       ("", "", True), ("a", "", False)]:
        got = sol.isAnagram(s, t)
        print(f"{'PASS' if got == want else 'FAIL'}  {s!r:10} {t!r:10} -> {got}")
