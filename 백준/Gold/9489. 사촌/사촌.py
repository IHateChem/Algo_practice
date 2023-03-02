import sys
from bisect import bisect_left as bl
input = sys.stdin.readline
while 1:
    n, k=map(int, input().split())
    if not (n or k): break
    numbers=list(map(int,input().split()))
    idx = bl(numbers, k)
    p = -1
    past = numbers[0]-1
    parents = [-1 for i in numbers]
    childs = [[] for i in numbers]
    for i, num in enumerate(numbers[1:]):
        if num - past != 1:
            p += 1
        parents[i+1] = p
        childs[p].append(i+1)
        past = num
    idxsparent = parents[idx]
    idxsgrand = parents[idxsparent]
    answer = 0
    if idxsparent != -1 and idxsgrand != -1: 
        unkles = childs[idxsgrand]
        for pc in unkles:
            if pc != idxsparent:
                answer += len(childs[pc])
    print(answer)