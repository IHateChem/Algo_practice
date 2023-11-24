import sys
sys.setrecursionlimit(100000000)
def solution(k, num, links):
    answer = 0
    INF = 10000000000000000
    dp = [[0,INF] for _ in range(len(num))]
    dp.append([0,0])
    depth = [[] for _ in range(len(num))]
    top = set(range(-1,len(num)))
    num.append(0)
    for u,v in links:
        if u in top:
            top.remove(u)
        if v in top:
            top.remove(v)
    top = top.pop()
    def bfs(nodes, h):
        t = []
        depth[h] = nodes
        for node in nodes:
            u,v = links[node]
            if u != -1:
                t.append(u)
            if v != -1:
                t.append(v)
        if t: bfs(t, h+1)
    bfs([top], 0)
    while depth[-1] == []: depth.pop()
    l =  sum(num) // k - 1
    r = sum(num)
    while l < r:
        new_depth = [i for i in depth]
        m = (l+r)//2
        flag = False
        while new_depth:
            t = new_depth.pop()
            for node in t:
                u, v = links[node]
                if num[node] + dp[u][1] + dp[v][1] <= m:
                    dp[node][0] = dp[u][0] + dp[v][0]
                    dp[node][1] = dp[v][1] + dp[u][1] + num[node]
                elif num[node] + min(dp[u][1], dp[v][1]) <= m:
                    dp[node][0] = dp[u][0] +dp[v][0] + 1
                    dp[node][1] = min(dp[v][1], dp[u][1]) + num[node]
                elif num[node] <= m:
                    dp[node][0] = dp[u][0] +dp[v][0] + 2
                    dp[node][1] = num[node]
                else:
                    dp[node][0] = k
                #print("node: ", node, dp[node])                
        if dp[top][0] > k-1:
            l = m + 1
        else:
            r = m
        #print("m ",m, dp[top])
    return l