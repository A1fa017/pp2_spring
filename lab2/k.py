s = input().split()
s = set(s)
l = []

for i in s:
    t = ''
    for j in i:
        if j.isalpha():
            t += j
    l.append(t)
l.sort()
print(len(l))
for x in l:
    print(x)