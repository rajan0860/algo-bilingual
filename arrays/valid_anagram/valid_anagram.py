def is_anagram(s: str, t: str) -> bool:
    print(f"Input: s = {s}, t = {t}")
    
    count_s = {}
    count_t = {}
    
    if len(s) != len(t):
        print("Output: False")
        return False
    
    else:
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
            print(f"Count of {char} in s: {count_s[char]}")
            
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
            print(f"Count of {char} in t: {count_t[char]}")
            
        if count_s == count_t:
            print("Output: True")
            return True
        else:
            print("Output: False")
            return False
if __name__ == "__main__":
    
    tests = [
        ("anagram", "nagaram", True),
        ("rat",     "car",     False),
        ("LISSTEN", "SSILENT", True),   # your original case
        ("a",       "a",       True),   # single char
        ("ab",      "a",       False),  # different lengths
    ]
    # Add your test cases or run validation here
    for s, t, expected in tests:
        result = is_anagram(s, t)
        print(f"Test: {s} and {t} -> {result} (expected: {expected})")
        
    print("Python solution ran successfully!")
