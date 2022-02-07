a = int(input())
b = input()

if b == 'k':
    c = input()
    s = '{:.' + c + 'f}'
    print(s.format(a/1024))
elif b == 'b':
    print(a*1024)