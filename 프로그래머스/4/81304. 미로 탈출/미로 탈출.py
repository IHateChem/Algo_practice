import heapq
def solution(n, start, end, roads, traps):
    power = [2**i for i in range(1001)]
    answer = 0
    traps = set(traps)
    graph = [[] for _ in range(n+1)]
    for p, q, s in roads:
        graph[p].append([q,0,s])
        graph[q].append([p,1,s])
    heap = [(0, start,power[start])]
    visited=set()
    while heap:
        t, u, p = heapq.heappop(heap)
        if (u,p) in visited: continue
        if u == end: break
        visited.add((u,p))
        curr = bool((power[u] & p) and u in traps)
        for q, b, s in graph[u]:
            nex = bool(power[q] & p and q in traps)
            if b == (curr+nex) % 2:
                nextPath = p ^ power[q]
                if (q, nextPath) in visited: continue
                heapq.heappush(heap, (t+s,q, nextPath))
    return t