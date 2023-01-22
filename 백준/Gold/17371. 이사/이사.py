import sys
input = sys.stdin.readline
def distance(x, y):return (x[0]-y[0])**2+(x[1]-y[1])**2
N = int(input())
MAP = []
_min = 1e10
for _ in range(N):MAP.append(tuple(map(int, input().split())))
for i in range(N):
    a, b = MAP[i]
    _max = -1
    for pos in MAP:
        temp_dis = distance(pos, (a, b))
        if temp_dis > _max:
            _max = temp_dis
    if _max < _min:
        min_pos = (a,b)
        _min = _max
    MAP.append((a,b))
print(min_pos[0], min_pos[1])