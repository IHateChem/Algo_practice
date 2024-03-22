#dfs로 하기. 
#각 노드별 다음 엣지 정렬시키기. 
find = 0
def solution(tickets):
    answer = []
    graph = []
    airport2idx = {}
    idx2airport = []
    idx = 0
    start = -1
    visited = {}
    for a, b in tickets:
        if not a in airport2idx:
            airport2idx[a] = idx
            idx2airport.append(a)
            graph.append([])
            idx += 1
        if not b in airport2idx:
            airport2idx[b] = idx
            graph.append([])
            idx2airport.append(b)
            idx += 1
        if a == "ICN": start = airport2idx[a]
        graph[airport2idx[a]].append(b)
        t = (airport2idx[a], airport2idx[b])
        if t in visited:
            visited[t] += 1
        else:
            visited[t] = 1
    for node in graph:
        node.sort()
    path = []
    def dfs(a):
        global find
        path.append(idx2airport[a])
        if len(path) == len(tickets)+1:
            find = 1
            return
        for b in graph[a]:
            b = airport2idx[b]
            if not visited[(a,b)]: continue
            visited[(a,b)] -= 1
            dfs(b)
            if find: return
            visited[(a,b)] += 1
        if not find:
            path.pop()
        return
    dfs(start)
    return path