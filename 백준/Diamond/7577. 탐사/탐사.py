l, n = map(int, input().split())

# 그래프 초기화
w = [[1e9]*(l+1) for _ in range(l+1)]
for i in range(l):
    w[i+1][i] = 0
    w[i][i+1] = 1

# 입력받은 값으로 그래프 갱신
for i in range(n):
    x, y, z = map(int, input().split())
    if w[x-1][y] > z:
        w[x-1][y] = z
    w[y][x-1] = -z

# 플로이드-와샬 알고리즘
for i in range(l+1):
    for j in range(l+1):
        for k in range(l+1):
            if w[j][i]+w[i][k] < w[j][k]:
                w[j][k] = w[j][i]+w[i][k]

# 사이클 검사
for i in range(l+1):
    if w[i][i] < 0:
        print("NONE")
        exit()

# 결과 출력
for i in range(l):
    if w[0][i+1]-w[0][i]:
        print("#", end="")
    else:
        print("-", end="")

