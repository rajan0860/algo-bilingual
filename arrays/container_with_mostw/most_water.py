def brute_force_container_mostw(heignts : list[int]) -> int:
    max_area = 0
    for i in range(len(heignts)):
        for j in range(i+1, len(heignts)):
            area = (j - i) * min(heignts[j], heignts[i])
            max_area = max(max_area, area)      
    return max_area

def container_mostwtr_two_ptr(heignts : list[int]) -> int:
    left = 0
    right = len(heignts) - 1
    max_area = 0
    while left < right:
        area = (right - left) * min(heignts[left], heignts[right])
        
        if heignts[left] < heignts[right]:
            left += 1
        else:
            right -= 1
        max_area = max(max_area, area)
    return max_area

if __name__ == "__main__":
    tests = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1],                 1),
        ([4,3,2,1,4],          16),
        ([1,2,1],               2),
        ([1],                   0),
        ([2,3,4,5,18,17,6],   17),
    ]
    for heights, expected in tests:
        bf     = brute_force_container_mostw(heights)
        tp     = container_mostwtr_two_ptr(heights)
        status = "Passed" if tp == expected else "Failed"
        print(f"{status} two_ptr={tp} brute={bf} expected={expected}")
            
        