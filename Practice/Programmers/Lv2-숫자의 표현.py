# https://school.programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    answer = 1
    for i in range(1, n):
        tmp = i
        for j in range(i+1, n):
            tmp += j
            if tmp > n:
                break
            elif tmp == n:
                answer += 1
                break
            
    return answer