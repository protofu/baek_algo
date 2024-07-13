n, m = map(int, input().split())
cards = list(map(int ,input().split()))
# 합을 -1로 해두기
ans = -1
# 카드 3장이라 쉽게 생각 3중 for, N이 100이하라 100만번 안에 끝남
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_cards = cards[i]+cards[j]+cards[k]
            # m보다 합이 작거나 같고, 합이 원래 저장된 합보다 크면 초기화
            if sum_cards <= m and sum_cards > ans:
                ans = sum_cards
print(ans)