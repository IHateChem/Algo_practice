import sys
import heapq
INF = int(2*10**15+3)
N, M = list(map(int, sys.stdin.readline().rstrip().split()))
graph = [[] for _ in range(N+1)]
negative = []

for i in range(M):
	a, b,c,d = list(map(int, sys.stdin.readline().rstrip().split()))
	if c+d < 0:
		if a == 1:
			negative.append(b)
		else:
			negative.append(a)
	graph[a].append(((c+d)/2,b))    
	graph[b].append(((c+d)/2,a))
k = int(sys.stdin.readline().rstrip())

#if ne..
isnegative = False
if negative:
	#DFS
	nodes = []
	visited = [0]*(N+1)
	visited[1] = 1
	stack = [1]
	while stack:
		u = stack.pop()
		for w, v in graph[u]:
			if not visited[v]:
				visited[v] = 1
				stack.append(v)
				nodes.append(v)
	for neg in negative:
		if neg in nodes:
			isnegative = True
			break
if isnegative:
	nodes.sort()
	print(len(nodes))
	print(" ".join(list(map(str, nodes))))
else:
	#dijk
	distance = [INF]*(N+1)
	distance[1] = 0
	stack = [(0, 1)]
	visited = [0]*(N+1)
	while stack:
		w, u = heapq.heappop(stack)
		if visited[u]:
			continue
		visited[u] = 1
		for w, v in graph[u]:
			if not visited[v]:
				if distance[u] + w < distance[v]:
					distance[v] = distance[u] + w 
					heapq.heappush(stack, (distance[u] + w , v))
	ans = []
	for i, d in enumerate(distance[2:]):
		if d <= k:
			ans.append(str(i+2))
	print(len(ans))
	if ans: 
		print(" ".join(ans))