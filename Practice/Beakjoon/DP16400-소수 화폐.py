'''
2 = 2 (1)
3 = 3 (1)
4 = 22 (1)
5 = 23, 5(2)
6 = 33, 222 (2)
7 = 223, 25, 7 (3)
8 = 2222, 233, 35 (3)

   0  1  2  3  4  5  6  7  8  
2 (1) 0  1  0  1  0  1  0  1  
3 (1) 0  0  1  0  1  1  1  1  
5 (1) 0  0  0  0  1  0  1  1
7 (1) 0  0  0  0  0  0  1  0
=     0  1  1  1  2  2  2  3
'''
def prime(n):
    t_f = [False, False] + [True for _ in range(2, n+1)]
    for i in range(2, n+1):
        if t_f[i]:
            for j in range(i*i, n+1, i):
                t_f[j] = False
    return t_f

n = int(input())
primes = prime(n)
cache = [0 for _ in range(n + 1)]
cache[0] = 1  # i-p 값
for p in range(len(primes)):
    if primes[p]:
        for i in range(p, n+1):
            cache[i] = (cache[i] + cache[i-p]) % 123456789

print(cache[n])