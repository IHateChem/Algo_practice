N=int(input())
workers = list(map(int, input().split()))
graph=[[]for _ in range(N)]
for i in range(1,N):
    graph[workers[i]].append(i)
visited = set()
def dfs(n):
    times = []
    for child in graph[n]:
        times.append(dfs(child))
    times.sort(reverse=True)
    time = 0
    for i in range(len(times)):
        time = max(time, times[i]+i +1)
    return time
print(dfs(0))