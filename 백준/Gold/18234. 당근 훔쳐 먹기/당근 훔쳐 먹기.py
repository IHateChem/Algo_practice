import sys
input = sys.stdin.readline
N, T = map(int,input().split())
carrots =  sorted([list(map(int,input().split())) for _ in range(N)], key=lambda t:( t[1]))
print(sum(map(lambda carrot: (T-N+carrot[0]) * carrot[1][1] + carrot[1][0]  , enumerate(carrots))))