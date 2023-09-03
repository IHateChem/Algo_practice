import sys
input=sys.stdin.readline
N,B,C=map(int,input().split())
A=list(map(int,input().split()))
answer=0
if B<=C:
    print(sum(A)*B)
    exit(0)
for i in range(N-2):
    if not A[i]: continue
    if A[i+1] > A[i+2]:
        if A[i] > A[i+1]:
            answer += (B+2*C) * A[i+2]
            answer += B * (A[i] - A[i+1])
            answer += (B+C) * (A[i+1]-A[i+2])
            A[i] =0; A[i+1] =0; A[i+2] =0
        else:
            if A[i] < A[i+1] - A[i+2]:
                answer += A[i] * (B+C)
                A[i+1] -=A[i]
                A[i] = 0
            else:
                answer += (B+C) * (A[i+1] -A[i+2])
                t =  min(A[i]-(A[i+1]-A[i+2]), A[i+2])
                answer += (B+2*C) * t
                A[i] -= t  + (A[i+1] -A[i+2])
                A[i+1] -= t + (A[i+1] -A[i+2])
                A[i+2] -= t
                if A[i]: answer += B*A[i]; A[i] = 0
    else:
        t = min(A[i], A[i+1], A[i+2])
        A[i] -= t;A[i+1]-=t;A[i+2]-=t
        answer += (B+2*C)*t
        if A[i]:
            answer += B*A[i]
            A[i] = 0
if A[-2]:
    t = min(A[-2], A[-1])
    answer += (B+C)*t
    if A[-2] != A[-1]:
        answer += B*abs(A[-1]-A[-2])
elif A[-1]:
    answer += B*A[-1]
print(answer)