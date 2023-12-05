import sys
from collections import defaultdict as dd
input=sys.stdin.readline
MAP=[list(input().strip()) for _ in range(4)]
input()
NMAP = [list(input().strip()) for _ in range(4)]

def map2bit(m):
    bit = 0
    for i in range(4):
        for j in range(4):
            if m[i][j] == "L":
                bit += 2**(4*i+j)
    return bit

bitMap = map2bit(MAP)
destbit = map2bit(NMAP)

stack = [bitMap]
visited = set([bitMap])
answer= 0
t = []
while stack:
    bit = stack.pop()
    if bit == destbit: break
    for i in range(15):
        if (i+1) % 4 == 0: continue
        if bit & 2**i != bit & 2**(i+1):
            tempBit = bit ^(2**i+2**(i+1))
            if tempBit not in visited:
                visited.add(tempBit)
                t.append(tempBit)    
    for i in range(12):
        if bit & 2**i != bit & 2**(i+4):
            tempBit = bit ^(2**i+2**(i+4))
            if tempBit not in visited:
                visited.add(tempBit)
                t.append(tempBit)
    if not stack:
        answer += 1
        stack = t
        t = []
print(answer)   