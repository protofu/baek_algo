def queen(s, n, l):
    # 끝줄까지 탐색했으면 return 1
    if s == n:
        return 1
    answer = 0
    # 퀸 채워넣기
    for i in range(n):
        l[s] = i
        # 가능한지 체크
        for r in range(s):
            # 같은줄 or 대각선이면 실패
            if l[r] == l[s] or abs(l[s] - l[r]) == s - r:
                break
        # 모두 통과면 다음
        else:
            answer += queen(s + 1, n, l)
    return answer

def solution(n): 
    return queen(0, n, [0] * n)