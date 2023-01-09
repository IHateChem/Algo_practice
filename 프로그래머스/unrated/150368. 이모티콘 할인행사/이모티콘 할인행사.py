import sys
input = sys.stdin.readline
def check(e, users, pnts):
    tot_price =0
    n = 0
    for user in users:
        price = 0
        for i, pn in enumerate(pnts):
            if user[0] <= e[i][pn][0]:
                price += e[i][pn][1]
            if price >= user[1]:
                n += 1
                price = 0
                break
        tot_price += price
    return n, tot_price
def nextpnt(pnts, i):
    pnts[i] += 1
    T = False
    if pnts[i] == 4:
        pnts[i] = 0
        if i + 1== len(pnts): return True
        T = nextpnt(pnts, i+1)
    return T

def solution(users, emoticons):
    answer = [0, 0]
    possible = [[] for _ in emoticons]
    discounts = [40,30,20,10]
    for i, emoticon in enumerate(emoticons):
        for dis in discounts:
            possible[i].append((dis, (1-dis/100)*emoticon))
    pnts = [0]*len(emoticons)
    pnt = 0
    max_pnt = 0
    while 1:
        n, price = check(possible, users, pnts)
        if answer[0] < n:
            answer[0] = n
            answer[1] = price
        elif answer[0] == n:
            answer[1] = max(answer[1], price)
        if nextpnt(pnts, 0): break
    return answer
users = 	[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]