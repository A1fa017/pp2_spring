d = {}

for x in range(int(input())):
    s,i = map(str,input().split())
    if s in d:
        d[s] += int(i)
    else:
        d[s] = int(i)

l = []

for x in d.values():
    l.append(x)
l.sort()
for key in sorted(d):
    if d[key] == l[-1]:
        print(key,'is lucky!')
    else:
        print(key,'has to receive',l[-1]-d[key],'tenge')