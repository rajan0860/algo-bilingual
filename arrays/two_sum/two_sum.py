from networkx import complement


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    """
    Problem: Two Sum
    Difficulty: Easy
    Category: Arrays
    
    Find two numbers that add up to target and return their indices.
    """
    print(f"Input: nums = {nums}, target = {target}")
    
    num_map = {}
    for i, num in enumerate(nums):
        output = target - num
        if output in num_map:
            print(f"Output: [{num_map[output]}, {i}]")
            return (num_map[output], i)
        num_map[num] = i
    
    print("No two sum solution found.")
    return (-1, -1)

if __name__ == "__main__":
    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9},
        {"nums": [3, 2, 4], "target": 6},
        {"nums": [3, 3], "target": 6},
    ]
    
    for tc in test_cases:
        two_sum(tc["nums"], tc["target"])
    
    print("Python solution ran successfully!")
