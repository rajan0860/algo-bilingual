def longest_subk(s: str, k: int) -> int:
    seen = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        seen[s[right]] = seen.get(s[right], 0) + 1
        while len(seen) > k:
            seen[s[left]] -= 1
            if seen[s[left]] == 0:
                del seen[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
        
        
if __name__ == "__main__":
    print(longest_subk("abcabcbb",2))
    