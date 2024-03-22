def solution(progresses, speeds):
    answer = []
    days = []
    len_pro = len(progresses)
    for i in range(len_pro):
        if (100 - progresses[i])%speeds[i] != 0:
            day = (100 - progresses[i])//speeds[i] + 1
        else:
            day = (100 - progresses[i])//speeds[i]
        days.append(day)
    tmp = days[0]
    cnt = 0
    for i in range(len(days)):
        if days[i] > tmp:
            tmp = days[i]
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
        if i == len(days)-1:
            answer.append(cnt)
    return answer