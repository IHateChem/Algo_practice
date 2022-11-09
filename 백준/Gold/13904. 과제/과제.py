import sys
import heapq
input = sys.stdin.readline
N = int(input())
stack = []
hwlists = []
for _ in range(N):
    d, w = map(int, input().split())
    hwlists.append((d, w))
hwlists.sort(reverse = True)
day = 0
while hwlists:
    d,w = hwlists.pop()
    day += 1
    if not stack:
        stack.append((w,d))
        continue
    if d < day:
        day -= 1
        if w > stack[0][0]:
            heapq.heappop(stack)
            heapq.heappush(stack,(w,d))
            continue
    else:
        heapq.heappush(stack, (w,d))
print(sum(map(lambda t: t[0], stack)))