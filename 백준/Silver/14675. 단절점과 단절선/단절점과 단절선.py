import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
edges = []
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    edges.append((a,b))
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    if a == 1:
        if len(graph[b]) < 2:
            print("no")
        else:
            print("yes")
    else:
        print("yes")