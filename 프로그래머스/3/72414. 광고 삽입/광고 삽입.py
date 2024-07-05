def time_parser(time: str):
    HH, MM, SS = time.split(":")
    return int(SS) + 60*int(MM) + 3600*int(HH)
def log2time(log:str):
    start_time, end_time = log.split("-")
    st = time_parser(start_time)
    et = time_parser(end_time)
    return st, et
def time2str(time: int):
    SS = time % 60
    HH = time // 3600
    MM = (time // 60) % 60
    return f'{HH:0>2}:{MM:0>2}:{SS:0>2}'
def solution(play_time, adv_time, logs):
    times = [0]*(3600*100+2)
    adv_time = time_parser(adv_time)
    for log in logs:
        start_time, end_time = log2time(log)
        times[start_time] += 1
        times[end_time] -= 1
    for i in range(360000):
        times[i+1] += times[i]
    window = sum(times[:adv_time])
    max_idx = 0
    max_sum = window
    idx = adv_time
    while idx < (3600*100+1):
        window += - times[idx - adv_time] + times[idx]
        if window > max_sum:
            max_sum = window
            max_idx = idx - adv_time + 1
        idx += 1
    return time2str(max_idx)