import heapq
def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]
    for a,b, c in paths:
        graph[a].append((c,b))
        graph[b].append((c,a))
        
    # gates, summits여부를 지속적으로 확인해야 하므로 set으로 한다.     
    gates = set(gates)
    summits = set(summits)
    
    # heap을 통해 summit을 향해 나아간다. 
    intensity = 10000001
    summit = -1
    for gate in gates:
        t = 0
        visited = set()
        heap =[(c,a) for c,a in graph[gate] if not a in gates]
        heapq.heapify(heap)
        while heap:
            w, a = heapq.heappop(heap)
            if a in visited: continue
            t = max(t, w)
            visited.add(a)
            if a in summits:
                if intensity > t:
                    summit = a
                    intensity = t
                if intensity == t and summit > a:
                    summit = a
                break
            for nw, b in graph[a]:
                if b in visited  or b in gates: continue
                heapq.heappush(heap, (nw,b))
    return summit, intensity