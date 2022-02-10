s = input().split()

def d(n,x):
    sum = 0
    for i in range(n):
        sum ^= x + 2*i
    print(sum)
if len(s) == 1:
    n = int(s[0])
    x = int(input())
    d(n,x)
else:
    n = int(s[0])
    x = int(s[1])
    d(n,x)