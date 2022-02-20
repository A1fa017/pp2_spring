l,l1 = input().split(),[]

def unique(l, l1):
    for nums in l:
        if l.count(nums) == 1:
            l1.append(nums)
    return l1
l1 = unique(l, l1)
print(*l1)