from itertools import product
def rotate(clock, i,j,r):
    neighbors = [(x,y) for x,y in ((i,j),(i-1,j),(i+1,j),(i,j-1),(i,j+1)) if 0<=x<len(clock) and 0<=y<len(clock)]
    for i,j in neighbors:
        clock[i][j] = (clock[i][j] + r) % 4
def solution(clockHands):
    answer = 100000000
    for firstRotate in product(range(4), repeat=len(clockHands)):
        t=sum(firstRotate)
        clock=[[k for k in i] for i in clockHands]
        for n,r in enumerate(firstRotate): rotate(clock,0,n,r)
        for i in range(1, len(clockHands)):
            for j in range(len(clockHands)):
                if (4 - clock[i-1][j])%4:
                    t += 4 - clock[i-1][j]
                    rotate(clock,i,j,4 - clock[i-1][j])
        if not sum(clock[-1]): answer= min(answer, t)
    return answer