import sys
from itertools import permutations as P
input = sys.stdin.readline
N, M = map(int, input().split())
inp = sorted(map(int, input().split()))
store = set()
for i in P(inp, M):
    if not tuple(i) in store:
        print(" ".join(map(str, i)))
        store.add(tuple(i))