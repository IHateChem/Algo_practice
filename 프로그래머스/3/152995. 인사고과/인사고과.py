def solution(scores):
    N = len(scores)
    wanho = scores[0]
    scores.sort(reverse=True)
    newScores = []
    maxB = 0
    maxA = 0
    for a, b in scores:
        if a < maxA and b < maxB: continue
        maxB = max(b, maxB)
        maxA = max(a,maxA)
        newScores.append((a,b))
    scoreSet = set(newScores)
    maxB = 0
    maxA = 0
    scores.sort(reverse=True, key=lambda t: (t[1], t[0]))
    for a, b in scores:
        if a < maxA and b < maxB: continue
        maxB = max(b, maxB)
        maxA = max(a,maxA)
        if (a,b) in scoreSet: continue
        newScores.append((a,b))
    totalScores = sorted([i+j for i,j in newScores])
    score2rank = {totalScores[i]: len(newScores)-i for i in range(len(newScores))} 
    for a, b in newScores:
        if [a,b] == wanho: return score2rank[sum(wanho)]
    return -1