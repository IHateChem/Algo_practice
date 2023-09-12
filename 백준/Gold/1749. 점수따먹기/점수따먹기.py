import sys
input=sys.stdin.readline
N,M=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(N)]
accumulated=[[0]*(M+1)]
for i in range(N):
    t=[0]
    for j in range(M):t.append(t[j]+MAP[i][j])
    accumulated.append(t)
for i in range(N):
    for j in range(M+1): accumulated[i+1][j] += accumulated[i][j]
answer=-1000000000000000000
for i in range(1,N+1):
    for j in range(i,N+1):
        for m in range(1,M+1):
            for n in range(m,M+1):
                if i == j:
                    if m == n:
                        t = accumulated[i][m]
                    else:
                        t = accumulated[i][n] - accumulated[i][m]
                else:
                    if m == n:
                        t = accumulated[j][m]- accumulated[i][m]
                    else:
                        t = accumulated[j][n] + accumulated[i][m] - accumulated[i][n] - accumulated[j][m]
                answer = max(answer, t)
print(answer)