n = int(input())
gen = (i for i in range(n,-1,-1))
for num in gen:
    print(num,end = ' ')