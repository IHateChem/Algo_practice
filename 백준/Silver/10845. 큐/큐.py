import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
c =  deque()
for _ in range(N):
    a = input().rstrip().split()
    if len(a) == 1:
        if a[0] == "front": print(c[0] if c else -1)
        elif a[0] == "back": print(c[-1] if c else -1)
        elif a[0] == "size": print(len(c))
        elif a[0] == "empty": print(0 if c else 1)
        else: print(c.popleft() if c else -1)
    else:
        b = int(a[1])
        c.append(b)