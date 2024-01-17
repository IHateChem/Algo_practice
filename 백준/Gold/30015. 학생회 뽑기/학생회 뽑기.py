N,K = map(int,input().split())
powerOftwo = [2**i for i in range(19,-1,-1)]
classified = [[] for _ in range(20)]
A = list(map(int,input().split()))
s = 0
def chooseMember(A):
    classified = [[] for _ in range(20)]
    global s
    for a in A:
        for i in range(s, 20):
            a -= powerOftwo[i]
            if a >= 0:
                classified[i].append(a)
                if a == 0: break
            else:
                a += powerOftwo[i]
    for i in range(s, 20):
        if len(classified[i]) >= K:
            s = i
            return (2**(19-i), classified[i])
    return -1, -1
answer = 0
while 1:
    a, b = chooseMember(A)
    if a == -1: break
    answer += a
    A = b
print(answer)