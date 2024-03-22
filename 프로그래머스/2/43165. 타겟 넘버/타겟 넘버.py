def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(idx, rlt):
        if idx == n:
            if rlt == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, rlt+numbers[idx])
            dfs(idx+1, rlt-numbers[idx])
    dfs(0, 0)
    return answer