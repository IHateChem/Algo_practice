def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for x, y in roads:
        graph[y].append(x)
        graph[x].append(y)
    distances = [200000 for _ in range(n+1)]
    q = [destination]
    t = []
    dist = 0
    visited = set([destination])
    while q:
        u = q.pop()
        distances[u] = dist
        for v in graph[u]:
            if v in visited: continue
            visited.add(v)
            t.append(v)
        if not q:
            dist += 1
            q = t
            t = []
    for s in sources:
        if distances[s] == 200000:
            answer.append(-1)
        else: answer.append(distances[s])
    return answer