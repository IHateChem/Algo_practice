import sys
import math
import heapq
from collections import defaultdict as dd
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    size = 0
    min_pri = []
    max_pri = []
    history = dd(int)
    for __ in range(k):
        oper, num = input().rstrip().split()
        num = int(num)
        if oper == 'I':
            heapq.heappush(min_pri, num)
            heapq.heappush(max_pri, -1*num)
            history[num] += 1
            size += 1
        elif oper == "D":
            if size == 0: continue
            if num == 1:
                n = heapq.heappop(max_pri)
                while not history[-1*n]:
                    n = heapq.heappop(max_pri)
                history[-1*n] -= 1
                size -= 1
            else:
                n = heapq.heappop(min_pri)
                while not history[n]:
                    n = heapq.heappop(min_pri)
                history[n] -= 1
                size -= 1
    if size:
        n = heapq.heappop(max_pri)
        while not history[-1*n]:
            n = heapq.heappop(max_pri)
        max_v = n
        n = heapq.heappop(min_pri)
        while not history[n]:
            n = heapq.heappop(min_pri)
        min_v = n
        print(-1*max_v, min_v)
    else:
        print("EMPTY")