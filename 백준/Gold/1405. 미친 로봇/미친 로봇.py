import sys
input = sys.stdin.readline
N, P1, P2, P3, P4 = map(int, input().split())
p = [P1/100, P2/100, P3/100, P4/100]
x = 0; y = 0
dx = {0: 0, 1: 0, 2: 1, 3: -1}
dy = {0: 1, 1: -1, 2: 0, 3: 0}
def move(N, path, x, y):
    if N == 0: return 0
    answer = 0
    for i in range(4):
        if not p[i]: continue
        if (x+dx[i], y+dy[i]) in path:
            answer += p[i]
        else:
            path.add((x+dx[i], y+dy[i]))
            answer += p[i] * move(N-1, path,  x+dx[i], y+dy[i])
            path.remove((x+dx[i], y+dy[i]))
    return answer
print(1-move(N, set([(0, 0)]), 0, 0))