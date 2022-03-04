n = int(input())
def gen(n):
    for i in range(n):
        if i%4 == 0 and i%3 == 0:
            yield i
for num in gen(n):
    print(num)