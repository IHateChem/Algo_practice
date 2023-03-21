#실력 좋은 사람이 이김.
def dfs(i, graph, visited):
    rank = 0
    visited[i] = 1
    for k in graph[i]:
        if visited[k]:
            continue
        rank += dfs(k, graph, visited)
    return rank + 1
def solution(n, results):
    graph = [[] for _ in range((n+1))]
    r_graph = [[] for _ in range((n+1))]
    win_ranks = [0 for _ in range(n+1)]
    lose_ranks = [0]*(n+1)
    answer = 0
    for a, b in results:
        graph[a].append(b)
        r_graph[b].append(a)
    for i in range(n+1):
        visited = [0]*(n+1)
        r = dfs(i, graph, visited)
        win_ranks[i] = r
    for i in range(n+1):
        visited = [0]*(n+1)
        r = dfs(i, r_graph, visited) -1
        lose_ranks[i] = r
    for i in range(n+1):
        if win_ranks[i]+lose_ranks[i] == n: answer += 1
    return answer

