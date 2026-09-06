# Python costs

n = number of elements in the container.
"avg" means average case — hash collisions can degrade it, but you quote the
average in interviews and nobody argues.

## Lists

| operation              | cost          | why |
|------------------------|---------------|-----|
| `lst[i]`               | O(1)          | a list is a contiguous block; index i is a direct address computation |
| `len(lst)`             | O(1)          | the length is stored, not counted |
| `lst.append(x)`        | O(1) amortised| usually free; occasionally reallocates and copies, which averages out |
| `lst.pop()`            | O(1)          | removing from the end shifts nothing |
| `lst.pop(0)`           | O(n)          | removing the front shifts every remaining element left one slot |
| `lst.insert(0, x)`     | O(n)          | same, shifting right |
| `x in lst`             | O(n)          | a list doesn't know what it holds — it walks from the front comparing |
| `lst[a:b]`             | O(b−a)        | a slice **copies**. Inside a loop this turns O(n) into O(n²) |
| `sorted(lst)`          | O(n log n)    | Timsort. Also O(n) extra space |
| `lst.reverse()`        | O(n)          | swaps in place, one pass |
| `min/max/sum(lst)`     | O(n)          | one pass each. Three of them inside a loop is three separate O(n²) |

## Sets and dicts

| operation              | cost          | why |
|------------------------|---------------|-----|
| `x in set` / `x in dict`| O(1) avg     | hashes x to a bucket address and looks *directly* there — no scan, and the cost doesn't grow with size |
| `set.add(x)`           | O(1) avg      | same hash, same direct address, writing instead of reading |
| `dict[k] = v`          | O(1) avg      | same |
| `dict.get(k, default)` | O(1) avg      | same lookup, just returns the default instead of raising `KeyError` |
| `set(lst)` / `dict(...)`| O(n)         | one hash+insert per element |
| `dict_a == dict_b`     | O(n)          | compares every key and value. Catches "extra key on one side" for free |

## Strings

| operation              | cost          | why |
|------------------------|---------------|-----|
| `s[i]`                 | O(1)          | same as a list |
| `x in s`               | O(n·m)        | substring search scans |
| `s.count(x)`           | O(n)          | **scans the entire string every call.** Called inside a loop over n, that's O(n²) — this is the one that bit me on LC 242 |
| `s += t` inside a loop | O(n²) total   | strings are immutable, so each `+=` allocates and copies a whole new string |
| `"".join(parts)`       | O(total len)  | measures once, allocates once, copies once. Always use this instead |
| `sorted(s)`            | O(n log n)    | returns a **list** of chars, not a string |

## Deque and heap

| operation              | cost          | why |
|------------------------|---------------|-----|
| `deque.popleft()`      | O(1)          | linked blocks, so there's no shifting. BFS is unusable without it |
| `deque.appendleft(x)`  | O(1)          | same |
| `heapq.heappush/heappop`| O(log n)     | sifts one element up or down a binary heap of depth log n |
| `heapq.heapify(lst)`   | O(n)          | surprisingly, not O(n log n) |
| `nums[0]` on a heap    | O(1)          | the min is always at index 0 |

---

## The rule this table exists for

**Step 4 of counting complexity: check what's inside the loop.**

An O(n) operation inside a loop over n is O(n²) — with only one visible `for`.
These are the ones that hide:

    if x in my_list          # O(n)  -> use a set
    my_list.pop(0)           # O(n)  -> use a deque
    sub = nums[a:b]          # O(n)  -> pass indices instead
    s.count(c)               # O(n)  -> build a frequency dict once
    s += t                   # O(n)  -> collect into a list, join once

Two conventions worth knowing before someone corrects you mid-round:

- the output array usually does **not** count toward space complexity
- the recursion stack **always** does
