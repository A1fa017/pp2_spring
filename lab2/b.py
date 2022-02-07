n = int(input())
s = input().split()
l = []
for i in s:
    l.append(int(i))
l.sort()
print(l[-1]*l[-2])