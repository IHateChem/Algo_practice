import sys
from collections import defaultdict as dd
input = sys.stdin.readline
n, m = map(int, input().split())
visited = dd(int)
def C(a, b):
    if a == b or b == 0:
        return 1
    elif b == 1:
        return a
    if visited[(a, b)]:
        return visited[(a, b)]
    t = C(a-1, b-1) + C(a-1, b)
    visited[(a, b)] = t
    return t
print(C(n, m))