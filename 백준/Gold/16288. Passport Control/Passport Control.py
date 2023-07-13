#최장 증가하는 부분순열 K개가 나오면됨. 
from collections import defaultdict as dd
from bisect import bisect_left as bs
N,K=map(int,input().split())
enterance_seq = range(1,N+1)
left = set(range(N))
seqeuences = list(map(int,input().split()))
num2seq = {j:i for i, j in enumerate(seqeuences)}
for _ in range(K):
    prior = [-1]*(N+1)
    D=[]
    for i in left:
        a = seqeuences[i]
        if not D:
            D.append(a)
        elif D[-1] < a:
            D.append(a)
            prior[D[-1]] = D[-2]
        else:
            idx= bs(D, a)
            D[idx] = a
            prior[a] = D[idx-1]
    if D:
        p = D[-1]
    else: break
    lis = set()
    for j in range(len(D)):
        lis.add(num2seq[p])
        p = prior[p]
    left -= lis
if left: print("NO")
else: print("YES")
