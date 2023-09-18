import sys
#콜라 30개 이상 중첩되면 무조건 0
input=sys.stdin.readline
N,K,L=map(int,input().split())
m=list(map(int,input().split()))
t=list(map(int,input().split()))
cola = [0]*N
for i in range(K):
    cola[t[i]-1] += 1
    if t[i]-1 +L< N:
        cola[t[i]-1 +L] -= 1
p=0
for i in range(N):
   cola[i] += p
   p = cola[i] 
power=[]
for i in range(200001):
    if i < 32: M=2**i
    power.append(M)
cola.sort()
m.sort()
answer =0
import math
for i in range(N):
    answer += m[i] // power[cola[i]]
print(answer)