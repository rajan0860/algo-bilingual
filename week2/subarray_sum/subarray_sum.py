def subarray_sum_bruteforce(nums : list[int], k : int) -> int:
    max_sum = sum(nums[:k])
    for i in range(len(nums) - k + 1):
        current_sum = 0
        for j in range(i, i + k):
            current_sum = current_sum + nums[j]
        max_sum = max(current_sum, max_sum)
    return max_sum

def subarray_sum_opt(nums : list[int], k : int) -> int:
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i - k] 
        max_sum = max(max_sum, current_sum)
    return max_sum     

if __name__ == "__main__":
    cases = [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([2, 3, 4, 1, 5],    2, 7),
        ([1, 2, 3],          3, 6),
        ([-1,-2,-3,-4],      2, -3),
        ([5],                1, 5),
    ]
for nums, k, expected in cases:
    result = subarray_sum_bruteforce(nums, k)
    status = "Passed" if result == expected else "Failed"
    print(f"{status} subarray_sum_bruteforce({nums}, k={k}) = {result}")

for nums, k, expected in cases:
    result = subarray_sum_opt(nums, k)
    status = "Passed" if result == expected else "Failed"
    print(f"{status} subarray_sum_opt({nums}, k={k}) = {result}")
    