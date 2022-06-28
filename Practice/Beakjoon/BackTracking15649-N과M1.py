# https://www.acmicpc.net/problem/15649

''' permutations 사용
from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]
answers = list(permutations(nums, m))
for answer in answers:
    print(' '.join(map(str, answer)))
'''

# 백트래킹 사용
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
 
sup = []
 
def dfs():
    if len(sup)==m:
        print(' '.join(map(str, sup)))
        return
    
    for i in range(1,n+1):
        if i not in sup:
            sup.append(i)
            dfs()
            sup.pop()
 
dfs()
