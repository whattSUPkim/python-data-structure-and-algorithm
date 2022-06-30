#https://www.acmicpc.net/problem/15650
def dfs():
    if len(sup) == m:
        answers.append(sup.copy())
        return
    
    for i in range(1, n+1):
        if i in sup:
            continue
        sup.append(i)
        dfs()
        sup.pop()

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sup = list()
answers = list()

dfs()

sup = set()
for answer in answers:
    if tuple(sorted(answer)) in sup:
        continue
    for num in answer:
        print(num, end=' ')
    print()
    sup.add(tuple(sorted(answer)))
    