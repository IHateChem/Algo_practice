def solution(n, money):
    answer = 0
    dp = [1]+[0] * n
    #howto = [set([0 for i in money])] + [set() for _ in range(n)]
    for m in range(len(money)):
        for i in range(n+1):
            if not dp[i]:continue
            if i +money[m] > n: break
            dp[i+money[m]] += dp[i]
    answer = dp[-1]
    return answer