
# 0.5초 -> 1000만회
# 아파트 전체를 구성
bu = [[] * 15 for _ in range(15)]
for i in range(14):
    bu[0].append(i + 1)
for j in range(1, 15):  # 층
    for i in range(1, 15):  # 호
        bu[j].append(sum(bu[j - 1][:i]))

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    print(bu[k][n - 1])

