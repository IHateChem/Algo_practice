import sys
from collections import defaultdict as dd
sys.setrecursionlimit(10000)
def find(parent, x):
    if not parent[x]:
        parent[x] = x+1
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]
def solution(k, room_number):
    parent = dd(int)
    answer = [find(parent, room) for room in room_number]
    return answer