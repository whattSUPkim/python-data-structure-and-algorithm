# https://school.programmers.co.kr/learn/courses/30/lessons/12905#
# (중첩 반복으로 실패 -> 검색하여 dp 힌트 얻음)
def solution(board):
    if len(board) == 1:
        return board[0][0]

    answer = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue
            v = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
            board[i][j] = v
            answer = max(answer, v)

    return answer ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))

