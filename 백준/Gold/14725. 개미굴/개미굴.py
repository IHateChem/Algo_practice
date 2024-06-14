import sys
input = sys.stdin.readline

N = int(input())
graph = {}
for _ in range(N):
    path = list(input().strip().split())[1:]
    t = graph
    for node in path:
        if node in t:
            t = t[node]
        else:
            t[node] = {}
            t = t[node]
def _print(g, depth):
    for n in sorted(g.keys()):
        print("-"*depth + n)
        _print(g[n], depth+2)
_print(graph, 0)
        