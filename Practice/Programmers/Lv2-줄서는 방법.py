from math import factorial


def solution(n, k):
    list_n = [i for i in range(1, n + 1)]
    answer = []
    N = n
    k -= 1
    while len(answer) < N:
        idx = int(k // (factorial(n) // n))
        answer.append(list_n[idx])

        del list_n[idx]
        k = int(k % (factorial(n) // n))
        n -= 1
    return answer
