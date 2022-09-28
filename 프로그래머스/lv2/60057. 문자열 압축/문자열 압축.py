import math
def solution(s):
    n = len(s)
    answer = n
    eps = 10**-10
    k = 1
    while k <= n //2:
        tempanswer = n
        pnt = 0
        tsh = 10
        succ = 0
        while pnt + 2*k <= n:
            if s[pnt:pnt+k] == s[pnt+k:pnt+2*k]:
                if succ:
                    tempanswer -= k
                else:
                    tempanswer -= k- 1
                succ += 1
                if succ == tsh-1:
                    tempanswer += 1
                    tsh *= 10
            else:
                succ = 0
                tsh = 10
            pnt += k 
        answer = min(answer, tempanswer)
        k += 1
    return answer