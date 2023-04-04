import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [(-1*i, m) for m, i in enumerate(map(int, input().split()))]
timelimit = 24*N
heapq.heapify(B)
while timelimit and B:
    b, n = heapq.heappop(B)
    b *= -1
    if timelimit - (100-A[n])//b >= 0:
        timelimit -= (100-A[n])//b
        t = (100-A[n])//b
    else:
        t = timelimit
        timelimit = 0
    A[n] += t*b
    if 100-A[n]:
        heapq.heappush(B, (-1*(100-A[n]), n))
print(sum(A))