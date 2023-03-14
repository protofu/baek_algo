def kaing(M, N, x, y):
    while x <= M * N:
        if not (x - y) % N:
            return x
        x += M
    return -1

N = int(input())
for _ in range(N):
    M, N, x, y = map(int, input().split())
    print(kaing(M, N, x, y))
    