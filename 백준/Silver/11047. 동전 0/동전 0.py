import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
ans = 0
sel_coin = []
for coin in coins:
    if coin <= K:
       sel_coin.append(coin)
    else:
        break
for i in sel_coin[::-1]:
    ans += K//i
    K %= i
    if not K:
        break
print(ans)