def solution(money):
    answer = 0
    n = len(money)
    a1 = [0] * n
    a2 = [0]*n
    a1[0] = money[0]
    a1[1] = money[0]
    a2[0] = 0
    a2[1] = money[1]
    a1[2] = money[0] + money[2]
    a2[2] = max(a2[1], money[2])
    for i in range(3, n-1):
        a1[i] = max(money[i] + a1[i-2], a1[i-1])
        a2[i] = max(money[i] + a2[i-2], a2[i-1])
    a1[n-1] = a1[n-2]
    a2[n-1] = max(money[n-1] + a2[n-3], a2[n-2])
    return max(a1[-1], a2[-1])
   