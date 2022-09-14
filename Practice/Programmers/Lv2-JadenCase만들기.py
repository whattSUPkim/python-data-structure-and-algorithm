# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    save = list()
    for i in range(len(s)):
        if s[i] == ' ':
            save.append(i)

    s = s.split()
    answer = list()
    for word in s:
        if word[0].isalpha():
            answer.extend(list(word.capitalize()))
        else: 
            answer.extend(list(word.lower()))
    
    for i in save:
        answer.insert(i, ' ')
    
    return ''.join(answer)
    