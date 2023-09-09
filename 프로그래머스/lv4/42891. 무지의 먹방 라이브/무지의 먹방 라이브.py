import heapq
def solution(food_times, k):
    if sum(food_times) <= k: return -1
    n=len(food_times)
    number=set(range(n))
    food = [(food_times[i],i) for i in range(n)]
    heapq.heapify(food)
    p=0
    while food:
        a,b = heapq.heappop(food)
        if (a-p) * n >= k:
            c = (k) % n
            number = sorted(list(number))
            answer = number[c] + 1
            break
        k -= (a-p)*n
        p = a
        number.remove(b)
        n -= 1
    return answer