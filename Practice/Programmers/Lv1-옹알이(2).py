# https://school.programmers.co.kr/learn/courses/30/lessons/133499#

def solution(babbling):
    answer = 0
    can_do = ['aya', 'ye', 'woo', 'ma']
    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b: continue    
        for do in can_do: b = b.replace(do, '0')
        try:
            int(b)
            answer += 1
        except:
            continue

    return answer