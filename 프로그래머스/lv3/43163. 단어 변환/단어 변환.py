def solution(begin, target, words):
    N = len(words)
    if not begin in words:
        N += 1
        words.append(begin)
        begin = N -1
    else:
        begin = words.index(begin)
    if not target in words:
        return 0
    else:
        target = words.index(target)
    edges = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            diff = 0
            for i_word, j_word in zip(words[i], words[j]):
                if i_word != j_word: diff += 1
                if diff > 1: break
            else:
                edges[i].append(j)
                edges[j].append(i)
    print(words)
    print(edges)
    stack = [begin]; t= []
    answer = 1
    visited = [0]*N
    visited[begin] = 1
    while stack:
        u = stack.pop()
        for v in edges[u]:
            #print(words[v])
            if not visited[v]:
                if v == target: return answer
                t.append(v)
                visited[v] = 1
        if not stack:
            answer += 1
            stack = t
            t = []
    return 0