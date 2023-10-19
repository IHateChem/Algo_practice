import sys
input=sys.stdin.readline
N,K=map(int,input().split())
pool=list(map(int,input().split()))
i=1
answer=0
visited = set(pool)
t=[]
num=0
while pool:
    p = pool.pop()
    for j in [-1,1]:
        n = p + j
        if n in visited: continue
        visited.add(n)
        t.append(n)
        answer+=i
        num += 1
        if num == K:
            print(answer)
            exit(0)
    if not pool:
        pool = t
        t = []
        i += 1
print(answer)
    
