import sys
input = sys.stdin.readline

s = list(map(int, input().rstrip()))
min_flip = 1e+8

if sum(s) == len(s) or sum(s) == 0:
    print(0)

else:
    for t in range(2):
        s_copied = s[:]
        temp = -1
        flip_n = 0
        for i in s_copied:
            if i != temp:
                temp = i
                if i == t:
                    flip_n += 1
        min_flip = min(min_flip, flip_n)

    print(min_flip)
