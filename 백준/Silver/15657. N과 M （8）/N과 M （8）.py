# 백트래킹
def back(start):
    # m개가 되면 도출
    if len(ans) == m:
        print(*ans)
        return
    # 백트래킹 로직
    # 이전 숫자만 넣지 않으면 문제없기에 start 인덱스 지정
    for i in range(start, n):
        ans.append(lst[i])
        back(i)
        ans.pop()

n, m = map(int, input().split())
# 입력받으면서 오름차순 정렬
lst = sorted(list(map(int, input().split())))
ans = []
back(0)