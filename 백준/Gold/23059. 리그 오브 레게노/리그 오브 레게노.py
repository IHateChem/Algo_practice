import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
item2idx = {};idx2item = {}; idx = 1
def getidx(word):
    global idx
    if not item2idx.get(word): 
        item2idx[word] = idx
        idx2item[idx] = word
        idx += 1
    return item2idx[word]
indegree = [0]*(2*N+1)
graph = [[] for _  in range(2*N+1)]
for _ in range(N):
    a, b = map(getidx, input().strip().split())
    indegree[b] += 1
    graph[a].append(b)
q = []; done = set(); t = []
for i in range(1,idx):
    if indegree[i]: continue
    q.append(i)
    done.add(i)
answer = []; q.sort(reverse=True, key =lambda t: idx2item[t])  
while q:
    u = q.pop()
    answer.append(idx2item[u])
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v]: continue
        t.append(v)
        done.add(v)
    if not q:
        t.sort(reverse=True, key =lambda t: idx2item[t])  
        q = t
        t = []
if done != set(range(1,idx)):
    print(-1)
else:
    print("\n".join(answer))