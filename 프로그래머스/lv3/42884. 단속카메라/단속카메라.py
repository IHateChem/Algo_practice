import heapq
from bisect import bisect_right
def solution(routes):
    _min = 300001
    _max = -300001
    for r in routes: r.sort()
    for start, end in routes:
        _min = min(_min, start)
        _max = max(_max, end)
    new_routes = [(i[0] - _min, i[1]-_min) for i in routes]
    road = [0] * (_max - _min+2)
    stack = []
    for start, end in new_routes:
        road[start] += 1
        road[end+1] -= 1
        heapq.heappush(stack, (end, start))
    p = 0
    for i in range(len(road)):
        road[i] += p
        p = road[i]
    p = -1
    answer = 0
    while stack:
        e, s = heapq.heappop(stack)
        if s <= p and e >= p: continue
        answer += 1
        t = max(road[s:e+1])
        t_i = bisect_right(road[s:e+1],t)
        p = s+t_i-1
        print(p)
    return answer