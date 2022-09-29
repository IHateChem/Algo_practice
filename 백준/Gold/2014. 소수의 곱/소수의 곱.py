import sys
import heapq
input = sys.stdin.readline
N, M = map(int,input().strip().split())
primes = list(map(int,input().strip().split()))
index = 0
numlog = {}
heap = [1]
n = -1
maxn =1 
while n < M:
    num = heapq.heappop(heap)
    for prime in primes:
        if len(heap) >= M and prime*num > maxn:
            break
        if not numlog.get(prime*num):
            numlog[prime*num] = 1
            heapq.heappush(heap,num*prime)
            maxn = max(prime*num, maxn)
    n += 1
print(num)
