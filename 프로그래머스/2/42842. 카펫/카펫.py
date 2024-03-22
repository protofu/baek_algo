def solution(brown, yellow):
    answer = []
    lst = []
    rlt = []
    total = brown + yellow
    for i in range(1, yellow+1):
        if yellow%i == 0 and yellow >= i*i:
            lst.append(i+2)
    for n in lst:
        if total % n == 0:
            if (n-2)*(total//n-2) == yellow:
                answer.append(total//n)
                answer.append(n)
    return answer