for _ in range(int(input())):
    ans = 1
    rlt = list(map(float, input().split()))
    for i in rlt:
        ans *= i
    print(f'${round(ans, 2):.2f}')
