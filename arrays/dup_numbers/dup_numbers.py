def is_duplicate(nums: list[int]) -> bool:
    num_map = {}
    for i, num in enumerate(nums):
        num_map[num] = num_map.get(num, 0) + 1
        count = num_map.get(num)
        if (count >= 2):
            print("Here is the duplicate number ", num)
            return True
    return False

if __name__ == "__main__":
    nums = [0, 2, 3, 1]
    if is_duplicate(nums):
        print("Duplicate number found")
    else:
        print("There are no duplicate number in the list")
        
        