N = int(input())
A = list(map(int,input().split()))
answer = 0
goodNumbers = [set(), set()]
before = []
inbound = lambda t: -100000<=t<=100000
for a in A:
    for b in before:
        if a - b in goodNumbers[1]:
            answer += 1
            break
    addNumbers = [a,a*2]
    nextGoods = [set([a]), set([a*2])]
    for j in goodNumbers[0]:
        if inbound(j+a):
            nextGoods[1].add(j+a)
    for i in range(2):
        goodNumbers[i] |= nextGoods[i]
    before.append(a)
print(answer)