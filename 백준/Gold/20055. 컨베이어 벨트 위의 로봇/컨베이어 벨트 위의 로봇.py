import sys
input=sys.stdin.readline
n,k=map(int,input().split())
belt=[[i,0] for i in map(int,input().split())]
up=0;down=n-1;answer=0
def check(A):
    flag=0
    for i in A:
        if i[0] == 0: flag += 1
    return flag < k
next = lambda t : (t-1) %(2*n)
n2 = 2*n
while check(belt):
    up =next(up)
    down = next(down)
    belt[down][1] = 0
    for i in range(n-1):
        t = (down-1-i) % n2
        if not belt[t][1] or not belt[(t+1)%n2][0] or belt[(t+1)%n2][1]: continue
        belt[(t+1)%n2][0] -= 1
        belt[(t+1)%n2][1] = 1
        belt[t][1] = 0
    belt[down][1] = 0
    if belt[up][0]:
        belt[up][0]-=1
        belt[up][1] = 1
    answer += 1
print(answer)