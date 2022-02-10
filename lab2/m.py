l = []
while 2>1:
    s = input().split()
    if s[0] == '0':
        break
    list = [s[2],s[1],s[0]]
    l.append(list)
l.sort()
for x in l:
    print(x[2],x[1],x[0])
