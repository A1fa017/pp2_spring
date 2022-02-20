l = map(int, input().split())

def filter_prime(l, prime_nums = ''):
    for num in l:
        ok = True
        for subnum in range(2, num):
            if num%subnum == 0:
                ok = False
        if ok == True:
            prime_nums += str(num) + ' '
    return prime_nums

print(filter_prime(l))