import sys
input=sys.stdin.readline
N,M=map(int,input().split())
marbles=[list(map(int,input().split())) for _ in range(N)]
magics=[tuple(map(int,input().split())) for _ in range(M)]
directions={1:(-1,0), 2:(1,0), 3:(0,-1), 4:(0,1)}
marbleOrder=[3,2,4,1]
explosion = {1:0,2:0,3:0}
distance=[i//2 for i in range(2, 3+4*(N//2))]
distance[-1] -= 1
pos2idx = {}
l = []
x=N//2;y=N//2;i=0;dir=0
for n in distance:
    dx, dy = directions[marbleOrder[dir]]   
    for j in range(n):
        x += dx; y += dy
        pos2idx[(x, y)] = i
        if marbles[x][y]:
            l.append(marbles[x][y])
        i += 1
    dir = (dir + 1) % 4
X=N//2;Y=N//2
def bomb(l):
    if not l: return l
    p = l[0]; t = []; destroy = set()
    l.append(-1)
    flag = False
    for i in range(len(l)):
        if p == l[i]:
            t.append(i)
        else:
            if len(t) > 3:
                flag=True
                explosion[p] += len(t)
                for j in t:
                    destroy.add(j)
            t = [i]; p = l[i]
    l.pop()
    newL = []
    for i in range(len(l)):
        if i in destroy: continue
        newL.append(l[i])
    if flag: newL = bomb(newL)
    return newL
for d, s in magics:
    if not l: break
    destroy = set()
    dx, dy = directions[d]
    for i in range(s):
        destroy.add(pos2idx[(X+dx*(i+1), Y+dy*(i+1))])
    newL = []
    for i in range(len(l)):
        if i in destroy: continue
        newL.append(l[i])
    l = bomb(newL)
    if not l: break
    newL = []; t = []; p = l[0]
    l.append(-1)
    for i in range(len(l)):
        if p == l[i]:
            t.append(i)
        else:
            newL.append(len(t))
            newL.append(p)
            t = [i]; p = l[i]
    for i in range(len(newL) - N*N + 1):
        newL.pop()
    l = newL
print(explosion[1]+2*explosion[2]+3*explosion[3])