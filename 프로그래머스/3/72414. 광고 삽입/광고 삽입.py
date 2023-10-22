def solution(play_time, adv_time, logs):
    answer = ''
    def toIndex(t):
        h,m,s= map(int, map(str.lstrip,t.split(":")))
        return h*3600+m*60+s
    def toTime(t):
        h = t // 3600
        m = (t-h*3600) // 60
        s = t % 60
        if h < 10: h = "0" + str(h)
        if m < 10: m = "0" + str(m)
        if s < 10: s = "0" + str(s)
        return str(h) + ":"+ str(m)+ ":" + str(s)
    times = [0]*100*3600
    for log in logs:
        s,e = log.split("-")
        start = toIndex(s)
        end= toIndex(e)
        times[start]+= 1
        times[end] -= 1
    idx=0
    window=0
    windowSize = toIndex(adv_time)
    for i in range(1, 100*3600):
        times[i] += times[i-1]
    for i in range(windowSize):
        window += times[i]
    answer = window
    for i in range(windowSize,100*3600):
        window -= times[i-windowSize] - times[i]
        if answer < window:
            answer =  window
            idx = i-windowSize+1
    
        
        
    return toTime(idx)