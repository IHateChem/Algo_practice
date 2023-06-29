def timediff(start, finish):
    h1, m1 = map(int, finish.split(":"))
    h2, m2 = map(int,start.split(":"))
    return (h1-h2)*60 + m1 - m2
def musicSplitter(music):
    return music.replace("C#", "H").replace("D#", "I").replace("A#", "J").replace("G#","K").replace("F#","L")
def solution(m, musicinfos):
    answer =  "(None)"
    m = musicSplitter(m)
    howLong = 0
    for musicinfo in musicinfos:
        start, finish, title, music = musicinfo.split(",")
        music = musicSplitter(music)
        Long = timediff(start, finish)
        t = []
        for i in range(Long):
            t.append(music[i%len(music)])
        t = "".join(t)
        if m in t and howLong < Long:
            answer = title
            howLong = Long
    return answer