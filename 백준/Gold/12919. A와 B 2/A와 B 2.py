import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
S = input().strip()
T = input().strip()
from collections import defaultdict as dd
history = dd(bool)
def reduce(w):
    if not w: return
    if w == S:
        print(1)
        exit()
    if w[-1] == "A":
        if not history[w[:-1]]:
            history[w[:-1]] = True
            reduce(w[:-1])
    if w[0] == "B":
        k = w[1:][::-1]
        if not history[k]:
            history[k] = True
            reduce(k)
reduce(T)
print(0)