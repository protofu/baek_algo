def I_want_a_solve_platinum(N):
    a=1
    for i in range(2, N+1):
        if not N%i:
            a+=i
    return a


print(I_want_a_solve_platinum(int(input()))*5-24)