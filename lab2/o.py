s = input()
t = ''
d,l = '',''
dic = {
    'ZER' : 0,
    'ONE' : 1,
    'TWO' : 2,
    'THR' : 3,
    'FOU' : 4,
    'FIV' : 5,
    'SIX' : 6,
    'SEV' : 7,
    'EIG' : 8,
    'NIN' : 9,}
a = 0

for i in s:
    t += i
    if t in dic:
        d += str(dic[t])
        t = ''
    if i == '+':
        t = ''
        break
    a += 1

for j in range(a+1,len(s)):
    t += s[j]
    if t in dic:
        l += str(dic[t])
        t = ''
y = int(d) + int(l)

for x in str(y):
    for key in dic:
        if int(x) == dic[key]:
            print(key,end='')