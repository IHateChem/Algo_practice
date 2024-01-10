import sys
input = sys.stdin.readline
N,B,W = map(int,input().split())
pebbles = input().strip()
l, r, ans, black, white = 0, 0, 0, pebbles[0]=="B", pebbles[0]=="W"
if black <= B and white >=W:
    ans = max(ans, r-l+1)
while r < len(pebbles)-1:
    if black > B:
        if pebbles[l] == "W":
            white -= 1
        else:
            black -= 1
        l += 1
    else:
        r += 1
        if pebbles[r] == "W":
            white += 1
        else:
            black += 1
    if black <= B and white >=W:
        ans = max(ans, r-l+1)
print(ans)
