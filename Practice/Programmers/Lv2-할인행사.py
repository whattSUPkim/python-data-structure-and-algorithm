# https://school.programmers.co.kr/learn/courses/30/lessons/131127#


def solution(want, number, discount):
    sum_of_number = sum(number)
    target = {want[i]: number[i] for i in range(len(want))}
    answer = 0
    for i in range(len(discount)):
        target_copied = target.copy()
        flag = True
        if len(discount) - i < sum_of_number:
            break
        for item in discount[i : i + sum_of_number]:
            try:
                target_copied[item] -= 1
                if target_copied[item] < 0:
                    flag = False
                    break
            except:
                flag = False
                break
        if flag:
            answer += 1
    return answer
