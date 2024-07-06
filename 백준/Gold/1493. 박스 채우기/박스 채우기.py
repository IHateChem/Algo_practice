import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
L,W,H =map(int,input().split())
N = int(input())
cubes = [list(map(int,input().split())) for _ in range(N)]
tot = 0
left_cube = N
for i in range(N):
    cubes[i][0] = 2**cubes[i][0]
    tot += cubes[i][1]
def sol(l,w,h):
    if not l or not w or not h: return True
    global left_cube
    m = min(l,w,h)
    if left_cube == 1:
        for i in range(N):
            if cubes[i][1]: break
        c = cubes[i][0]
        v = cubes[i][1]
        if c > m or not l // c or not h // c or not w // c or v < (l//c)*(h//c)*(w//c): return False
        cubes[i][1] -= (l//c)*(h//c)*(w//c)
        return True
        
    for i in range(N):
        cube = cubes[N-1-i]
        if not cube[1]: continue
        if cube[0] <= m: break
    else:
        return False
    
    c, v = cube
    if v >= (l//c)*(h//c)*(w//c):
        cl = l//c * c
        ch = h//c * c
        cw = w//c * c
        cube[1] -= (l//c)*(h//c)*(w//c)
    else:
        cl = c
        ch = c
        cw = c
        cube[1] -= 1
    if not cube[1]:
        left_cube -= 1
    if not (sol(cl,w-cw,ch) and sol(l-cl, w, ch) and sol(l,w,h-ch)): return False
    return True
if sol(L,W,H):
    answer = sum(map(lambda t: t[1], cubes))
else:
    answer = tot + 1
print(tot -answer)