# https://school.programmers.co.kr/learn/courses/30/lessons/12978
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    for r in road:
        graph[r[0]].append([r[1], r[2]])
        graph[r[1]].append([r[0], r[2]])

    visited = [500001 for _ in range(N + 1)]

    def dfs(graph, v, cnt):
        visited[v] = cnt
        for g in graph[v]:
            i, k = g
            if cnt + k > K or visited[i] <= cnt + k:
                continue
            dfs(graph, i, cnt + k)

    dfs(graph, 1, 0)
    for v in visited:
        if v != 500001:
            answer += 1
    return answer

