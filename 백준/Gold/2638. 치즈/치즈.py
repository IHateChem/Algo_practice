import sys
input = sys.stdin.readline
N, M= map(int, input().split())
MAP = []; t = 0; num = -1; flag = True
for _ in range(N):
    MAP.append(list(map(int, input().split())))
def check(i,j):
    if MAP[i-1][j] % 2 == 0 or MAP[i][j-1]  % 2 == 0 or MAP[i+1][j]  % 2 == 0 or MAP[i][j+1]  % 2 == 0:
        return True
    return False

def check_melt(i,j):
    if MAP[i-1][j] // 2 +  MAP[i][j-1]  // 2 + MAP[i+1][j] // 2 + MAP[i][j+1]  // 2 >= 2:
        return True
    return False
flag = True; num = 0
while flag:
    flag = False
    stack = [(0,0)]
    visited = [ [0 for _ in range(M)] for __ in range(N)]
    visited[0][0] = 1
    while stack:
        i, j = stack.pop()
        MAP[i][j] = 2
        if i > 0:
            if not visited[i-1][j] and MAP[i-1][j] == 0: stack.append((i-1, j))
        if j > 0:
            if not visited[i][j-1] and MAP[i][j-1] == 0: stack.append((i, j-1))
        if i < N-1:
            if not visited[i+1][j] and MAP[i+1][j] == 0: stack.append((i+1, j))
        if j < M-1:
            if not visited[i][j+1] and MAP[i][j+1] == 0: stack.append((i, j+1))
    for i in range(1, N-1):
        for j in range(1, M-1):
            if MAP[i][j] == 1 and check_melt(i,j):
                MAP[i][j] = 0.5
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0.5 or MAP[i][j] == 2:
                MAP[i][j] = 0
            elif MAP[i][j] == 1:
                flag = True
    num += 1
print(num)