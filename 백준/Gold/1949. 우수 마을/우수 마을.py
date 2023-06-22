import sys
from collections import deque
sys.setrecursionlimit(50000)
input = sys.stdin.readline
N = int(input())
villages = [0]+list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
goodDp = [0]*(N+1)
badDp = [0]*(N+1)
visited = [0]*(N+1)
def topDownBad(village, history:set):
    if badDp[village]: return badDp[village]
    history.add(village)
    bad = 0
    for next in graph[village]:
        if next in history: continue
        bad += max(topDownBad(next, history), topDownGood(next,history))
    badDp[village] = bad
    history.remove(village)
    return bad
def topDownGood(village, history):
    if goodDp[village]: return goodDp[village]
    history.add(village)
    good = villages[village]
    for next in graph[village]:
        if next in history: continue
        good += topDownBad(next, history)
    goodDp[village] = good
    history.remove(village)
    return good
print(max(topDownBad(1, set()), topDownGood(1, set())))