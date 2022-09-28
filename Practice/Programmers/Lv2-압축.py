def solution(msg):
    answer = []
    c = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {c[i]: i for i in range(1, 27)}
    skip_count = 0
    for i in range(len(msg)):
        if skip_count:
            skip_count -= 1
            continue
        cache = []
        for m in msg[i:]:
            cache.append(m)
            skip_count += 1
            if "".join(cache) not in dic:
                dic["".join(cache)] = len(dic) + 1
                answer.append(dic["".join(cache[:-1])])
                skip_count -= 2
                break
    answer.append(dic["".join(cache)])
    return answer


print(solution("TOBEORNOTTOBEORTOBEORNOT"))
