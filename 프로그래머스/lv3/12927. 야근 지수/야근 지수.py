import heapq
def solution(n, works):
    n_works = [-1*w for w in works]
    heapq.heapify(n_works)
    i = 0
    while n_works and i < n:
        work = heapq.heappop(n_works) + 1
        if work:
            heapq.heappush(n_works, work)
        i += 1
    answer = 0
    for w in n_works:
        answer += w*w
    return answer