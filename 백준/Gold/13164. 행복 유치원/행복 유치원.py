import sys
import heapq
input = sys.stdin.readline
N, M = map(int,input().strip().split())
children = list(map(int, input().strip().split()))
gap = [-children[i+1]+children[i] for i in range(N-1)]
tot = children[-1] - children[0]
groupnum = 1 
heapq.heapify(gap)
while gap:
    if groupnum == M:
        break
    g = heapq.heappop(gap)
    groupnum += 1
    tot += g
print(tot) 