from collections import defaultdict as dd
import heapq
def solution(genres, plays):
    answer = []
    total = dd(int)
    genreHeap = dd(list)
    idx=0
    for genre, play in zip(genres, plays):
        total[genre] += play
        heapq.heappush(genreHeap[genre], (-1*play, idx))
        idx += 1
    for genre, _ in sorted(total.items(), key = lambda t: t[1], reverse = True):
        n = 0
        while genreHeap[genre] and n < 2:
            p,i = heapq.heappop(genreHeap[genre])
            answer.append(i)
            n += 1
    return answer