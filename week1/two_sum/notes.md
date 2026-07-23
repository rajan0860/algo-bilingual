# Two Sum

| Pattern | Time Complexity | Space Complexity | Difficulty |
|---|---|---|---|
| Hash Map (One-Pass) | O(N) | O(N) | Easy |

---

## Approach
*Provide a step-by-step breakdown of the logic before coding.*

1. Initialize an empty hash map/dictionary to map each number to its corresponding index.
2. Iterate through the input array elements one by one. For each element:
   - Calculate its complement: `target - num`.
   - Check if this complement exists in the map.
   - If it does, we found the pair! Return the index of the complement (from the map) and the current index.
   - If it does not, store the current number and its index in the map.
3. If no matching pair is found by the end of the array, print or return a message indicating no solution exists.

## Key Differences

| Python 🐍 | Go ⚡ |
|---|---|
| Simple dictionary literal syntax: `num_map = {}` | Must explicitly instantiate maps: `m := make(map[int]int)` |
| Clean membership check: `if complement in num_map` | Explicit comma-ok idiom: `if j, ok := m[sub]; ok` |
| Native `enumerate()` returns both index and value | Uses standard range loop: `for i, num := range nums` |

## Gotchas & Edge Cases
- **No duplicate reuse:** We must not use the same element twice. By checking if the complement is in the map *before* inserting the current number, we guarantee that the two indices refer to different elements.
- **Map initialization:** Go maps are `nil` by default and will cause a runtime panic if written to without initializing using `make`.

---

## Resources
- **Problem Link:** [LeetCode Two Sum](https://leetcode.com/problems/two-sum/)
- **Status:** Solved ✅
