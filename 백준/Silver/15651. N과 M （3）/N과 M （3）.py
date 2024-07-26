n, m = map(int, input().split())
ans = []
# 백트래킹
def back():
    # 출력 시점
    if len(ans) == m:
        print(*ans)
        return
    # 하나씩 순회하면서 백트래킹 넣기
    for i in range(1, n+1):
        # 메인의 for문 안 동작과 동일
        ans.append(i)
        back()
        ans.pop()
back()