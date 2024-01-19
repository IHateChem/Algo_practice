def getInSingleList(a, n):
    a_set = set(a)
    for c in a:
        if n+1 - c in a_set:
            a_set.remove(c)
            a_set.remove(n+1-c)
            return list(a_set)
    return a

def getInDoubleList(a,b, n):
    a_set = set(a)
    b_set = set(b)
    for c in a:
        if n+1 - c in b_set:
            a_set.remove(c)
            b_set.remove(n+1-c)
            return list(a_set), list(b_set)
    return a, b

def solution(coin, cards):
    n = len(cards)
    answer = 1
    a = cards[:n//3]
    b = []
    idx = n//3
    while idx<n:
        b.append(cards[idx])
        b.append(cards[idx+1])
        idx += 2
        new_a = getInSingleList(a, n)
        answer += 1
        if len(new_a) != len(a):
            a = new_a
            continue
        new_a, new_b = getInDoubleList(a,b, n)
        if coin > 0 and len(new_a) != len(a):
            a = new_a
            b = new_b
            coin -= 1
            continue
        new_b = getInSingleList(b, n)
        if coin > 1 and len(new_b) != len(b):
            b = new_b
            coin -=2
            continue
        answer -= 1
        break
    return answer