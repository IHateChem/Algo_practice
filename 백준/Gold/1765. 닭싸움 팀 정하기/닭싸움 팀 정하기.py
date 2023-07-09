import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
parent=list(range(n+1))
enemies=[set()for i in range(n+1)]
def union(x, y):
    px = find(x)
    py = find(y)
    parent[px] = py
def find(x):
    if parent[x] == x: return x
    px = find(parent[x])
    parent[x] = px
    return px
for _ in range(m):
    R,p,q=input().strip().split()
    p,q=int(p),int(q)
    if R=="E":
        p_enemies = enemies[p]
        q_enemies = enemies[q]
        for p_enemy in p_enemies:
            union(p_enemy, q)
        for q_enemy in q_enemies:
            union(q_enemy, p)
        enemies[p].add(q)
        enemies[q].add(p)
    elif R == "F":
        union(p,q)
answer = set()
for t in parent:
    answer.add(find(t))
print(len(answer)-1)