from collections import deque as dq
def solution(n, m, x, y, r, c, k):
    num_d = r - x
    num_l = y - c 
    num_r = c - y if c - y > 0 else 0
    num_u = x - r if x - r > 0 else 0
    num = abs(num_d) + abs(num_l)
    if (num ) % 2 != k % 2: return "impossible"
    if (num ) > k: return "impossible"
    answer = []
    answer.append("d"*num_d)
    x += num_d if num_d > 0 else 0
    while num < k and x < n:
        answer.append("d")
        x += 1
        num += 2
        num_u += 1
    answer.append("l"*num_l)
    y -= num_l if num_l > 0 else 0
    while num < k and y >1:
        answer.append("l")
        y -= 1
        num += 2
        num_r += 1
    while num < k:
        answer.append("rl")
        num += 2
    answer.append("r"*num_r)
    answer.append("u"*num_u)
    answer = "".join(answer)
    return answer