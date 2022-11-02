# https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import deque


def bfs(graph, wires, idx):
    local_graph = [i[:] for i in graph]
    local_wires = [i[:] for i in wires]
    del local_wires[idx]

    for wire in local_wires:
        local_graph[wire[0]].append(wire[1])
        local_graph[wire[1]].append(wire[0])

    visited = [0 for _ in range(len(local_graph))]
    queue = deque([1])
    visited[1] = 1

    while queue:
        v = queue.popleft()
        for i in local_graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

    return sum(visited)


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]
    for i in range(len(wires)):
        side_1 = bfs(graph, wires, i)
        answer = min(answer, abs(n - side_1 - side_1))
        print(answer)

    return answer


tf = [0, 0, 0]
if solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]) == 3:
    tf[0] = 1
print()
if solution(4, [[1, 2], [2, 3], [3, 4]]) == 0:
    tf[1] = 1
print()
if solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]) == 1:
    tf[2] = 1
print(tf)

