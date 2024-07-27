# 백트래킹
def back():
    # 수열의 길이가 조건에 맞으면 출력
    if len(ans) == m:
        print(*ans)
        return
    # 순회하며 ans에 넣기
    for i in lst:
        if i in ans: continue
        ans.append(i)
        back()
        ans.pop()

n, m = map(int, input().split())
# 입력과 오름차순 정렬
lst = sorted(list(map(int, input().split())))
ans = []
# 백트래킹 시작
back()
