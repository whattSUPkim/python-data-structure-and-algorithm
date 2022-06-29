# https://www.acmicpc.net/problem/16236
def find_baby_shark():
    for r in range(len(minimap)):
        for c in range(len(minimap[r])):
            if minimap[r][c] == 9:
                return r, c

def set_default(baby_shark):
    queue = deque()
    queue.append((baby_shark[0], baby_shark[1], 0))
    visited = set()
    return queue, visited

def find_and_move():
    global baby_shark, baby_shark_lv, baby_shark_exp, result
    limit = 9999999999  # moving별 경계 나누기용
    possible_list = list()
    while queue:
        now_r, now_c, moving = queue.popleft()
        if moving > limit:
            break
        for i in range(4):
            next_r, next_c = now_r+mr[i], now_c+mc[i]
            if next_r < 0 or next_r > n-1 or next_c < 0 or next_c > n-1:
                continue
            if minimap[next_r][next_c] > baby_shark_lv:
                continue
            if (next_r, next_c) in visited:
                continue
            if minimap[next_r][next_c] < baby_shark_lv and minimap[next_r][next_c] != 0:
                possible_list.append([next_r, next_c, moving + 1])
                limit = moving
            queue.append([next_r, next_c, moving + 1])
            visited.add((next_r, next_c))
             
    if possible_list:
        next_r, next_c, moved = sorted(possible_list, key=lambda x: (x[2], x[0], x[1]))[0]
        result += moved
        baby_shark = (next_r, next_c)
        baby_shark_exp += 1
        minimap[next_r][next_c] = 0
        if baby_shark_exp >= baby_shark_lv:
            baby_shark_lv += 1
            baby_shark_exp = 0
        return True

    return False



import sys
from collections import deque
input = sys.stdin.readline

# setting
n = int(input())
minimap = [list(map(int, input().split())) for _ in range(n)]
baby_shark = find_baby_shark()
minimap[baby_shark[0]][baby_shark[1]] = 0
baby_shark_lv = 2
baby_shark_exp = 0
result = 0
mr, mc = [-1, 0, 0, 1], [0, -1, 1, 0]  # 상 좌 우 하

# main
while True:
    queue, visited = set_default(baby_shark)
    if not find_and_move():
        break

print(result)