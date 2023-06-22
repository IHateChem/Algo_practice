import sys
import heapq
input = sys.stdin.readline
while 1:
    try:
        X,Y,D,T=map(int, input().split())
        distance = (X**2 + Y**2)**0.5
        stack = [(0.0,0.0, 0)]
        while stack:
            time, dist, flag =  heapq.heappop(stack)
            if dist >= distance and flag > 1: break
            dx = distance -dist
            heapq.heappush(stack, (time+abs(dx), dist+dx, flag + 2))
            heapq.heappush(stack, (time+T, dist+D, flag + 1))
        print(time)
    except:
        break