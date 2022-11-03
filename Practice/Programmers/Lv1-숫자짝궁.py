https://school.programmers.co.kr/learn/courses/30/lessons/131128
from collections import Counter

def solution(X, Y):
    Z = Counter(X) & Counter(Y)
    if len(Z) == 0:
        return "-1"
    if max(Z) == "0":
        return "0"
    
    answer = []
    for k, v in Z.items():
        answer.extend(k * v)

    return ''.join(sorted(answer, reverse=True))
    