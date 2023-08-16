import sys
input=sys.stdin.readline
N,T=map(int,input().split())
times = [0]*100002
for _ in range(N): 
    K = int(input())
    for i in range(K):
        s,e = map(int,input().split())
        times[s] += 1
        times[e] -= 1
window = 0;answerTime=T-1
for i in range(T):
    times[i+1] += times[i]
    window+= times[i]
answer = window
for i in range(T, 100001):
    times[i+1] += times[i]
    window += times[i] - times[i-T]
    if window > answer:
        answer = window
        answerTime = i
print(answerTime-T+1,answerTime+1)