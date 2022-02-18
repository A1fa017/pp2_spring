def spy_game(nums):
    num_007 = ''
    for subnums in nums:
        if subnums == 0 or subnums == 7:
            num_007 += str(subnums)
    if '007' in num_007:
        return True
    return False
print(spy_game([1,2,4,0,0,7,5])) #True
print(spy_game([1,0,2,4,0,5,7])) #True
print(spy_game([1,7,2,0,4,5,0])) #False