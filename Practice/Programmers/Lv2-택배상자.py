from collections import deque


def solution(order):
    answer = 0
    container = deque([i for i in range(1, len(order) + 1)])
    sub_container = []
    for o in order:
        while True:
            if sub_container and sub_container[-1] == o:
                sub_container.pop()
                answer += 1
                break
            if container:
                box = container.popleft()
                if box == o:
                    answer += 1
                    break
                else:
                    sub_container.append(box)
                    continue
            return answer

    return answer


q1, q2 = solution([4, 3, 1, 2, 5]), solution([5, 4, 3, 2, 1])
print(f"{q1==2} ... boxes = {q1}")
print(f"{q2==5} ... boxes = {q2}")
