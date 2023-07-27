MAP = [list(map(int, input().split())) for _ in range(3)]
ANSWER = sum([(i+1)*(9**i) for i in range(8)])
visited = set()
def Map2Num(M):
    ret = 0
    for i in range(9):
        ret += M[i//3][i%3] * (9**i)
    return ret
def Num2Map(N):
    M = [[0]*3 for _ in range(3)]
    for i in range(9):
        M[i//3][i%3] = N % 9
        N //= 9
    return M
def getNext(M):
    for i in range(9):
        if(M[i//3][i%3]): continue
        x, y = i//3 , i%3
    ret = []
    for dx, dy in ((0,1), (0,-1), (-1,0), (1,0)):
        if 0<=x+dx<3 and 0<=y+dy<3:
            M[x+dx][y+dy], M[x][y] = M[x][y], M[x+dx][y+dy]
            ret.append(Map2Num(M))
            M[x+dx][y+dy], M[x][y] = M[x][y], M[x+dx][y+dy]
    return ret
q = [Map2Num(MAP)]
visited.add(q[0])
ans = 0; t= []
while q:
    n = q.pop()
    if n == ANSWER: break
    M = Num2Map(n)
    possible_next = getNext(M)
    for p in possible_next:
        if p in visited: continue
        visited.add(p)
        t.append(p)
    if not q:
        ans += 1
        q = t
        t = []
else:
    ans = -1
print(ans)