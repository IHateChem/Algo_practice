def solution(enroll, referral, seller, amount):
    adress = {}
    n = len(enroll)
    adress["-"] = n
    enroll.append("-")
    for i in range(n):
        name = enroll[i]
        adress[name] = i
        referral[i] = adress[referral[i]]
    answer = [0]*len(referral)
    for i in range(len(seller)):
        revenue = amount[i] * 100
        idx = adress[seller[i]]
        while revenue != 0 and idx != n:
            fee = revenue // 10
            answer[idx] += revenue - fee
            revenue = fee
            idx = referral[idx]
             
    return answer