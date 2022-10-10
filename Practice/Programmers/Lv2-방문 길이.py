def solution(dirs):
    # 키보드 세팅
    mr = [-1, 1, 0, 0]
    mc = [0, 0, -1, 1]
    keyboard = {"U": 0, "D": 1, "L": 2, "R": 3}

    # 맵 세팅
    minimap = [[set() for _ in range(11)] for _ in range(11)]

    # game start
    now = [5, 5]
    cnt = 0

    for d in dirs:
        nr = now[0] + mr[keyboard[d]]
        nc = now[1] + mc[keyboard[d]]
        if nr < 0 or nr > 10 or nc < 0 or nc > 10:
            continue
        if (nr, nc) not in minimap[now[0]][now[1]]:
            cnt += 1
            minimap[now[0]][now[1]].add((nr, nc))
            minimap[nr][nc].add((now[0], now[1]))
        now = [nr, nc]
    return cnt


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
