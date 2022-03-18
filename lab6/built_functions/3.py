import time
s = input()
l = ''
for i in reversed(s):
    l += i

if l == s:
    print('Yes')
else:
    print('no')