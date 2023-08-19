import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
busPath = [(*tuple(map(int,input().split())),i+1) for i in range(M)]
normLine = [i for i in busPath if i[0]<i[1]]
revLine = [(i[0], i[1]+N , i[2]) for i in busPath if i[0]>i[1]]
normLine2 = [(i[0]+N, i[1]+N , i[2]) for i in busPath if i[0]<i[1]]
Line = normLine + normLine2 + revLine
Line.sort(key=lambda t: (t[0], -1*t[1]))
answer = set(range(1,M+1))
idx = 0
for s, e, n in Line:
    if e > idx:
        idx = e
        revLine.append((s+N,e+N,n))
    else:
        if n in answer:
            answer.discard(n)
        continue
print(*answer)  