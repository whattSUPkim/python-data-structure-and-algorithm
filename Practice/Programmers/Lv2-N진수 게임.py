def converter(a, b):
    convertString = "0123456789ABCDEF"
    sol = ""
    if a < b:
        return convertString[a]
    while a >= b:
        n = divmod(a, b)
        a //= b
        sol += convertString[n[1]]
    sol += convertString[n[0]]
    return sol[::-1]


def solution(n, t, m, p):
    answer = ""
    p = p - 1
    waiting = list()
    now = 0
    while len(waiting) < t * m:
        waiting.extend(list(converter(now, n)))
        now += 1
    for i in range(p, t * m, m):
        answer += waiting[i]

    return answer
