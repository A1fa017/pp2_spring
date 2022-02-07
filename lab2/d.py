n = int(input())

for x in range(n):
    for y in range(n):
        if n%2 == 1:
            if x+y >= n-1:
                print('#',end='')
            else:
                print('.',end='')
        else:
            if x >= y:
                print('#',end='')
            else:
                print('.',end='')
    print()