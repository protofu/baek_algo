def solution(nums):
    answer = 0
    n = len(nums)
    # 서로 다른 3개를 골라 더했을때 소수인가
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                ijk = nums[i]+nums[j]+nums[k]
                # ijk가 소수인지 판별 n^4 => 6,250,000  --> 0.625s
                isPrime = True
                for q in range(2, ijk):
                    if ijk%q == 0:
                        isPrime = False
                        break
                if isPrime:
                    answer += 1
                    
                
    return answer