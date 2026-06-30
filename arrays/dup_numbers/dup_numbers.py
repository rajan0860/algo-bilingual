def is_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

if __name__ == "__main__":
    nums = [0, 2, 3, 1]
    if is_duplicate(nums):
        print("Duplicate number found")
    else:
        print("There are no duplicate number in the list")
        
        