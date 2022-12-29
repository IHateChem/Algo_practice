import sys
input = sys.stdin.readline
N = int(input())
MAP = []
def _cmp(x, y):
    if ccw(s, x, y) < 0: return 1
    if ccw(s, x, y) > 0: return -1
    return -1 if dist(x, s) < dist(y, s) else 1
def dist(x, y):
    return (x[0]-y[0])**2+(x[1]-y[1])**2
def ccw(p1, p2, p3):
    return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))
def get_slope(p1, p2):
    return float('inf') if p1[0] == p2[0] else round((p1[1]-p2[1])/(p1[0]-p2[0]), 9)
for _ in range(N):
    MAP.append(list(map(int, input().split())))
MAP.sort(key = lambda t: (t[0], t[1]))
s = MAP[0]
from functools import cmp_to_key
MAP.sort(key = cmp_to_key(_cmp))
#MAP.sort(key = lambda t: (get_slope(t, s), -t[1], t[0]))
pnt = 1
stack = [s, MAP[0]]
while pnt < N:
    second = stack.pop()
    first = stack.pop()
    next = MAP[pnt]
    t = ccw(next, second, first)
    if t < 0:
        pnt  += 1 
        stack.append(first)
        stack.append(second)
        stack.append(next)
    else:
        stack.append(first)
        if len(stack) < 2:
            stack.append(next)
            pnt += 1
print(len(set(tuple(map(tuple, stack)))))
