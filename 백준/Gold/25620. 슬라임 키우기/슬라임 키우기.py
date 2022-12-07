import sys
from collections import defaultdict as dd
import heapq
N, M = list(map(int, sys.stdin.readline().rstrip().split()))
data = list(map(int, sys.stdin.readline().rstrip().split()))
da = dd(int)
for d in data:
    if da[d]:
        da[d] += 1
    else:
        da[d] = 1
data = []
for k, v in da.items():
    data.append([k, v])
overdata = []
heapq.heapify(data)
for i in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if data and y != 1:
        mindata = heapq.heappop(data)
        templist = []
        while mindata[0] <= x and data:
            templist.append([mindata[0]*y, mindata[1]])
            mindata = heapq.heappop(data)
        templist.append( [mindata[0] * y, mindata[1]] if mindata[0] <= x else [mindata[0], mindata[1]])
        for temp in sorted(templist):
            if temp[0] == 0:
                overdata.append(temp)
            elif temp[0] > 10**9:
                overdata.append(temp)
            else:
                heapq.heappush(data, temp)
data += overdata
overdata = []
for dat in data:
    k = dat[0]
    v = dat[1]
    for i in range(v):
        overdata.append(k)
overdata.sort()
print(" ".join(list(map(str,overdata))))
