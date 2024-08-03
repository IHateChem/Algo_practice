import sys
from itertools import combinations as C
import heapq
input = sys.stdin.readline
N,K,M=map(int,input().split())
stations = [[] for _ in range(N+1)]
lines = [list(map(int,input().split())) for _ in range(M)]
for n, line in enumerate(lines):
    for s in line:
        stations[s].append(n)
lineGraph = [set() for _ in range(M)]
for n, line in enumerate(lines):
    for s in line:
        for nextLine in stations[s]:
            if nextLine != n: lineGraph[n].add(nextLine)
heap = [(2, l) for l in stations[1]]
end = set(stations[N])
if N == 1:
    print(1)
    exit(0)
visited = set([])
while heap:
    w, l = heapq.heappop(heap)
    if l in end: break
    if l in visited: continue
    visited.add(l)
    for nextline in lineGraph[l]:
        if nextline in visited: continue
        heapq.heappush(heap, (w+1, nextline))
else:
    w = -1
print(w)