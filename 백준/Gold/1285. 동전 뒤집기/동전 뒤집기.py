import sys
input = sys.stdin.readline
N = int(input())
answer = N*N;
MAP = [[0 if i == "H" else 1 for i in input().strip()] for _ in range(N)]

for i in range(2**N):
    t = 0
    flip = []
    for j in range(N):
        if 2**j & i:
            for k in range(N):
                MAP[k][j] = not MAP[k][j]
    for j in range(N):
        if sum(MAP[j]) > N // 2:
            flip.append(j)
            for k in range(N):
                MAP[j][k] = not MAP[j][k]
        t+= (sum(MAP[j]))
    answer = min(answer, t)
    for j in flip:
        for k in range(N):
            MAP[j][k] = not MAP[j][k]
    for j in range(N):
        if 2**j & i:
            for k in range(N):
                MAP[k][j] = not MAP[k][j]
print(answer)             