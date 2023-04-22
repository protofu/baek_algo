import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))

# 팰린드롬 여부를 저장할 이중 리스트
dp = [[0 for _ in range(n)] for _ in range(n)]

# 길이가 1인 부분 수열은 항상 팰린드롬
for i in range(n):
    dp[i][i] = 1

# 길이가 2인 부분 수열은 두 수가 같으면 팰린드롬
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

# 길이가 3 이상인 부분 수열
for length in range(3, n+1):
    for start in range(n-length+1):
        end = start + length - 1
        if nums[start] == nums[end] and dp[start+1][end-1]:
            dp[start][end] = 1

m = int(input().rstrip())

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
