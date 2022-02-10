s = input().split()
l = len(s)-1
for i in range(len(s)-1,-1,-1):
    if int(s[i])+i>=l:
        l = i
if l == 0:
    print(1)
else:
    print(0)
