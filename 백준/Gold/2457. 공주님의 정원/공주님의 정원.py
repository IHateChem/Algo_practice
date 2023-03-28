import sys
import heapq
input = sys.stdin.readline
N = int(input())
date = [0, 31, 28, 31,30,31,30,31,31,30,31,30,31]
flowers = [tuple(map(int, input().split())) for i in " "*N]
heapq.heapify(flowers)
current = [0,0]
start = [3,1]
end = [3,1]
answer = 1
while flowers:
    a, b, c, d = heapq.heappop(flowers)
    if [c,d] > end:
        if start < [a,b]:
            if end > start and [a, b] <= end:
                start = [i for i in end]
                answer += 1
            else:
                print(0)
                exit()
        current = [a,b]
        end = [c,d]
    if end > [11,30]: break
else:
    print(0)
    exit()
print(answer)