def solve() -> None:
    """
    Problem: Two Sum
    Difficulty: Easy
    Category: Arrays
    """
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: nums = {nums}, target = {target}")
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            print(f"Output: [{num_map[complement]}, {i}]")
            return
        num_map[num] = i
    print("No two sum solution found.")

if __name__ == "__main__":
    # Add your test cases or run validation here
    solve()
    print("Python solution ran successfully!")
