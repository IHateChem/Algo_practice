import sys
input = sys.stdin.readline
from itertools import combinations
N, M = map(int, input().split())
t = combinations(range(1, N+1), M)
for i in t:
    print(" ".join(map(lambda k: str(k), i)))