import sys

input = sys.stdin.readline
n, m = map(int, input().split())
n_list = set([input() for _ in range(n)])
m_list = [input() for _ in range(m)]

answer = 0
for i in m_list:
    if i in n_list:
        answer += 1
        
print(answer)