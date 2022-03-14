# https://www.acmicpc.net/problem/1907
from collections import Counter

m1m2, m3 = input().split('=')
m1, m2 = m1m2.split('+')

def decomposition(x:str):
    result = []
    for i in x:
        if i not in ['O', 'C', 'H']:
            tmp = result[-1] * int(i)
            result.extend(tmp[:-1])
        else:
            result.append(i)
    return result

breaker = False
for i in range(1, 11):
    if breaker:
        break
    for j in range(1, 11):
        if breaker:
            break
        for k in range(1, 11):
            t1, t2, t3 = m1*i, m2*j, m3*k
            if dict(Counter(decomposition(t1+t2))) == dict(Counter(decomposition(t3))):
                answer=[i, j, k]
                breaker = True
                break   
                
print(*answer)
            
