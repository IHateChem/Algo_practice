import sys
input = sys.stdin.readline
N = int(input())
builds = []
postions = set()
for _ in range(N):
    L,H,R=map(int,input().split())
    postions.add(L)
    postions.add(R)
    builds.append((L,H,R))
sweepIn = [set() for  _ in " "*len(postions)]
sweepOut = [set() for  _ in " "*len(postions)]
idx2pos = {i: j for i,j in enumerate(sorted(list(postions)))}
pos2idx = {j: i  for i,j in enumerate(sorted(list(postions)))}
for l,h,r in builds:
    idx_l = pos2idx[l]
    idx_r = pos2idx[r]
    sweepIn[pos2idx[l]].add((-1*h,l))
    sweepOut[pos2idx[r]].add((-1*h,l))
import heapq
heap = []
answer = []
done = set()
for i in range(len(postions)):
    for j in sweepIn[i]:
        heapq.heappush(heap, j)
    while heap and heap[0] in done:
        heapq.heappop(heap)
    if not heap:
        print(1)
    top = heap[0][0]*-1
    if i == 0 or top != answer[-1]:
        answer.append(idx2pos[i])
        answer.append(top)
    for j in sweepOut[i]:
        done.add(j)
    while heap and heap[0] in done:
        heapq.heappop(heap)
    if not heap:
        answer.append(idx2pos[i])
        answer.append(0)
    elif heap[0][0]*-1 != answer[-1]:
        answer.append(idx2pos[i])
        answer.append(heap[0][0]*-1)
print(*answer)


