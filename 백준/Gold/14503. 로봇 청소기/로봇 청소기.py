import sys
def clean(x, y , m):
	if m[x][y]:
		return 0 
	m[x][y] = 2
	return 1
def getNextPosition(x, y , dir):
	dx, dy = dxdy[dir]
	if Map[x+dx][y+dy]:
		return -1, -1
	return x+dx, y+dy
input = sys.stdin.readline
N, M = map(int, input().strip().split())
x, y, dir = map(int, input().strip().split())
dxdy = [(0,-1), (-1, 0), (0, 1), (1, 0)]
backdxdy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
Map = []
for i in range(N):
	Map.append(list(map(int,input().strip().split())))
answer = 0
f = True
while True:
	if f: answer += clean(x, y, Map)
	for i in range(4):
		tx, ty = getNextPosition(x, y , (dir-i)%4)
		if tx >= 0:
			dir = (dir-i-1)%4
			x = tx
			y = ty
			f = True
			break
	else: 
		f = False
		tdx , tdy = backdxdy[dir]
		x = x+ tdx
		y = y+ tdy			
		if Map[x][y] == 1:
			break
print(answer)