import heapq
import sys
input=sys.stdin.readline
N=int(input())
programmers = list(map(int,input().split()))
l = 0
r = N-1
answer = (N-2)*min(programmers[0], programmers[-1])
while l < r:
    if programmers[l] < programmers[r]:
        l += 1
    else:
        r -= 1
    answer = max(answer, (r-l-1)*min(programmers[l], programmers[r]))
print(answer)