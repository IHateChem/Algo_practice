import sys
from itertools import combinations as com
input = sys.stdin.readline
N, M= map(int, input().split())
answer = 0; MAP = []; house = []; chicken = []; stack = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))
for i, m in enumerate(MAP):
    for j , n in enumerate(m):
        if n == 1:
            house.append((i, j))
        elif n == 2:
            chicken.append((i, j))
com_chick = com(chicken, M)
answer = 2e8
for chick in com_chick:
    tot = 0
    for cx, cy in house:
        t = 200
        for x, y in chick:
            t = min(t, abs(cx-x) + abs(cy-y))
        tot += t
    answer = min(tot, answer)
print(answer)