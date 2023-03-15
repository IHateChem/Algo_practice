#해쉬 이용한 풀이.. 시간 줄일려고 고민했는데 정작 비슷함. 
import sys
from itertools import permutations as P
from collections import defaultdict as dd
input = sys.stdin.readline
N = int(input())
inings = [list(map(int, input().split())) for _ in range(N)]
sequence = P(range(1,9), 8)
answer = 0
history = dd(tuple)
power_table = [[5**_ * j for j in range(5)] for _ in range(9)]
def hash(ining, number, seq):
    t = 0
    for _ in range(9):
        t+= power_table[_][ining[seq[number]]]
        number = (number+1)%9
    return t
for seq in sequence:
    order = list(seq)
    order.insert(3,0)
    num = 0
    tot_score=  0
    for ining in inings:
        key = hash(ining, num, order)
        if not history[key]:
                origin = num
                b3, b2, b1 = 0,0,0
                out = 0
                score = 0
                while out < 3:
                        step = ining[order[num]]
                        if step ==  0:
                                out += 1
                        elif step ==  1:
                                score += b3
                                b3 = b2
                                b2 = b1
                                b1 = 1
                        elif step ==  2:
                                score += b3+b2
                                b3 = b1
                                b2 = 1
                                b1 = 0
                        elif step ==  3:
                                score += b3+b2+b1
                                b3 = 1
                                b2 = 0
                                b1 = 0
                        else:
                                score += b3+b2+b1+1
                                b3 = 0
                                b2 = 0
                                b1 = 0
                        num = (num+1)%9
                dif  = num - origin
                history[key] = (score, dif)
                num = origin
        tot_score += history[key][0]
        num = (num+ history[key][1]) % 9
    answer = max(answer, tot_score)
print(answer)