# # https://www.acmicpc.net/problem/9663
def check(x):
    for r in range(x):
        if row[x] == row[r] or abs(row[x] - row[r]) == abs(x-r): # 같은 열  or  대각(행-행 == 열-열)
            return False
    
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
        return

    else:
        for col in range(n):  # col
            # [x, col]: queen
            row[x] = col   # [0,0]
            if check(x):
                dfs(x+1)


n = int(input())
row = [0 for _ in range(n)]
result = 0

dfs(0)
print(result)