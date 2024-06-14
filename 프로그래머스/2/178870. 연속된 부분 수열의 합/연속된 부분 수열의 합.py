def solution(sequence, k):
    l = 0
    r = 0
    _sum = sequence[0]
    _len = len(sequence) + 1
    answer = [-1,-1]
    while l < len(sequence):
        if _sum == k:
            if r-l +1 < _len:
                answer = [l,r]
                _len = r- l + 1
        if _sum == k or r == len(sequence) - 1 or _sum  > k:
            _sum -= sequence[l]
            l += 1
        elif _sum < k:
            r += 1
            _sum += sequence[r]
    return answer