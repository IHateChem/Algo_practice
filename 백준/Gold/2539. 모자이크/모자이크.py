import sys
input=sys.stdin.readline
r,c=map(int,input().split())
n=int(input())
e=int(input())
papers=[]
for _ in range(e):
    papers.append(tuple(map(int,input().split())))
papers.sort(key=lambda t: t[1])

l=max([t[0] for t in papers]);r=c;answer=0
while l+1<r:
    answer=0
    m=(l+r)//2
    x=0
    for a,b in papers:
        if b>=x:
            x = b+ m
            answer+=1
    if answer <= n:
        r = m
    else:
        l = m
x=0;answer=0
for a,b in papers:
    if b>=x:
        x = b+ l
        answer+=1
if answer <= n: r = l
print(r)