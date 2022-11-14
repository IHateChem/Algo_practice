import sys
import heapq
input = sys.stdin.readline

#아읻디어: 보석 무게 역순 가방은 역순 정렬, 작은거 부터 사용. 과제문제랑 비슷하게. 

N, K = map(int, input().split())

jewels = []
for _ in range(N):
    M, V = map(int, input().split())
    jewels.append((M, V))
jewels.sort(reverse = True)
bag = []
for _ in range(K):
    C = int(input())
    bag.append(C)
bag.sort(reverse=True)
bag.append(0)
answer = 0
jewelspnt = 0
bagpnt = 0
store = []
bagmax = max(bag)
while jewelspnt < len(jewels):
    m, v = jewels[jewelspnt]
    if m <= bag[bagpnt]:
        heapq.heappush(store, v)
        bagpnt += 1
        answer += v
    elif m <= bagmax:
        if store[0] < v:
            a = heapq.heappop(store)
            answer -= a
            answer += v
            heapq.heappush(store, v)
    jewelspnt += 1
    
print(answer)