def solution(info, n, m):
    num_items = len(info)

    # DP 테이블: A의 흔적을 기준으로 B의 최소 흔적을 저장
    dp = {0: 0}  # 초기 상태 (A 흔적 0 → B 흔적 0)

    for i in range(num_items):
        next_dp = {}
        a_trace, b_trace = info[i]
        
        for a_current, b_current in dp.items():
            # A가 i번 물건을 가져가는 경우
            a_next, b_next = a_current + a_trace, b_current
            if a_next < n and b_next < m:
                if a_next not in next_dp or next_dp[a_next] > b_next:
                    next_dp[a_next] = b_next

            # B가 i번 물건을 가져가는 경우
            a_next, b_next = a_current, b_current + b_trace
            if a_next < n and b_next < m:
                if a_next not in next_dp or next_dp[a_next] > b_next:
                    next_dp[a_next] = b_next

        dp = next_dp  # DP 테이블 갱신

        if not dp:  # 모든 경우가 경찰에 잡히는 경우
            return -1

    return min(dp.keys()) if dp else -1
