import sys
from itertools import combinations as C
input = sys.stdin.readline
N=int(input())
mp,mf,ms,mv = map(int,input().split())
foods = [list(map(int,input().split())) for _ in range(N)]
answer = 10000000000000000000
answerList = []
def cal(selection):
    for i in range(4): t[i] += selection[i]
def judge(t):
    return t[0] >= mp and t[1] >= mf and t[2] >= ms and t[3] >= mv
total = []
for i in range(N):
    total.extend(C(range(N), i+1))
for selections in sorted(total):
    t = [0,0,0,0]
    tPrice = 0
    for select in selections:
        select = select
        cal(foods[select])
        tPrice += foods[select][4]
    if judge(t) and answer > tPrice:
        answer = tPrice
        answerList = selections
print(answer if answer != 10000000000000000000 else -1)
if(answerList):print(*map(lambda t: t+1, answerList))