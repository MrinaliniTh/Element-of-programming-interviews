def sortColors(nums):
    """
    Given an array nums with n objects colored red, white, or blue.
    sort them in-place so that objects of the same color are adjacent,
    with the colors in the order red, white, and blue.We will use the integers 0, 1,
    and 2 to represent the color red, white, and blue, respectively.
    """
    left = cur = 0
    right = len(nums) - 1
    while cur <= right:
        if nums[cur] == 0:
            nums[left], nums[cur] = nums[cur], nums[left]
            cur += 1
            left += 1
        elif nums[cur] == 2:
            nums[right], nums[cur] = nums[cur], nums[right]
            right -= 1
        else:
            cur += 1
    return nums

print(sortColors([1,1,1,0,0,2,0,0,2]))
            