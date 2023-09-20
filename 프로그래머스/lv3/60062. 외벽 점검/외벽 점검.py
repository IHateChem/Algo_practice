def solution(n, weak, dist):
    answer = 1
    weakSet = set(weak)
    weakindex = {w:2**i for i, w in enumerate(weak)}
    dest=2**len(weak)-1
    bits = set()
    N = len(dist)
    for i in range(len(weak)):
        for j in range(N):
            pos = weak[i]
            bit = weakindex[weak[i]]
            for _ in range(dist[j]):
                pos += 1
                pos %= n
                if pos in weakSet:
                    bit += weakindex[pos]
            bits.add((bit, 2**j))
    q = list(bits);t=[];visited=set()
    distmask = 2**N -1
    for bit, check in bits:
        visited.add(bit)
    while q and answer <= N:
        bit, checked = q.pop()
        if bit == dest: break
        for firstbit, fcheck in bits:
            if fcheck & checked: continue
            t_bit = bit ^ firstbit
            if not t_bit in visited:
                visited.add(t_bit)
                t.append((t_bit, fcheck^checked))
        if not q:
            q = t
            t = []
            answer += 1
    else: answer = -1
    return answer