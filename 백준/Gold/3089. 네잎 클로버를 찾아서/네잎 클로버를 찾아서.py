import sys
from bisect import bisect_left as bl, bisect_right as br
import heapq
input = sys.stdin.readline
N,M = map(int, input().split())
xAxis = [[] for _ in range(200001)]
yAxis = [[] for _ in range(200001)]
for _ in range(N):
    x, y = map(int,input().split())
    xAxis[y].append(x)
    yAxis[x].append(y)
x, y = 0, 0
orders = input().strip()
for _ in range(200001):
    xAxis[_].sort()
    yAxis[_].sort()
directions= {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}
for order in orders:
    if order == "R": x = xAxis[y][br(xAxis[y],x)]
    elif order == "L": x = xAxis[y][bl(xAxis[y],x)-1]
    elif order == "U": y = yAxis[x][br(yAxis[x],y)]
    else: y = yAxis[x][bl(yAxis[x],y)-1]
print(x,y)