import sys
from collections import deque
input=sys.stdin.readline
left = list(input().strip())
right = deque()
N=int(input())
for _ in range(N):
    command = input().strip().split()
    if command[0] == "P":
        left.append(command[1])
    elif command[0] == "L":
        if left:
            right.appendleft(left.pop())
    elif command[0] == "D":
        if right:
            left.append(right.popleft())
    elif command[0] == "B":
        if left:
            left.pop()
answer = "".join(left) + "".join(right)
print(answer)