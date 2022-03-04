n = int(input())
even = (i for i in range(n) if i%2 == 0)
for num in even:
    if n-num == 2 or n-num == 1:
        print(num)
    else:
        print(num, end = ',')