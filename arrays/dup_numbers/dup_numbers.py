def is_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

if __name__ == "__main__":
    tests = [
        ([0, 2, 3, 1],     False),
        ([1, 2, 3, 1],     True),    # duplicate at the ends
        ([1, 1, 1, 3],     True),    # multiple duplicates
        ([1],              False),   # single element
        ([],               False),   # empty list
    ]
    
    for nums, expected in tests:
        result = is_duplicate(nums)
        print(f"is_duplicate({nums}) = {result}, expected = {expected}")
        assert result == expected, f"Test failed for input: {nums}"
        
        