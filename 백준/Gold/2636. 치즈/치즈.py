import sys
input = sys.stdin.readline
N, M= map(int, input().split())
MAP = []; t = 0; num = -1; flag = True
for _ in range(N):
    MAP.append(list(map(int, input().split())))
def check(i,j,t,MAP,visited,stack):
    if MAP[i][j] == 1:
        MAP[i][j] = "C"; t += 1
    elif MAP[i][j] == 0 and not visited[i][j]:
        visited[i][j] = 1; stack.append((i, j))
    return t
while flag:
    past = t; t = 0;  flag = False
    stack = [(0, 0)]
    visited = [[0]*M for _ in range(N)]; visited[0][0] = 1
    while stack:
        i, j = stack.pop()
        if MAP[i][j]==0:
            if i != N-1: t = check(i+1,j,t,MAP,visited,stack)
            if j !=M-1: t = check(i,j+1,t,MAP,visited,stack)
            if i !=0: t = check(i-1,j,t,MAP,visited,stack)
            if j !=0: t = check(i,j-1,t,MAP,visited,stack)
    for i in range(N):
        for j in range(M):
            if MAP[i][j]: flag = True
            if MAP[i][j] == "C": MAP[i][j] = 0
    num += 1
print(num); print(past)           