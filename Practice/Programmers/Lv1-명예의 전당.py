# https://school.programmers.co.kr/learn/courses/30/lessons/138477


def solution(k, score):
    answer = []
    top_k = []
    for s in score:
        if len(top_k) < k:
            top_k.append(s)
            answer.append(min(top_k))
            continue
        top_k.append(s)
        top_k.sort(reverse=True)
        top_k.pop()
        answer.append(top_k[-1])

    return answer
