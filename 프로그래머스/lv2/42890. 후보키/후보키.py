from itertools import combinations as C
def solution(relation):
    answer = 0
    N=len(relation[0])
    keys = set(range(N))
    unique = set()
    for i in range(N):
        candidates = list(C(keys, i+1))
        columns = [set() for _ in candidates]
        for n, candidate in enumerate(candidates):
            for row in relation:
                a = ""
                for c in candidate:
                    a += row[c]
                columns[n].add(a)
        for j in range(len(candidates)):
            if len(columns[j]) == len(relation):
                flag = True
                for k in range(i+1):
                    subs = tuple(C(candidates[j], k+1))
                    for sub in subs:
                        if sub in unique:
                            flag = False
                            break
                if flag:
                    answer += 1
                    unique.add(tuple(candidates[j]))

    return answer