import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
computer = [-m]
answer = 0
schedule = []
for _ in range(n):
    schedule.append(list(map(int, input().split())))
schedule.sort()
for a, s in schedule:
    heapq.heappush(computer, a+s)
    if computer[0] <= a:
        p = heapq.heappop(computer) 
        while p + m < a and computer[0] <= a:
            p = heapq.heappop(computer)
        if p + m < a: answer += 1
    else:
        answer += 1
print(n-answer)