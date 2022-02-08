s = input()
l = []
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
if len(l)>0:
    print('No')
else:
    print('Yes')