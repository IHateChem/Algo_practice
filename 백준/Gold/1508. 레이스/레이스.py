import sys
input = sys.stdin.readline
N,M,K = map(int, input().split())
judges = list(map(int, input().split()))
l = 1
r = judges[-1] - judges[0]
while l < r:
    m = (l+r)//2
    if m == l: break
    p = judges[0]
    cnt = 1
    for j in judges[1:]:
        if j-p >= m:
            cnt += 1
            p = j
    if cnt >= M:
        l = m 
    else:
        r = m - 1
for m in (r, l):
    p = judges[0]
    cnt = 1
    answer = ["1"]
    for j in judges[1:]:
        if j-p >= m:
            cnt += 1
            p = j
            answer.append("1")
        else:
            answer.append('0')
    if cnt == M: break
else:
    p = judges[0]
    cnt = 1
    answer = ["1"]
    for j in judges[1:]:
        if cnt == M:
            answer.append("0")
            continue
        if j-p >= m:
            cnt += 1
            p = j
            answer.append("1")
        else:
            answer.append('0')
print("".join(answer))