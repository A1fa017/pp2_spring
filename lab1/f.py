mylist = []

for i in range(int(input())):
    n = int(input())
    if n<=10:
        mylist.append('Go to work!')
    elif n<=25:
        mylist.append('You are weak')
    elif n<=45:
        mylist.append('Okay, fine')
    else:
        mylist.append('Burn! Burn! Burn Young!')

for i in mylist:
    print(i)