a,b = map(int,input().split())
sqrt = (i**2 for i in range(a,b))
for num in sqrt:
    print(num)