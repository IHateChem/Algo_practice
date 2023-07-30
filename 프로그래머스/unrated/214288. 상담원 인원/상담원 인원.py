import heapq
from collections import defaultdict as dd
def solution(k, n, reqs):
    case = dd(list)
    for req in reqs:
        case[req[2]].append( (req[0], req[1]) ) 
    timePerType =  dd(list)
    for i in range(1, k+1):
        for t in range(n-k+1):
            finish = []
            wait = 0
            for a, b in case[i]:
                if len(finish) <= t:
                    heapq.heappush(finish, a+b)
                else:
                    fin = heapq.heappop(finish)
                    if fin > a:
                        wait += fin - a
                    fin = max(fin, a)
                    heapq.heappush(finish, fin+b)
            timePerType[i].append(wait)
    answer = find(timePerType, 1, n-k+1, k+1, 0, n-k)
    return answer
def find(dic, i, j, n, cnt, limit):
    if i == n: return 0
    answer = 10000000000000000000000
    for k in range(j):
        if cnt+k > limit: break
        answer = min(answer,dic[i][k]+ find(dic, i+1, j,n, cnt+k, limit))
    return answer