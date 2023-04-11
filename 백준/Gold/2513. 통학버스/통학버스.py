import sys
input = sys.stdin.readline
N, K, S = map(int, input().split())
street = [0]*100001
start = 100002;end=0
for _ in range(N):
    a,b=map(int,input().split())
    end = max(end,a)
    street[a] = b
bus=0; answer = 0
for i in range(S):
    if street[i] and not bus:
        while street[i]:
            if street[i] < K:
                bus += street[i]
                answer += 2*(S-i)
                street[i] = 0
            else:
                street[i] -= K
                answer += 2*(S-i)
    elif street[i]:
        while street[i]:
            if bus:
                if street[i]+bus < K:
                    bus += street[i]
                    street[i] = 0
                else:
                    street[i] -= (K-bus)
                    bus = 0
            else:
                if street[i] < K:
                    bus += street[i]
                    answer += 2*(S-i)
                    street[i] = 0
                else:
                    street[i] -= K
                    answer += 2*(S-i)
bus = 0
for i in range(end, S, -1):
    if street[i] and not bus:
        while street[i]:
            if street[i] < K:
                bus += street[i]
                answer += 2*(i-S)
                street[i] = 0
            else:
                street[i] -= K
                answer += 2*(i-S)
    elif street[i]:
        while street[i]:
            if bus:
                if street[i]+bus < K:
                    bus += street[i]
                    street[i] = 0
                else:
                    street[i] -= (K-bus)
                    bus = 0
            else:
                if street[i] < K:
                    bus += street[i]
                    answer += 2*(i-S)
                    street[i] = 0
                else:
                    street[i] -= K
                    answer += 2*(i-S)
print(answer)