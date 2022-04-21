# https://www.acmicpc.net/problem/1500

s, k = map(int, input().split())

q = s // k
r = s - q * k

nums = [q] * k
answer = 1
for i in range(k):
    if r != 0:
        nums[i] += 1
        r -= 1
        answer *= nums[i]
    else:
        answer *= nums[i]

print(answer)

