import sys
input = sys.stdin.readline
N, L = map(int,input().split())
graph = [set() for _ in range(L)] #각 노선이 환승 할 수 있는 노선
stations = [set() for _ in range(N+1)] #각 역이 가지는 노선
lines = [set() for _ in range(L)] #각 노선이 가지는 역들
for i in range(L):
    inputs = map(int,input().split())
    for station in inputs:
        if station == -1: break
        stations[station].add(i)
        lines[i].add(station)
s,e = map(int,input().split())
q = [s]
visited_s = set([s])
visited_l = set()
t = []
ans = -1 if s != e else 0
while q:
    station = q.pop()
    if station == e: break
    next_lines = stations[station]
    for next_line in next_lines:
        if next_line in visited_l: continue
        visited_l.add(next_line)
        for s in lines[next_line]:
            if s in visited_s: continue
            visited_s.add(s)
            t.append(s)
    if not q:
        q = t
        t = []
        ans += 1
else:
    ans = -1
print(ans)