from collections import deque


def solution(n):
    minimap = [[0 for _ in range(n)] for __ in range(n)]
    move = list(reversed([i for i in range(n + 1)][1:]))
    now, p = [-1, 0], 1
    movements = deque([(1, 0), (0, 1), (-1, -1)])
    for m in move:
        movement = movements.popleft()
        for i in range(m):
            now[0] += movement[0]
            now[1] += movement[1]
            minimap[now[0]][now[1]] = p
            p += 1
        movements.append(movement)
    answer = [n for n in sum(minimap, []) if n != 0]
    return answer
