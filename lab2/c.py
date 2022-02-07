n = int(input())

for x in range(n):
    for y in range(n):
        if y == 0:
            print(str(x)+' ',end='')
        elif x == 0:
            print(str(y)+' ',end='')
        elif x == y:
            print(str(x*y)+' ',end='')
        else:
            print(str(0)+' ',end='')
    print()