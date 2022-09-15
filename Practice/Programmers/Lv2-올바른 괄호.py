# https://school.programmers.co.kr/learn/courses/30/lessons/12909
def converter(a):
    if a == '(':
        return 1
    else:
        return -1

def solution(s):
    monitor = 0
    for a in s:
        monitor += converter(a)
        if monitor < 0:
            return False
    
    return monitor == 0
