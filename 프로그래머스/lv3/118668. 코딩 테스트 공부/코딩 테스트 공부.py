import heapq


def MKgraph(alp, cop, problems):
    alp_max = 0
    cop_max = 0
    edges = []
    INF = 100000000
    for problem in problems:
        alp_max = max(problem[0], alp_max)
        cop_max = max(problem[1], cop_max)
        edges.append(problem)
    if alp_max <= alp and cop >= cop_max:
        return 0
    elif alp_max <= alp:
        alp = alp_max
    elif cop >= cop_max:
        cop = cop_max
    d = [[INF for i in range(alp_max+1)] for m in range(cop_max+1)]
    d[cop][alp] = 0
    possibles = [[[(1, 0, 1)] for _ in range(alp_max+1)] for __ in range(cop_max+1)]
    for __ in range(alp_max+1):
        for _ in range(cop_max+1):
             possibles[_][__].append((0, 1, 1))
    for alpr, copr,  talp, tcop, tconst in edges:
        for m in range(alpr, alp_max + 1):
            for i in range(copr, cop_max +1):
                possibles[i][m].append((talp, tcop, tconst))
    stack = []
    heapq.heappush(stack, (0, alp, cop))
    while stack:
        time, m, i = heapq.heappop(stack)
        if i == cop_max and m == alp_max:
            return time
        for  talp, tcop, tconst in possibles[i][m]:
            x = i + tcop if i + tcop <= cop_max else cop_max
            y = m + talp if m + talp <= alp_max else alp_max
            if d[x][y] != min(d[i][m] + tconst, d[x][y]):
                d[x][y] = min(d[i][m] + tconst, d[x][y])
                heapq.heappush(stack, (d[x][y], y, x))
def solution(alp, cop, problems):
    answer =MKgraph(alp, cop,problems)
    return answer
