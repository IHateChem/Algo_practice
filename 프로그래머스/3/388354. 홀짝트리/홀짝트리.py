import sys
sys.setrecursionlimit(10**6)
def solution(nodes, edges):
    orgNode2seq = {node: n for n, node in enumerate(nodes)}
    seq2orgNode = {n: node for node, n in orgNode2seq.items()}
    graph = [[] for _ in nodes]
    
    for u, v in edges:
        u_idx = orgNode2seq[u]
        v_idx = orgNode2seq[v]
        graph[u_idx].append(v_idx)
        graph[v_idx].append(u_idx) 
        

    visited = [False] * len(nodes)
    forest = []

    def dfs(u, tree):
        visited[u] = True
        tree.append(seq2orgNode[u])
        for v in graph[u]:
            if not visited[v]:
                dfs(v, tree)
    # 모든 노드를 방문하며 포레스트 구성
    for i in range(len(nodes)):
        if not visited[i]:
            tree = []
            dfs(i, tree)
            forest.append(tree)
            
    numOfChildredIfNotRoot = [len(g) - 1 for g in graph]
    answer = [0,0]
    for tree in forest:
        evenOrOdd = 0
        reverseEvenOrOdd = 0
        for node in tree:
            n = orgNode2seq[node]
            num = numOfChildredIfNotRoot[n]
            if (node % 2 == 1 and num % 2 == 1) or (node % 2 == 0 and num % 2 == 0):
                evenOrOdd += 1
            if (node % 2 == 0 and num % 2 == 1) or (node % 2 == 1 and num % 2 == 0):
                reverseEvenOrOdd += 1
        if evenOrOdd == 1:
            answer[1] += 1
        if reverseEvenOrOdd == 1:
            answer[0] += 1

    return answer