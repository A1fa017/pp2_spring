x1,y1 = map(int,input().split())
l = []
for i in range(int(input())):
    x2,y2 = map(int,input().split())
    values = str(x2) +' '+ str(y2)
    key = ((x2-x1)**2+(y2-y1)**2)**0.5
    list = [key,values]
    l.append(list)
l.sort()
for x in l:
    print(x[1])