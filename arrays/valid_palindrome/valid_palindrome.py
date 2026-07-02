def is_palindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l < r:
        # skip non-alphanumeric on left
        if not s[l].isalnum():
            l += 1
            continue
        # skip non-alphanumeric on right
        if not s[r].isalnum():
            r -= 1
            continue
        # compare characters case-insensitively
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1

    return True

if __name__ == "__main__":
    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        (".,", True),
    ]
    for s, expected in tests:
        result = is_palindrome(s)
        status = "Passed" if result == expected else "Failed"
        print(f'{status} is_palindrome("{s}") = {result}')