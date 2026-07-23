def longest_substring_set(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
            
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

def longest_substring_hasmap(s: str) -> int:
    seen = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1

        seen[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    cases = [
    ("", 0),
    ("a", 1),
    ("bbbbb", 1),
    ("abcabcbb", 3),
    ("pwwkew", 3),
    ("abcdef", 6),
    (" ", 1),
]
    print("----  HashSet approach ------")
    for s, expected in cases:
        result = longest_substring_set(s)
        print(f"longest_substring({s}) = {result}, expected = {expected}")
        assert result == expected, f"Test failed for input: {s}"
    
    print("----  HashMap approach ------")
    for s, expected in cases:
        result = longest_substring_hasmap(s)
        print(f"longest_substring({s}) = {result}, expected = {expected}")
        assert result == expected, f"Test failed for input: {s}"
            