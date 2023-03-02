import heapq as hq
def union(g, u, v):
    p_u = find(g, u)
    p_v = find(g, v)
    g[p_u] = p_v
def find(g, u):
    if g[u] == u: return u
    g[u] = find(g, g[u])
    return g[u]
def solution(n, costs):
    answer = 0
    stack  = []
    group = [_  for _ in range(n)]
    for cost in costs:
        hq.heappush(stack, (cost[2], cost[0], cost[1]))
    while stack:
        w, u, v = hq.heappop(stack)
        if find(group,u) != find(group, v):
            union(group, u, v)
            answer += w
        else: continue
    return answer