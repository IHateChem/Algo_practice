import sys
import bisect
input = sys.stdin.readline
N = int(input())
papers = []
for _ in " "*N:
    u, v = map(int, input().split())
    if u > v:
        papers.append((v, u))
    else:
        papers.append((u, v))
papers.sort()
where = [papers[0][1]]
for paper in papers[1:]:
    u, v = paper[0],paper[1]
    if v >= where[-1]:
        where.append(v)
    else:
        id = bisect.bisect_right(where, v)
        where[id] = v
print(len(where))