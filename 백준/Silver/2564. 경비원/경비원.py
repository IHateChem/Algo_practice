import sys
import copy
input = sys.stdin.readline
W, H = map(int, input().split())
N = int(input())
position = []
change = [0, 1, 3, 2, 4] #편의상 북:1, 서:2 남:3 동:4로 바꾸기
witdhorheight = [0,W,H,W,H]
reverse = [0,H,W,H,W]
for _ in range(N):
    a, b = map(int, input().split())
    position.append((change[a],b))
x , y = map(int, input().split())
x = change[x]
answer = 0
def ccw(a, b, x, y):
    if x == 2:
        return y +b
    elif x == 3:
        return y +witdhorheight[a] - b
    elif x == 4:
        return witdhorheight[a] - b +witdhorheight[x] - y
    else:
        return b +witdhorheight[x] - y
def cw(a,b,x,y):
    if x == 2:
        return b +witdhorheight[x] - y
    elif x == 3:
        return witdhorheight[a] - b +witdhorheight[x] - y
    elif x == 4:
        return y +witdhorheight[a] - b
    else:
        return y +b

for a, b in position:
    if (x-a) % 4 == 1:
        answer += ccw(a, b, x, y)
    elif (x-a) % 4 == 3:
        answer += cw(a, b, x, y)
    elif (x-a)==0:
        answer += abs(y-b)
    else:
        answer += reverse[a] + min(b+y, witdhorheight[a] - b +witdhorheight[x] - y)
print(answer)