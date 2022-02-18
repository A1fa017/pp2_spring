def has_33(nums):
    num_33 = ''
    for subnums in nums:
        num_33 += str(subnums)
    if '33' in num_33:
        return True
    return False
print(has_33([1, 3, 3])) #True
print(has_33([1, 3, 1, 3])) #False
print(has_33([3, 1, 3])) #False