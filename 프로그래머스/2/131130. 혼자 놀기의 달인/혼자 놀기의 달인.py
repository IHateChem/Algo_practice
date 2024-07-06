def solution(cards):
    visited = set()
    group_size = []
    def dfs(a, group_len):
        visited.add(a)
        if cards[a] -1 in visited:
            return group_len
        return dfs(cards[a]-1, group_len+1)
    answer = 0
    for i in range(len(cards)):
        if i in visited: continue
        group_size.append(dfs(i, 1))
    if len(group_size) == 1: return 0
    group_size.sort()
    return group_size[-1] * group_size[-2]