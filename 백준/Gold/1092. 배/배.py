import sys
input = sys.stdin.readline
n = int(input())
crane = sorted(list(map(int,input().split())))
m = int(input())
boxes = sorted(list(map(int,input().split())))
answer=  0
while boxes:
    t = []
    l = len(boxes)
    idx = 0
    for i in range(n):
        if not boxes: break
        while idx < len(boxes):
            if crane[-1-i] >= boxes[-1-idx]:
                del boxes[-1-idx]
                break
            idx += 1
    if l == len(boxes):
        print(-1)
        exit(0)
    answer += 1
print(answer)