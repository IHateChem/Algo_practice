import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N, M = map(int, input().split())
MAP = []
pos = [[] for _ in range(M+1)]
for i in range(N):
    MAP.append(list(map(int, input().split())))
    for n, j in enumerate(MAP[-1]):
        if j:
            pos[j].append((i, n))
S, X, Y = map(int, input().split())
def check(x, y, n, t):
    if x > 0:
        if not MAP[x-1][y]:
            MAP[x-1][y] = n
            t.append((x-1, y))
    if y > 0:
        if not MAP[x][y-1]:
            MAP[x][y-1] = n
            t.append((x, y-1))
    if x < N-1:
        if not MAP[x+1][y]:
            MAP[x+1][y] = n
            t.append((x+1, y))
    if y < N-1:
        if not MAP[x][y+1]:
            MAP[x][y+1] = n
            t.append((x, y+1))


def contimination(t):
    for _ in range(t):
        for i in range(1, M+1):
            t = []
            for x, y in pos[i]:
                check(x, y, i, t)
            pos[i] = t
contimination(S)
print(MAP[X-1][Y-1])