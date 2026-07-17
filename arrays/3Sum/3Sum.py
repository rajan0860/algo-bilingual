def find_3sum_bruteforce(nums : list[int]) -> list[list[int]]:
    sum_indexes = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    sum_indexes.append([nums[i], nums[j], nums[k]])
    
    unique_lists = {tuple(sorted(x)) for x in sum_indexes}
    
    return [list(x) for x in unique_lists]

def skip_left_duplicates(nums: list[int], left: int, right: int) -> int:
    while left < right and nums[left] == nums[left - 1]:
        left += 1
    return left


def skip_right_duplicates(nums: list[int], left: int, right: int) -> int:
    while left < right and nums[right] == nums[right + 1]:
        right -= 1
    return right

def find_3sum_two_pointers(nums : list[int]) -> list[list[int]]:
    sum_indexes = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and (nums[i] == nums[i-1]):
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total_sum = nums[i] + nums[left] + nums[right]
            if total_sum == 0:
                sum_indexes.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                left = skip_left_duplicates(nums, left, right)
                right = skip_right_duplicates(nums, left, right)
            elif total_sum < 0:
                left += 1
            elif total_sum > 0:
                right -= 1

    return sum_indexes

if __name__ == "__main__":
    test_cases = [
    [],
    [0],
    [0, 0],
    [1, 2, -3],
    [1, 2, 3, 4, 5],
    [-1, -2, -3, -4],
    [0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [-2, -2, 0, 0, 2, 2],
    [-1, -1, 2, 2, -1],
    [1, 1, -2, -2, 1],
    [3, 3, -3, -2, -2, -1, -1, 2, -3],
    [-1, 0, 1, 2, -1, -4],
    [3, 0, -2, -1, 1, 2],
    [0, 0, 2, -2, 1, 1, 2, -2, 4],
    [1, -1, -3, 3, -3, -1, 1, 4, -2],
    [-4, -1, -1, 0, 1, 2],
]

for nums in test_cases:
    result = find_3sum_two_pointers(list(nums))  # pass a copy since your function sorts in place
    print(f"{nums} -> {result}")
                    