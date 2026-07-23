# Week 01 — Arrays & Strings

**Pattern:** HashMap/HashSet for O(1) lookup, two pointers for in-place swaps
**Languages:** Python (all 4) + Go (Two Sum, Reverse String)
**Status:** ✅ Complete

---

## Problems

| Day | Problem | Difficulty | Python | Go | Notes |
|-----|---------|------------|--------|----|-------|
| Mon | Two Sum | Easy | ✅ | ✅ | HashMap complement lookup |
| Tue | Two Sum (Go translation) | Easy | — | ✅ | Stray `networkx` import caught + removed |
| Wed | Valid Anagram | Easy | ✅ | — | Single dict, increment/decrement |
| Thu | Contains Duplicate | Easy | ✅ | — | Switched dict → set after review |
| Fri | Reverse String | Easy | ✅ | ✅ | Go version had O(n²) bug, fixed |

---

## Pattern Notes

**Core idea:**
When a problem asks "does X exist?" or "have I seen this before?", reach for a HashMap or HashSet before reaching for nested loops. Trading O(n) space for O(1) lookup turns O(n²) brute force into O(n).

**When to use HashSet vs HashMap:**
- HashSet — you only need existence checks (Contains Duplicate: "have I seen this number?")
- HashMap — you need to associate a value with a key (Two Sum: "what index did I see this number at?", Valid Anagram: "what's the count of this character?")
- Using a dict when a set would do is a common over-engineering tell — caught this in Contains Duplicate.

**Two pointers — first appearance this week:**
Reverse String introduced the left/right pointer pattern: start at both ends, swap inward, stop when pointers meet. This is the foundation for Week 2 (Two Pointers & Sliding Window) — palindromes, 3Sum, and container problems all extend this same idea.

**Time/space complexity rule of thumb:**
HashMap/HashSet trade O(n) space for O(1) average lookup. When the key space is bounded (e.g. lowercase letters, ≤26 keys), space is effectively O(1) regardless of input size — this came up in Valid Anagram.

---

## Go vs Python — Key Differences Noticed

- **Strings are immutable in both languages** — but the fix differs:
  - Python: `list(s)` → mutate → `''.join(...)`
  - Go: `[]byte(s)` → mutate → `string(...)`
- Forgetting this in Go is dangerous: concatenating strings inside a loop (`s = s[:l] + ... `) *compiles fine* but silently degrades O(n) to O(n²), since each concatenation copies the whole string. Python is more forgiving here — direct mutation attempts just throw a `TypeError`, which fails loudly instead of silently.
- Go has no built-in `set` type — use `map[T]struct{}` or `map[T]bool` when a HashSet is needed (not used yet this week, but will come up).
- Go's `make(map[K]V)` requires explicit initialization; Python dict/set literals are more concise.

---

## Mistakes Made This Week (and fixed)

1. **Stray `from networkx import complement` import** in Two Sum (Python) — unrelated to the problem, likely copy-paste leakage from another project. Lesson: always sanity-check imports before submitting.
2. **Debug `print()` statements left inside logic functions** (Two Sum Go, Reverse String Python, Contains Duplicate) — functions should be pure (compute + return), with all I/O isolated to `main()` / `__main__`. This matters because interview test harnesses call your function directly and check the return value — printing instead of returning breaks that contract.
3. **Used `dict` where `set` was the correct tool** (Contains Duplicate) — worked, but signaled imprecision. Reach for the leanest data structure that solves the problem.
4. **O(n²) string reversal in Go** via repeated concatenation inside a loop — the most significant bug of the week. Fixed by converting to `[]byte` first and swapping in place, restoring true O(n).
5. **Tests checked "did it return *something*" instead of "did it return the *correct* answer"** (Two Sum Go, first pass) — fixed by comparing against known expected values rather than just checking for non-(-1,-1) output.

---

## What to Watch For Next Week (Two Pointers & Sliding Window)

- Ask: can a second pointer replace a nested loop?
- Left/right pointers (move inward) vs fast/slow pointers (different speeds) — different tools for different shapes of problem.
- Sliding window extends two pointers for substring/subarray problems — window expands and contracts rather than just moving inward.
- Valid Palindrome (Day 1) reuses the exact swap-pointer logic from Reverse String, but adds a filtering step for non-alphanumeric characters — good test of whether last week's pattern actually stuck.