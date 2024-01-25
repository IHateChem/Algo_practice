import sys
import heapq
input = sys.stdin.readline
N,K = map(int,input().split())
customers = [list(map(int,input().split())) for N in range(N)]
counters = []; counterNumbers = [i for i in range(K)]
def out(turn):
    outs = []
    while counters and counters[0][0] == turn:
        t, c, n = heapq.heappop(counters)
        outs.append(n)
        heapq.heappush(counterNumbers, c)
    return reversed(outs)
def counterIn(turn, idx):
    while counterNumbers and idx < N:
        id, w = customers[idx]
        idx += 1
        c = heapq.heappop(counterNumbers)
        heapq.heappush(counters, (turn+w, c, id))
    return idx
turn = 0; idx = 0; answer = []
while len(answer)< N:
    answer.extend(out(turn))
    idx = counterIn(turn, idx)
    turn += 1
print(sum([(i+1)*answer[i] for i in range(N)]))