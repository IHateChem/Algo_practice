import sys
input = sys.stdin.readline
exp = input().rstrip()
alpha = set([chr(65+i) for i in range(26)])
oper = set([ "+", "-","*", "/"])
plus_minus = set([ "+", "-"])
prod_div = set(["*", "/"])
stack = []
answer =  []
for c in exp:
    if c in alpha:
        answer.append(c)
    elif c == "(":
        stack.append(c)
    elif c == ")":
        while stack[-1] != "(":
            answer.append(stack.pop())
        stack.pop()
    elif c in prod_div:
        if stack and stack[-1] in prod_div:
            answer.append(stack.pop())
        stack.append(c)
    elif c in plus_minus:
        while stack and stack[-1] != "(":
            answer.append(stack.pop())
        stack.append(c)
while stack:
    answer.append(stack.pop())
print("".join(answer))