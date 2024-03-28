def solution(land):
    answer = 0
    n = len(land)
    dp = land
    for i in range(1, n):
        for j in range(4):
            dp[i][j] += max(dp[i-1][:j] + dp[i-1][j+1:])
    answer = max(dp[-1])
    return answer