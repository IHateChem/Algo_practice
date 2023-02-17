N=int(input())
ints=list(map(int,input().split()))
v=int(input())
answer=0
for i in ints:
    if v== i: answer += 1
print(answer)