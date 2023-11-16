from itertools import combinations as C
from collections import defaultdict as dd
import heapq
def solution(orders, course):
    answer = []
    for c in course:
        t = dd(int)
        for order in orders:
            order = sorted(list(order))
            for menus in C(order, c):
                t[menus] += 1
        t = sorted(list(t.items()), key = lambda t: t[1])
        if t and t[-1][1] > 1:
            largest = t[-1][1]
            while t and t[-1][1] == largest:
                answer.append("".join(t.pop()[0]))
    answer.sort()
    return answer