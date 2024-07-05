import sys
input = sys.stdin.readline
N = int(input())
pollutions = [list(map(int, input().split())) for _ in range(N)]
pollutions.sort()
def calc(polls):
    cnt = polls[0][1]
    _x = polls[0][0]
    n = 1
    if len(polls) > 1:
        for x,p in polls[1:]:
            cnt += p + n*abs(x-_x)
            n+= 1
            _x = x
    return cnt
left = calc(pollutions)
right = calc(pollutions[::-1])
answer = min(left, right)
if (len(pollutions) > 1):
    answer = min(answer, calc(pollutions[1:]), calc(pollutions[::-1][1:]))
    answer = min(   answer, calc(pollutions[:-1]), calc(pollutions[::-1][:-1]))
else:
    answer = 0
for i in range(N-2):
    pollution = pollutions[i+1]
    answer = min(answer,left - pollution[1] - (pollutions[-1][0] - pollution[0]), right  - pollution[1] - (pollution[0] - pollutions[0][0]))
    
print(answer)