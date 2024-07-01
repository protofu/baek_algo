# n 동전 종류 개수, k 만들어야할 금액
n, k = map(int, input().split())
# 동전 종류 리스트로 받기
coins = [int(input()) for _ in range(n)]
# 최대한 적게 쓰기
# 큰 금액부터 채우기
use_cnt = 0
for idx in range(n-1, -1, -1):
    # 사용할 동전보다 가치가 크거나 같다면
    if k >= coins[idx]:
        # 총 금액을 동전 가치로 나눈 몫 = 사용할 코인 개수
        use_cnt += k//coins[idx]
        # 사용한 만큼 금액에서 빼주기
        k %= coins[idx]
print(use_cnt)
