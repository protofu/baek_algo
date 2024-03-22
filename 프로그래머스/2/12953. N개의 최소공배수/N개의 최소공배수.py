def solution(arr):
    answer = 0
    mnum = max(arr)
    strnum = 1
    while True:
        num = mnum * strnum
        cnt = 0
        for i in arr:
            if num % i != 0:
                strnum += 1
                break
            else:
                cnt += 1
        if cnt == len(arr):
            break
    answer = mnum * strnum
    return answer