import sys
input = sys.stdin.readline
from collections import defaultdict as dd
nations = list(input().strip().split())
games = []
for _ in range(6):
    n1, n2, w, d, l = input().strip().split()
    w = float(w); d = float(d); l = float(l)
    games.append((n1,n2,w,d,l))
def game(N, score, p, final):
    if N == 6:
        rank = []
        for nation in nations:
            rank.append((score[nation], nation))
        rank.sort(reverse=True)
        for i, tp in enumerate(rank):
            sc, na = tp
            if i == 0: winner = [[sc, na]]
            elif winner[-1][0] == sc: winner[-1].append(na)
            else:
                winner.append([sc, na])
        num = 0 
        for win in winner:
            n = len(win) - 1
            if n + num <= 2:
                for na in win[1:]:
                    final[na] += p
                num += n
            else:
                for na in win[1:]:
                    final[na] += p* ((2-num)/(n))
                num += n
            if num >= 2:
                return final
    n1, n2, w, d,l = games[N]
    if w != 0:
        score[n1] += 3
        game(N+1, score, p*w, final)
        score[n1] -= 3
    if d != 0:
        score[n1] += 1
        score[n2] += 1
        game(N+1, score, p*d,final)
        score[n1] -= 1
        score[n2] -= 1
    if l != 0:
        score[n2] += 3
        game(N+1, score, p*l, final)
        score[n2] -= 3
    return final
final = game(0, dd(int), 1, dd(int))
for nation in nations:
    print(final[nation])