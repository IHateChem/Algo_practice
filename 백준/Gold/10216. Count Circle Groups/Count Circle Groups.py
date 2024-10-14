import sys
input = sys.stdin.readline

T  = int(input())

getdist = lambda x, y: ((x[0] - y[0])**2 + (x[1] - y[1])**2)
isLinked =  lambda node1, node2 : getdist(node1, node2) <= (node1[2] + node2[2])**2
def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)
    return parents[x]
def union(x, y, parents):
    x = find(x, parents)
    y = find(y, parents)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    
for _ in range(T):
    N = int(input())
    nodes = []
    for i in range(N):
        nodes.append(tuple(map(int, input().split())))
    parents = [i for i in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if isLinked(nodes[i], nodes[j]):
                union(i, j, parents)
    for i in range(N):
        find(i, parents)
    print(len(set(parents)))