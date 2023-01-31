def get_last(l, idx):
    while idx != -1:
        if l[idx] == 0:
            idx -=1
        else: break
    return idx
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_last = get_last(deliveries, n-1)
    pickup_last = get_last(pickups, n-1)
    while deliver_last != -1 or pickup_last != -1:
        weight = 0
        if deliver_last != -1:
            idx = deliver_last
            answer += deliver_last + 1
            while deliver_last != -1:
                if deliveries[deliver_last]:
                    if weight + deliveries[deliver_last] <= cap:
                        weight += deliveries[deliver_last]
                        deliveries[deliver_last] = 0
                    else:
                        deliveries[deliver_last] -= cap - weight
                        weight = cap
                        break
                deliver_last -= 1
        if pickup_last != -1:
            answer += abs(pickup_last - idx)
            idx = pickup_last
            weight= 0
            while pickup_last != -1:
                if pickups[pickup_last]:
                    if weight + pickups[pickup_last] <= cap:
                        weight += pickups[pickup_last]
                        pickups[pickup_last] = 0
                    else:
                        pickups[pickup_last] -= cap - weight
                        weight = cap
                        break
                pickup_last -= 1
        answer += idx + 1
        idx = -1
        deliver_last = get_last(deliveries, deliver_last)
        pickup_last = get_last(pickups, pickup_last)
    return answer