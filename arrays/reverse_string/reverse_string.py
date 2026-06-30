def reverse_string(st : str) -> str:
    l = 0
    r = len(st) - 1
    st = list(st)
    print(st)
    while l < r:
        st[l], st[r] = st[r], st[l]
        print(st)
        l += 1
        r -= 1
    return ''.join(st)

if __name__ == "__main__":
    assert reverse_string("Hello") == "olleH"
    assert reverse_string("a")     == "a"
    assert reverse_string("")      == ""
    assert reverse_string("ab")    == "ba"
    print("All tests passed!")