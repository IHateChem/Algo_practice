import heapq
def solution(lines):
    times=[]
    for line in lines:
        _,h,t=line.split()
        hour,minute,second=map(float,h.split(":"))
        end=int(hour)*3600000+int(minute)*60000+int(second*1000)
        #hour,minute,second= h.split(":")
        #end=int(hour+minute)*100000+int(float(second)*1000)
        time=int(float(t.strip("s"))*1000)
        start=end-time+1
        times.append((start,end))
    answer=0
    candidates=set()
    for s, e in times:
        candidates.add(s)
        candidates.add(e)
    candidates=sorted(list(candidates))
    stimes=sorted(times)
    windows=[];idx=0
    for s in candidates:
        end=s+1000
        while windows and windows[0][0] <s:
            heapq.heappop(windows)
        while idx<len(lines):
            if stimes[idx][0] < end: heapq.heappush(windows,(stimes[idx][1],stimes[idx][0]))
            else: break
            idx+=1
        answer = max(answer,len(windows))
    return answer