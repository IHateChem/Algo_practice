def solution(n, k, cmd):
    table = {i:[i-1, i+1] for i in range(n)}
    m=0
    M=n-1
    table[-1] = [-1,0]
    table[n] = [n-1, n]
    last = []
    for c in cmd:
        order = c.split()
        if order[0] == "U":
            for i in range(int(order[1])):
                k = max(table[k][0],m)
        if order[0] == "D":
            for i in range(int(order[1])):
                k = min(table[k][1],M)
        if order[0] == "C":
            l, r = table[k]
            table[l][1] = r
            table[r][0] = l
            last.append(k)
            k = r
            if k == n: k = l
        if order[0] == "Z":
            t= last.pop()
            l, r = table[t]
            table[l][1] = t
            table[r][0] = t
    answer = ["O"]*n
    while last:
        t = last.pop()
        answer[t] = "X"
    return "".join(answer)
