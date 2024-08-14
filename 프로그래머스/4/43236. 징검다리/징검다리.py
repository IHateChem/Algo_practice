def calc(rocks, m, distance):
    p = 0
    t =  0
    for r in rocks:
        if r - p >= m:
            p = r
        else:
            t += 1
    return t
def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()

    l = 1
    r = distance
    ans = distance
    while l <= r:
        m = (l+r)//2
        p = 0
        t = calc(rocks, m, distance)
        if n < t:
            r = m - 1
        else:
            l = m + 1
            ans = m
    return ans