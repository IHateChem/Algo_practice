#아이디어1. 세그먼트 트리 사용. 
#아이디어2. dp. 
def solution(sequence):
    n = len(sequence)
    dp_p = [s for s in sequence]
    dp_n = [-1*s for s in sequence]
    for i in range(1, n):
        dp_p[i] = max(dp_p[i], dp_n[i-1]+sequence[i])
        dp_n[i] = max(dp_n[i], dp_p[i-1]+ (-1)*sequence[i])
    answer = max(dp_p + dp_n)
    return answer