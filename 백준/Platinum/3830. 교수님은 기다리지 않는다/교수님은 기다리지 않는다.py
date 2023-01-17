import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def find(mass, parent, x):
    if parent[x] == x:
        return x
    t = find(mass, parent, parent[x])
    mass[x] += mass[parent[x]]
    parent[x] = t
    return t
def union(mass, parent, a, b, c):
    root_a = find(mass, parent, a)
    root_b = find(mass, parent, b)
    parent[root_b] = root_a
    mass[root_b] = mass[a] - mass[b] + c
while 1:
    N, M = map(int, input().split())
    if N == 0 and  M == 0: break
    parent = [i for i in range(N+1)]
    mass = [0]*(N+1)
    for i in range(M):
        order = input().strip().split()
        if order[0] == "!":
            a,b,c = map(int, order[1:])
            union(mass, parent, a,b,c)
        else:
            a, b =  map(int, order[1:])
            r_a = find(mass, parent, a)
            r_b = find(mass, parent, b)
            if r_a != r_b: print("UNKNOWN")
            else: print(mass[b] - mass[a])