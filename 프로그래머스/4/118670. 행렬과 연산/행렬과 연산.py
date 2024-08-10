def rotate(start, end, rc, col1, col2):
    R = len(rc)
    C = len(rc[0])
    rc[start].pop()
    col2.appendleft(rc[start][-1])
    col2.pop()
    rc[end].append(col2[-1])
    rc[end].popleft()
    col1.append(rc[end][0])
    col1.popleft()
    rc[start].appendleft(col1[0])
from collections import deque as dq
def solution(rc, operations):
    start = 0
    end = len(rc)-1
    rc_dq = [dq(rc[i]) for i in range(len(rc))]
    col1 = dq([rc[i][0]for i in range(len(rc))])
    col2 = dq([rc[i][-1] for i in range(len(rc))])
    for op in operations:
        if op == "Rotate":
            rc_dq[start][0] = col1[0]
            rc_dq[start][-1] = col2[0]
            rc_dq[end][0] = col1[-1]
            rc_dq[end][-1] = col2[-1]
            rotate(start, end, rc_dq, col1, col2)
        else:
            col1.appendleft(col1.pop())
            col2.appendleft(col2.pop())
            start = (start - 1) % len(rc)
            end = (end - 1) % len(rc)
    answer = []
    for i in range(len(rc)):
        rc_dq[(start +i) % len(rc)][0] = col1[i]
        rc_dq[(start +i) % len(rc)][-1] = col2[i]
        answer.append(list(rc_dq[(start +i) % len(rc)]))
    return answer