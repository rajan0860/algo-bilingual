# Valid Anagram

Problem: Determine whether two strings are anagrams of each other by comparing their character frequencies.

## Approach
- Compare lengths first; if they differ, the strings cannot be anagrams.
- Build a character count dictionary for `s`.
- Build a character count dictionary for `t`.
- Return `True` if both dictionaries are equal, otherwise `False`.

## Python implementation details
- Function: `is_anagram(s: str, t: str) -> bool`
- Uses two dictionaries: `count_s` and `count_t`.
- Prints intermediate counts while iterating through each string.
- Prints the final output before returning.

## Time and space complexity
- Time: O(n), where `n` is the length of the strings.
- Space: O(n) for the character count dictionaries.

## Example test cases
- `("anagram", "nagaram")` -> `True`
- `("rat", "car")` -> `False`
- `("LISSTEN", "SSILENT")` -> `True`
- `("a", "a")` -> `True`
- `("ab", "a")` -> `False`
