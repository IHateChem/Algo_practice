import sys
from collections import defaultdict as dd
input=sys.stdin.readline
n=int(input())
def union(a, b):
    parentA = find(a)
    parentB = find(b)
    groupSize[parentA] += groupSize[parentB]
    parent[parentB] = parentA
def find(a):
    if a != parent[a]:
        parentA = find(parent[a])
        parent[a] = parentA
    return parent[a]
for _ in range(n):
    F=int(input())
    parent=[i for i in range(F*3)]
    groupSize=[1 for i in range(F*3)]
    id = dd(int); num=1
    for i in range(F):
        A,B=input().strip().split()
        if not id[A]:
            id[A] = num
            num+= 1
        if not id[B]:
            id[B] = num
            num+= 1
        if(find(id[A]) != find(id[B])): union(id[A],id[B])
        print(groupSize[find(id[A])])