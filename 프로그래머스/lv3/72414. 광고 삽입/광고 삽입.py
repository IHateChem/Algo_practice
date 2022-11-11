def solution(play_time, adv_time, logs):
    end_time = list(map(int, play_time.split(":")))
    play_time = 3600*end_time[0] + 60*end_time[1] + end_time[2]
    adh, adm, ads = map(int, adv_time.split(":"))
    adv_time = adh*3600 + adm*60 + ads
    views = [0]*(play_time+1)
    for log in logs:
        log_start, log_end = log.split("-")
        log_st_time = list(map(int, log_start.split(":")))
        log_ed_time = list(map(int, log_end.split(":")))
        log_st = log_st_time[0]* 3600 + log_st_time[1] * 60 + log_st_time[2] 
        log_ed = log_ed_time[0] * 3600 + log_ed_time[1] * 60 + log_ed_time[2]
        views[log_st] += 1
        views[log_ed] -= 1
    for i in range(len(views)-1):
        views[i+1] += views[i]
    starttime = 0
    window = sum(views[:adv_time])
    maxtime = window
    for i in range(1, len(views)- adv_time+1):
        window -= views[i-1]
        window += views[i+adv_time-1]
        if window > maxtime:
            maxtime = window
            starttime = i
    answer_hw = starttime // 3600
    starttime = starttime %3600
    answer_m = starttime // 60
    answer = starttime % 60
    answer = str(answer_hw).zfill(2) + ":" + str(answer_m).zfill(2)+  ":" +str(answer).zfill(2)    
    return answer