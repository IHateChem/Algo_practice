import heapq
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
id = 1
bears = []
leveldata = []
for i in range(K):
    prefer, level = map(int, input().split())
    bears.append( (level, prefer) )
bears.sort()
q = []
s = 0
answer = -1
for i in range(K):
    if i < N:
        s += bears[i][1] 
        heapq.heappush(q, bears[i][1])
    else:
        if q[0] <  bears[i][1]:
            it = heapq.heappop(q)
            s -= it
            heapq.heappush(q, bears[i][1])
            s += bears[i][1]
    if s >= M and i >= N-1 :
        answer = bears[i][0]
        break
print(answer)