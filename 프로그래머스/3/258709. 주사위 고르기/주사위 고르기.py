from collections import defaultdict as dd
from itertools import combinations as C
def calc(A, B):
    p_a = {0:1}
    p_b = {0:1}
    ret = [0, 0, 0]
    for a in A:
        t = dd(int)
        for ka, va in a.items():
            for k, v in p_a.items():
                t[ka+k] += v*va
        p_a = t
    for b in B:
        t = dd(int)
        for ka, va in b.items():
            for k, v in p_b.items():
                t[ka+k] += v*va
        p_b = t
    for ka, va in p_a.items():
        for kb, vb in p_b.items():
            if ka == kb:
                ret[1] += va* vb
            elif ka > kb:
                ret[0] += va * vb
            else:
                ret[2] += va* vb
    return ret
        
    
        
def solution(dice):
    answer = []
    N = len(dice)
    t = []
    max_score = [0,0,0]
    for d in dice:
        t.append({d[i]: d.count(d[i]) for i in range(len(dice[0]))})
    dice = t
    for combination in C(range(N), N//2):
        A = []
        B = []
        for i in range(N):
            if i in combination: A.append(dice[i])
            else: B.append(dice[i])
        t = calc(A, B)
        if max_score < t:
            answer = list(combination)
            max_score = t
        
    return [a + 1 for a in  answer]