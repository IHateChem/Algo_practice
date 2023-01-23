import sys
input = sys.stdin.readline
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
if (x1, y1) > (x2, y2): x1, y1, x2, y2 = x2, y2, x1, y1
if (x3, y3) > (x4, y4): x3, y3, x4, y4 = x4, y4, x3, y3
def ccw(a, b, c, d, e, f):
    return (c-a)*(f-b) - (e-a)*(d-b)
def get_crosspt(x11,y11, x12,y12, x21,y21, x22,y22):
    if x12==x11:
        cx = x12
        m2 = (y22 - y21) / (x22 - x21)
        cy = m2 * (cx - x21) + y21
        return cx, cy
    if x22==x21:
        cx = x22
        m1 = (y12 - y11) / (x12 - x11)
        cy = m1 * (cx - x11) + y11
        return cx, cy
    m1 = (y12 - y11) / (x12 - x11)
    m2 = (y22 - y21) / (x22 - x21)
    cx = (x11 * m1 - y11 - x21 * m2 + y21) / (m1 - m2)
    cy = m1 * (cx - x11) + y11
    return cx, cy
b1 = ccw(x1, y1, x2, y2, x3, y3)
b2 = ccw(x1, y1, x2, y2, x4, y4)
b3 = ccw(x3, y3, x4, y4, x1, y1)
b4 = ccw(x3, y3, x4, y4, x2, y2)
if min(x1, x2) > max(x3, x4) or min(x3, x4) > max(x1, x2) or min(y1, y2) > max(y3, y4) or min(y3, y4) > max(y1, y2):
    print(0)
    exit(0)
elif b1*b2 <= 0  and b3 * b4 <= 0:
    print(1)
    if (x4 - x3) * (y2 - y1) == (x2 - x1) * (y4 - y3):
        if max(x1, x2) == min(x3, x4) or max(x3, x4) == min(x1, x2):
            if (x1,y1) in [(x3, y3), (x4, y4)]: print(*(x1, y1))
            elif (x2, y2) in [(x3, y3), (x4, y4)]: print(*(x2, y2))

    else: print(*get_crosspt(x1, y1, x2, y2, x3, y3, x4, y4))
else:
    print(0)