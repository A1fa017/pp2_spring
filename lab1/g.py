import math
s = input()
t = s[::-1]
sum = 0
a = 0
for i in t:
    sum += pow(2,a)*int(i)
    a += 1
print(sum)