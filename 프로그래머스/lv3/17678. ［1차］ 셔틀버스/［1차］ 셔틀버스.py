from collections import deque 
def solution(n, t, m, timetable):
    timeList=[0]*(24*60)
    for time in timetable:
        H,M=map(int,time.split(":"))
        timeList[H*60+M] += 1
    busTime=540;cnt=0;bus=0;answerTime=busTime
    for time in range(24*60):
        if time>busTime and bus<n:
            bus+=1
            busTime+=t
            cnt=0
            if bus<n:answerTime=busTime
            else:break
        if not timeList[time]: continue
        people=timeList[time]
        cnt+=people
        if cnt<m: continue
        while cnt>=m:
            cnt -= m
            bus += 1
            busTime+=t
            if bus<n:answerTime=busTime
            else:
                answerTime=time-1
                break
        else:
            continue
        break
    H=answerTime//60;M=answerTime%60
    if H<10:
        H = "0" + str(H)
    else:H=str(H)
    if M<10:
        M="0"+str(M)
    else:
        M=str(M)
    answer = H+":"+M
    return answer