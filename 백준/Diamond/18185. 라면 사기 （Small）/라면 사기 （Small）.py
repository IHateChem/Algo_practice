import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
answer=0
for i in range(N-2):
    if not A[i]: continue
    if A[i+1] > A[i+2]:
        if A[i] > A[i+1]:
            answer += 7 * A[i+2]
            answer += 3 * (A[i] - A[i+1])
            answer += 5 * (A[i+1]-A[i+2])
            A[i] =0; A[i+1] =0; A[i+2] =0
        else:
            if A[i] < A[i+1] - A[i+2]:
                answer += A[i] * 5
                A[i+1] -=A[i]
                A[i] = 0
            else:
                answer += 5 * (A[i+1] -A[i+2])
                t =  min(A[i]-(A[i+1]-A[i+2]), A[i+2])
                answer += 7 * t
                A[i] -= t  + (A[i+1] -A[i+2])
                A[i+1] -= t + (A[i+1] -A[i+2])
                A[i+2] -= t
                if A[i]: answer += 3*A[i]; A[i] = 0
    else:
        t = min(A[i], A[i+1], A[i+2])
        A[i] -= t;A[i+1]-=t;A[i+2]-=t
        answer += 7*t
        if A[i]:
            answer += 3*A[i]
            A[i] = 0
if A[-2]:
    t = min(A[-2], A[-1])
    answer += 5*t
    if A[-2] != A[-1]:
        answer += 3*abs(A[-1]-A[-2])
elif A[-1]:
    answer += 3*A[-1]
print(answer)