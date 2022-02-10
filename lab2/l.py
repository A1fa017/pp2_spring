s = input()
l = []
ok = True
for i in s:
    if i == '(' or i == '[' or i ==  '{':
        l.append(i)
    else:
        if len(l)>0:
            if i == ')' and l[-1] == '(':
                l.pop()
            if i == ']' and l[-1] == '[':
                l.pop()
            if i == '}' and l[-1] == '{':
                l.pop()
        else:
            ok = False
if len(l)>0 or ok == False:
    print('No')
else:
    print('Yes')
    