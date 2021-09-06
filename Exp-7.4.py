def is_sorted(nums):
    if len(nums) <= 1:
        return True
    else:
        desc = True if nums[0] > nums[1] else False
        if desc:
            for i in range(1, len(nums) - 1):
                if nums[i] < nums[i+1]: return False
            return True
        else:
            for i in range(1, len(nums) - 1):
                if nums[i] > nums[i+1]: return False
            return True
print("[] --> ",is_sorted([]))
print("[1] --> ",is_sorted([1]))
print("[1, 2, 3] --> ",is_sorted([1, 2, 3]))
print("[3, 2, 1] --> ",is_sorted([3, 2, 1]))
print("[1, 3, 2] --> ",is_sorted([1, 3, 2]))
'''
Output:
[] -->  True
[1] -->  True
[1, 2, 3] -->  True
[3, 2, 1] -->  True
[1, 3, 2] -->  False
'''
