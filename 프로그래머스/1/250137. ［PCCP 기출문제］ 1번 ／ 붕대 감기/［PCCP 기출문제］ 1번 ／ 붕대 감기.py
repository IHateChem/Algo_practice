def solution(bandage, health, attacks):
    # t초동안 붕대 감으면 1초마다 x회복, t초 연속 성공시 y추가.  << 최대체력 못넘음. 
    # 몬스터 공격 당하면 취소
    # 몬스터 공격당하면 현재 체력 줄어듬 0 이되면 으악. 더이상 회복 불가. 
    b_time, x, y = bandage
    answer = health
    idx = 0
    t_time = 0;
    for i in range(1, 10000):
        if attacks[idx][0] != i:
            answer = min(health, answer + x)
            t_time += 1
            if t_time == b_time:
                answer = min(health, answer + y)
                t_time = 0
        else:
            answer -= attacks[idx][1]
            if answer <= 0 or idx == len(attacks)-1: break
            idx += 1
            t_time = 0
    return answer if answer > 0 else -1