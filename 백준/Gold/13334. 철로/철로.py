import heapq
import sys
input = sys.stdin.readline
N = int(input())
answer = 0
t=  []
for _ in range(N):
    a, b = map(int, input().split())
    t.append((a, b) if a < b else (b, a))
d = int(input())
MAP = []
candidates = set()
points = set()
for i in t:
    if i[1] - i[0] <= d:
        MAP.append(i)
        candidates.add(i[0])
        points.add(i[0])
        points.add(i[1])
impossible = []; can = [];possible = []
MAP.sort(reverse=True)
pnt = 0
for start in sorted(list(candidates)):
    end = start + d
    while MAP and MAP[-1][0] < end:
        t = MAP.pop()
        if t[1] <= end: heapq.heappush(can, t)
        else: heapq.heappush(possible, (t[1], t[0]))
    while possible and possible[0][0] <= end:
        t = heapq.heappop(possible)
        heapq.heappush(can, (t[1], t[0]))
    while can and can[0][0] < start:
        t = heapq.heappop(can)
    answer = max(answer, len(can))
print(answer)