
def solution(sales, links):
    N = len(sales)
    graph = [[] for _ in range(N)]
    for a,b in links:
        graph[a-1].append(b-1)
    q = []
    def dfs(n):
        q.append(n)
        for v in graph[n]:
            dfs(v)
    dfs(0)
    dp1 = [s for s in sales]
    dp2 = [0 for _ in sales]
    while q:
        n = q.pop()
        if not graph[n]: continue
        t = 0
        for i, v in enumerate(graph[n]):
            t += min(dp1[v], dp2[v])
        dp1[n] = dp1[n] + t
        dp2[n] = 10000000000
        for i, u in enumerate(graph[n]):
            t = 0
            for j, v in enumerate(graph[n]):
                if i!= j: t += min(dp1[v], dp2[v])
                else: t += dp1[v]
            dp2[n] = min(dp2[n], t)
    return min(dp1[0], dp2[0])