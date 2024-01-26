from collections import defaultdict as dd
def findCreatedNodeAndInOut(edges, ins, outs):
    for a, b in edges:
        outs[b] += 1
        ins[a] += 1
    for k, v in ins.items():
        if v >= 2 and not outs[k]: return k
def getStartNodes(edges, cNode):
    return [b for a, b in edges if a == cNode]
def buildGraph(edges, cNode):
    n = 1000000
    inGraph = [[] for _ in range(n+1)]
    outGraph = [[] for _ in range(n+1)]
    for a, b in edges:
        if a == cNode: continue
        inGraph[a].append(b)
        outGraph[b].append(a)
    return inGraph, outGraph
def findConnections(graph, node, visited):
    q = [node]
    while q:
        node = q.pop()
        for v in graph[node]:
            if v in visited: continue
            visited.add(v)
            q.append(v)
def solution(edges):
    ins = dd(int); outs = dd(int)
    cNode = findCreatedNodeAndInOut(edges, ins, outs)
    startNodes = getStartNodes(edges, cNode)
    inGraph, outGraph = buildGraph(edges, cNode)
    groups = []
    for node in startNodes:
        visited = set([node])
        findConnections(inGraph, node, visited)
        findConnections(outGraph, node, visited)
        groups.append(visited)
    answer = [cNode,0,0,0]
    for group in groups:
        n = len(group)
        edge = 0
        for v in group:
            edge += ins[v]
        if edge == n + 1: answer[3] += 1
        elif edge == n - 1: answer[2] += 1
        else: answer[1] += 1
    return answer