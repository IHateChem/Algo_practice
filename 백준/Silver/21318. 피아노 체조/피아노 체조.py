import sys
input =sys.stdin.readline
N = int(input())
musics = list(map(int,input().split()))
summuscis = [0]
for i in range(N-1):
    summuscis.append(summuscis[i] +( musics[i+1] < musics[i]) )
Q=int(input())
for _ in range(Q):
    x,y=map(int,input().split())
    print(summuscis[y-1]-summuscis[x-1])