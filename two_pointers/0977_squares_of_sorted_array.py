"""
LC 977 - Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Pattern: converging two pointers + backwards fill
NOT on NeetCode 150 - done as reinforcement. Accepted 137/137.

The problem:
    A SORTED array that can contain negatives: [-4,-1,0,3,10]
    Return the squares, sorted:                [0,1,9,16,100]

Brute force (kept below as sortedSquaresSort):
    Square everything, call .sort(). Correct, and it's what I submitted.
    Time O(n log n)   Space O(n)

Why O(n) is possible - the shape:
    nums     = [-4,  -1,   0,   3,  10]
    squares  = [16,   1,   0,   9, 100]
                <-- descending -->  <-- ascending -->
    The squares form a VALLEY. Guaranteed, not luck, because the input was
    sorted. So the LARGEST square is always at one of the two ends, never in
    the middle - which means one comparison between the ends always names the
    largest remaining value.

    That also means this is a MERGE, not a sort. Two already-ordered runs
    facing away from each other. Merging is O(n) because the ordering
    information already exists; sorting is O(n log n) because it throws that
    information away and rediscovers it.

Final:
    Three indices, but only TWO pointers:
        x, y  - read, one at each end. WHICH one moves depends on a
                comparison, so these are the pointers.
        z     - write. Counts down by one every single pass, unconditionally,
                and depends on nothing. That's a cursor, not a pointer.
    Each pass: bigger |value| wins -> square it into out[z] -> move that
    side's read pointer inward -> z -= 1.
    Loop while x <= y, not x < y: n elements means n writes, and the middle
    element needs its turn.
    Time O(n)   Space O(n) for the output (O(1) extra)

    abs() on the original array gives the same ordering as the squares
    without building a second array first.

THE LESSON - six rounds, and five of them were the same mistake:
    I kept trying to rearrange nums in place by swapping.

    Why that can never work: a swap requires knowing BOTH destinations. At
    any moment I only know one - where the LARGEST goes, which is last. I
    have no idea yet where anything else belongs. So when you can only
    identify one end of the answer at a time, you need a SEPARATE array to
    write into.

    Every slot in nums holds something still needed. Writing into it destroys
    data I haven't read yet.

    The contrast worth keeping: LC 88 Merge Sorted Array and LC 283 Move
    Zeroes ARE in-place - because there you know where things go, and in 88
    the padding at the end is already free. Knowing WHICH situation you are
    in is the actual skill.

        can't identify both destinations / no free space  -> build a new array
        destination known, or free space available        -> in place

On LeetCode runtimes:
    Submitted the O(n log n) version: Accepted, 12 ms, "beats 59.5%". The
    0 ms sample shown next to it was the SAME CODE. LeetCode's timer is
    coarse and the judges are shared - the same submission returns different
    numbers each time. It is not a quality signal.

    And a real wrinkle: the O(n) two-pointer version may report a SLOWER
    wall-clock than the sort version, because .sort() runs in C while a
    Python while-loop runs in the interpreter (roughly 50-100x slower per
    operation). That does not make sorting better - complexity is what an
    interviewer grades, and the curve wins once n is large enough.

The tell:
    Input is SORTED but the transformation breaks the order symmetrically
    (squares, absolute values) -> the extremes end up largest -> two pointers
    from the ends, filling the answer BACKWARDS, because the only thing you
    can ever name is the largest remaining.
"""


class Solution(object):

    # ---- the one to submit: two pointers + backwards fill, O(n) ----
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        out = [0] * n
        x = 0            # read, left end
        y = n - 1        # read, right end
        z = n - 1        # write cursor, moves backwards every pass

        while x <= y:
            if abs(nums[x]) > abs(nums[y]):
                out[z] = nums[x] * nums[x]
                x += 1
            else:
                out[z] = nums[y] * nums[y]
                y -= 1
            z -= 1

        return out

    # ---- brute force, kept for reference: O(n log n) ----
    def sortedSquaresSort(self, nums):
        sqlist = []
        for i in nums:
            sqlist.append(i * i)
        sqlist.sort()
        return sqlist


if __name__ == "__main__":
    sol = Solution()
    cases = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [-5, -3, -2, -1],        # all negative
        [1, 2, 3],               # all positive
        [0],                     # single
        [-1, 0, 1],
        [-10, -9, -8, 1, 2],
        [-3, -3, 3, 3],          # ties
    ]
    for nums in cases:
        want = sorted(v * v for v in nums)
        a = sol.sortedSquares(list(nums))
        b = sol.sortedSquaresSort(list(nums))
        flag = "PASS" if a == b == want else "FAIL"
        print(f"{flag}  {str(nums):22} -> {a}")
