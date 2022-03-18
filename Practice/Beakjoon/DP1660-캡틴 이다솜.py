# https://www.acmicpc.net/problem/1660
'''
cal -> n(n+1) / 2
cases[i] = cases[i-1] + cal(i)
(반복)case 
  -> cache[idx] = min(cache[idx], cache[idx - case] + 1)
'''
import sys
input = sys.stdin.readline

def cal(n):
    return int(n * (n+1) / 2)

n = int(input())
cases = [0]
idx = 1
while True:
    tmp = cases[idx-1] + cal(idx)
    if tmp > n:
        break
    cases.append(tmp)
    idx += 1   

cache = [0] + [999999 for _ in range(n)]
for case in cases[1:]:
    cache[case] = 1
    for j in range(case, len(cache)):
        cache[j] = min(cache[j], cache[j-case] + 1)

print(cache[n])