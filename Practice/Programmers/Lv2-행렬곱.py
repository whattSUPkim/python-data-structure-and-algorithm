"""
import numpy as np


def solution(arr1, arr2):
    return np.dot(arr1, arr2).tolist()
"""


def solution(arr1, arr2):
    answer = list()
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr2)):
                tmp += arr1[i][k] * arr2[k][j]
            answer[i].append(tmp)
    return answer
