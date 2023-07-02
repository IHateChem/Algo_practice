import sys
input = sys.stdin.readline
n=int(input())
stack = [[int(input()), 1]]
for _ in range(n-1):
    next = int(input())
    if stack[-1][0] == next:
        stack[-1][1] += 1
    else:
        stack.append([next, 1])
N = len(stack)
def canPop(top, bottom, stack, th):
    return stack[top][0] == stack[bottom][0] and stack[top][1] + stack[bottom][1] > th
def howManyLeft(top, bottom):
    while top < N and bottom >= 0:
        if canPop(top, bottom, stack, 3):
            top += 1
            bottom -= 1
        else: break
    ret = 0
    while top < N:
        ret += stack[top][1]
        top += 1
    while bottom >= 0:
        ret += stack[bottom][1]
        bottom -= 1
    return ret
candidates = []
for i in range(len(stack)-1):
    if stack[i][1] == 1:
        if i > 0 and canPop(i+1,i-1, stack, 2):
            top = i + 2
            bottom = i-2
            candidates.append(howManyLeft(top, bottom))
    elif stack[i][1] == 3:
        if i > 0:
            if not (stack[i-1][1] == 1 and i > 2 and stack[i][0] == stack[i-2][0]):
                stack[i-1][1] -= 1
                top = i+1
                bottom = i-1 if stack[i-1][1] != 0 else i - 2
                candidates.append(howManyLeft(top, bottom))
                stack[i-1][1] += 1
        if i < N-1:
            if not (stack[i+1][1] == 1 and i < N-2 and stack[i][0] == stack[i+2][0]):
                stack[i+1][1] -= 1
                top = i+1 if stack[i-1][1] != 0 else i+2
                bottom = i-1 
                candidates.append(howManyLeft(top, bottom))
                stack[i+1][1] += 1
print(min(candidates) if candidates else n)