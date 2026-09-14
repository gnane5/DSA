"""
LC 49 - Group Anagrams
https://leetcode.com/problems/group-anagrams/

Pattern: canonical key   (sorting is the IMPLEMENTATION, not the idea)

Brute force:
    Build a frequency dict per word, then compare every dict against every
    other. n words = n^2/2 comparisons - 6 words is 15, 10,000 words is
    50 million. Same nested-loop shape I have now killed on 217, 242 and 1.
    Time O(n^2 * k)   Space O(n * k)

    Two wrong turns:
      - tried {"eat": [{e:1},{a:1},{t:1}]}. Backwards - the WORD was the
        key, so I could only look up BY the word, but I need to look up by
        fingerprint. And a LIST of dicts is order-dependent: "eat" gives
        [{e:1},{a:1},{t:1}] and "ate" gives [{a:1},{t:1},{e:1}], which are
        not equal. A fingerprint must never differ between anagrams.
      - c.extend(word) flattened every word into loose characters and
        destroyed the word boundaries, which is the one thing to keep.

Final:
    Never compare anything. Turn each word into ONE value that all of its
    anagrams produce identically, then drop the word into that value's
    bucket. The dict does all the matching, O(1) per word, zero comparisons.

        "".join(sorted(word)):   eat -> aet,  tea -> aet,  bat -> abt

    sorted() returns a LIST, which is unhashable and cannot be a dict key,
    so join it into a string first (tuple(sorted(word)) also works).
    defaultdict(list) means groups[key].append(word) works on a key that
    does not exist yet - no "if key not in d" check.
    list(g.values()) drops the keys and returns just the buckets.
    Time O(n * k log k)   Space O(n * k)

    A faster fingerprint also exists: a 26-length tuple of letter counts,
    O(k) instead of O(k log k). Same idea, different implementation - which
    is the proof that sorting is not the point.

The tell:
    "group the ones that are the SAME in some sense" -> compute one value
    that every member of a group produces identically -> let a dict group
    them for free.
    Generalises: same move for grouping numbers, shapes, file hashes -
    anything where "same" can be reduced to a computable key.
"""

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        g = defaultdict(list)
        for i in strs:
            k = "".join(sorted(i))
            g[k].append(i)
        return list(g.values())


if __name__ == "__main__":
    sol = Solution()
    for xs in [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"], []]:
        print(xs, "->", sol.groupAnagrams(list(xs)))
