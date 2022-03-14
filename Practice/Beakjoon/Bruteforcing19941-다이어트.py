#https://www.acmicpc.net/problem/19942
import sys
from itertools import combinations

n = int(input())
le = list(map(int, input().split()))
nums = np.array([list(map(int, input().split())) for _ in range(n)])


data = range(n)
search_list = list()
for i in range(1, n + 1):    
    c = list(combinations(data, i))
    search_list.extend(c)

result = [np.inf, []]
for search in search_list:
    tmp = np.sum(nums[list(search)], axis = 0)
    if sum(tmp[:-1] < le) != 0:
        continue
    if result[0] > tmp[-1]:        
        result[0] = min(result[0], tmp[-1])
        result[1] = list(search)

if result[0] == np.inf:
    print(-1)
else:
    print(result[0])
    print(' '.join(map(str, sorted(list(np.array(result[1]) + 1)))))
