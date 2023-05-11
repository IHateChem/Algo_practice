count = int(input())
for i in range(count):
    student = list(map(int,input().split()))
    sum = 0
    aver = 0
    for j in range((len(student)-1)):
        sum += student[j+1]
    average = sum / student[0]
    for l in student[1:]:
        if l > average:
            aver += 1
    lo = aver / student[0]
    percent = lo * 100
    formatpercent = "{:.3f}%".format(percent)
    
    print(formatpercent)