l = []

for i in range(int(input())):
    a = b = c = 0
    s = input()
    if s not in l:
        for x in s:
            if x.isdigit():
                a += 1
            elif x.islower():
                b += 1
            elif x.isupper():
                c += 1
        if a>=1 and b>=1 and c>=1:
            l.append(s)            
l.sort()                 
print(len(l))
for x in l:
    print(x)