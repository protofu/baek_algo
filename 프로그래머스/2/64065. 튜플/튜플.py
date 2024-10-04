def solution(s):
    answer = []
    rlt = []
    str_list = s.replace("},{", "|").replace("{", "").replace("}", "")
    str_list = str_list.split("|")
    tmp = []

    for j in str_list:
        tmp = []
        for i in j.split(","):
            tmp.append(int(i))
        rlt.append(tmp)
    sorted_rlt = sorted(rlt, key=len)
    for i in sorted_rlt:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer