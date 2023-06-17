#완전탐색
def solution(n, info):
    answer = [-1]
    maxDiff = 0
    score = range(10,-1,-1)
    possible = []
    for i in info:
        possible.append((i+1,0))
    stack = [(0,0, [])] #화살 쏜 개수, 점수차, 기록
    t = []
    for i in range(10,-1,-1):
        for num, scoreDiff, record in stack:
            for p in possible[i]:
                if num + p >n: continue
                t.append((num+p, scoreDiff + score[i] * (1 if p > info[i] else -1) *(1 if info[i] or p else 0), [r for r in record]+[p]))
        stack = t
        t = []
    for i, d, r in stack:
        if d > maxDiff:
            answer=  r
            maxDiff = d
    answer.reverse()
    if sum(answer) != -1 and sum(answer) < n:
        d = n- sum(answer)
        answer[-1] += d
    return answer