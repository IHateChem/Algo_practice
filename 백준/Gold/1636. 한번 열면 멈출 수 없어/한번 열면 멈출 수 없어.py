import sys
input=sys.stdin.readline
N=int(input())
answer=10100000100000000
stressList = [list(map(int,input().split()))for _ in range(N)]
answerList = []
for p in range(stressList[0][0], stressList[0][1]+1):
    t = 0
    tList = [p]
    for i in range(1,N):
        s,e = stressList[i]
        if p in range(s,e+1):
            pass
        elif abs(s-p) < abs(e-p):
            t += abs(s-p)
            p = s
        else:
            t += abs(e-p)
            p = e
        tList.append(p)
    if t < answer:
        answerList = tList
        answer = t
print(answer)
print("\n".join(map(str,answerList)))