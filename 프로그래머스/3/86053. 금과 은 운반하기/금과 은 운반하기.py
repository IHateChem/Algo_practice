def solution(a, b, g, s, w, t):
    def is_possible(time):
        total_gold = 0
        total_silver = 0
        total_weight = 0

        for i in range(len(g)):
            trips = time // (2 * t[i])
            if time % (2 * t[i]) >= t[i]:
                trips += 1
            max_weight = trips * w[i]

            gold = min(g[i], max_weight)
            silver = min(s[i], max_weight)
            total = min(g[i] + s[i], max_weight)

            total_gold += gold
            total_silver += silver
            total_weight += total

        return total_gold >= a and total_silver >= b and total_weight >= a + b

    left, right = 0, 10**15
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer