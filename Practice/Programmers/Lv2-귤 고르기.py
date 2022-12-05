from collections import Counter


def solution(k, tangerine):
    answer = 0
    tangerine = dict(Counter(tangerine))
    sorted_by_value = sorted(tangerine, key=tangerine.get, reverse=True)

    for s in sorted_by_value:
        k -= tangerine[s]
        answer += 1
        if k <= 0:
            return answer
