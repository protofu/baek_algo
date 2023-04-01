import sys
input = sys.stdin.readline

cnt = ans = 0
stk = []
for _ in range(int(input())):
    n = int(input())
    # stk가 차있고 마지막 수가 n 보다 작으면 ans에 cnt만큼 추가
    while stk and stk[-1][0] < n:
        ans += stk.pop()[1]
    # 만약 stk 가 차있고 마지막 수가 n 과 동일하다면 cnt 초기화 후 ans 에 추가
    if stk and stk[-1][0] == n:
        cnt = stk.pop()[1]
        ans += cnt
        # stk가 차있으면 ans에 1 추가
        if stk:
            ans += 1
        stk.append([n, cnt + 1])

    else:
        if stk:
            ans += 1
        stk.append([n, 1])
print(ans)


