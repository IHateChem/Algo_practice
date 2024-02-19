import sys
input = sys.stdin.readline
cities = [[] for _ in range(10001)]
s = 0
while 1:
    try:
        a,b,c = map(int,input().split())
        cities[a].append((b, c))
        cities[b].append((a, c))
        s = a
    except:
        break
def findMax(n):
    visited = set([n])
    s = [(n, 0)]
    ret = 0
    lastNode = 0
    while s:
        u, t = s.pop()
        if t > ret:
            ret = t
            lastNode = u
        for v, w in cities[u]:
            if v in visited: continue
            visited.add(v)
            s.append((v, t + w))
    return ret, lastNode
ret, n = findMax(s)
ret, n = findMax(n)
print(ret)