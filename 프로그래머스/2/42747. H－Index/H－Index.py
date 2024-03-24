def solution(citations):
    answer = 0
    # 이분탐색..?
    n = len(citations) # 논문 수  
    use_cnt = sum(citations) # 인용 수
    avr_use = use_cnt//n # 평균 인용 수
    while avr_use != 0 or avr_use != max(citations):
        cnt = 0
        for cit in citations:
            if cit >= avr_use:
                cnt += 1
        if avr_use <= cnt and avr_use >= n-cnt:
            answer = avr_use
            break
        elif avr_use > cnt:
            avr_use -= 1
    
    return answer