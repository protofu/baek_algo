N, M, L = map(int, input().split())
cnt = 0
if M == 1:
    print(0)
else:
    lst = [0] * (N+1)
    S = 1
    while lst[S] != M:
        cnt += 1
        lst[S] += 1
        if lst[S] == M:
            break
        if lst[S] % 2:
            S += L
            if S > N:
                S -= N
        else:
            S -= L
            if S < 1:
                S += N
    print(cnt-1)