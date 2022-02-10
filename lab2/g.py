demons = {}
for i in range(int(input())):
    s = input().split()
    if s[-1] not in demons:
        demons[s[-1]] = 1
    else:
        demons[s[-1]] += 1
hunters = {}
for j in range(int(input())):
    s = input().split()
    if s[-2] not in hunters:
        hunters[s[-2]] = int(s[-1])
    else:
        hunters[s[-2]] += int(s[-1])
l = 0
for x in demons:
    if x in hunters:
        if demons[x]>hunters[x]:
            l += demons[x]-hunters[x]
    else:
        l += demons[x]
print('Demons left:',l)
        

