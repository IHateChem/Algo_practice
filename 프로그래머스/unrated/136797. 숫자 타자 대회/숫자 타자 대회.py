graph = {0: {7: 3, 8: 2, 9: 3, 5: 4, 4: 5, 6: 5, 2: 6, 1: 7, 3: 7, 0: 1}, 1: {2: 2, 4: 2, 5: 3, 3: 4, 7: 4, 6: 5, 8: 5, 9: 6, 0: 7, 1: 1}, 2: {1: 2, 3: 2, 5: 2, 4: 3, 6: 3, 8: 4, 7: 5, 9: 5, 0: 6, 2: 1}, 3: {2: 2, 6: 2, 5: 3, 1: 4, 9: 4, 4: 5, 8: 5, 7: 6, 0: 7, 3: 1}, 4: {1: 2, 5: 2, 7: 2, 2: 3, 8: 3, 6: 4, 0: 5, 3: 5, 9: 5, 4: 1}, 5: {2: 2, 4: 2, 6: 2, 8: 2, 1: 3, 3: 3, 7: 3, 9: 3, 0: 4, 5: 1}, 6: {3: 2, 5: 2, 9: 2, 2: 3, 8: 3, 4: 4, 0: 5, 1: 5, 7: 5, 6: 1}, 7: {4: 2, 8: 2, 5: 3, 0: 3, 1: 4, 9: 4, 2: 5, 6: 5, 3: 6, 7: 1}, 8: {5: 2, 7: 2, 9: 2, 4: 3, 6: 3, 0: 2, 2: 4, 1: 5, 3: 5, 8: 1}, 9: {6: 2, 8: 2, 5: 3, 0: 3, 3: 4, 7: 4, 2: 5, 4: 5, 1: 6, 9: 1}}
import heapq
from collections import defaultdict as dd
def solution(numbers):
    history = dd(int)
    stack = [(0,0,4,6)]
    numbers = list(map(int, numbers))
    N = len(numbers)
    while 1:
        tot, idx, l, r = heapq.heappop(stack)
        if idx == N: return tot
        n = numbers[idx]
        if r != n and idx  < N:
            if  (not history[(idx+1,n,r)] )or (history[(idx+1,n,r)] and  history[(idx+1,n,r)] > tot+graph[l][n]):
                history[(idx+1,n,r)] = tot+graph[l][n]
                heapq.heappush(stack, (tot+graph[l][n], idx+1, n, r))
        if l != n and idx < N:
            if (not history[(idx+1,l,n)]) or (history[(idx+1,l,n)] and history[(idx+1,l,n)] > tot+graph[r][n]):
                history[(idx+1,l,r)] = tot+graph[r][n]
                heapq.heappush(stack, (tot+graph[r][n], idx+1, l, n))
