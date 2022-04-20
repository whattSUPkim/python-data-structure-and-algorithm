# https://www.acmicpc.net/problem/11000

import sys
import heapq
input = sys.stdin.readline

n = int(input())
schedule = list()
for i in range(n):
    schedule.append(list(map(int, input().split())))
schedule.sort(key=lambda x: (x[0], x[1]))
classroom = list()

heapq.heappush(classroom, schedule[0][1])
for i in range(1, n):
    time = schedule[i]
    if classroom[0] <= time[0]:
        heapq.heappushpop(classroom, time[1])
    else:
        heapq.heappush(classroom, time[1])

print(len(classroom))