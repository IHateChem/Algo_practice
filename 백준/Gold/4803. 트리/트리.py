import sys
input=sys.stdin.readline
n,m=map(int, input().split())
def union(x,y):
    px=find(x)
    py=find(y)
    parent[py]=px
def find(x):
    if x == parent[x]: return x
    px=find(parent[x])
    parent[x] = px
    return px
num=1
while n or m:
    parent = list(range(n+1))
    for _ in range(m):
        u,v=map(int,input().split())
        if find(u) == find(v) or not find(u) or not find(v): parent[find(u)] = 0; parent[find(v)] = 0
        else: union(u,v)
    trees=set()
    for i in range(n+1):
        pi=find(i)
        if pi:trees.add(pi)
    print(f"Case {num}: ", end="")
    if len(trees) == 1:
        print("There is one tree.")
    elif len(trees):
        print(f"A forest of {len(trees)} trees.")
    else:
        print("No trees.")
    num+=1
    n,m=map(int, input().split())