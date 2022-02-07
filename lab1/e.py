a, b = map(int, input().split())

def myfunc(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

if a<500 and myfunc(a)==True and b%2==0:
    print('Good job!')
else:
    print('Try next time!')
