import sys
input = sys.stdin.readline
N, M= map(int, input().split())
MAP = []; t = 0; num = -1; flag = True
for _ in range(N):
    MAP.append(list(map(int, input().split())))
while flag:
    past = t; t = 0;  flag = False
    stack = [(0, 0)]
    visited = [[0]*M for _ in range(N)]; visited[0][0] = 1
    while stack:
        i, j = stack.pop()
        if MAP[i][j]==0:
            if i != N-1:
                if MAP[i+1][j] == 1:
                    MAP[i+1][j] = "C"
                    t += 1
                elif MAP[i+1][j] == 0 and not visited[i+1][j]:
                    visited[i+1][j] = 1; stack.append((i+1, j))
            if j !=M-1:
                if MAP[i][j+1] == 1:
                    MAP[i][j+1] = "C"
                    t += 1
                elif MAP[i][j+1] == 0 and not visited[i][j+1]:
                    visited[i][j+1] = 1; stack.append((i, j+1))
            if i !=0:
                if MAP[i-1][j] == 1:
                    MAP[i-1][j] = "C"
                    t += 1
                elif MAP[i-1][j] == 0 and not visited[i-1][j]:
                    visited[i-1][j] = 1; stack.append((i-1, j))
            if j !=0:
                if MAP[i][j-1] == 1:
                    MAP[i][j-1] = "C"
                    t += 1
                elif MAP[i][j-1] == 0 and not visited[i][j-1]:
                    visited[i][j-1] = 1; stack.append((i, j-1))
    for i in range(N):
        for j in range(M):
            if MAP[i][j]: flag = True
            if MAP[i][j] == "C": MAP[i][j] = 0
    num += 1
print(num); print(past)           