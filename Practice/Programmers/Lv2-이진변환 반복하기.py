def converter(n):
    tmp = ''
    while n:
        tmp += str(n % 2)  
        n = n // 2
    return tmp[::-1]

def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        len_s = len(s)
        len_one = s.count('1')
        answer[1] += len_s - len_one
        s = converter(len_one)
    return answer
