def back(p_score, posi):
    global ans
    # 종료 조건 -> posi가 11까지 갔단건 모든 포지션을 고려했단 말
    if posi == 11:
        # 원래 포지션스코어와 현재 포지션 스코어중 큰걸로 초기화
        ans = max(ans, p_score)
        return
    # 11개의 포지션 탐색
    for i in range(11):
        # 포지션 스코어가 0이면 or 이미 더해진 포지션 스코어라면 패스
        if players[posi][i] == 0 or visit[i]: continue
        visit[i] = True
        back(p_score+players[posi][i], posi+1)
        visit[i] = False

for _ in range(int(input())):
    players = [list(map(int, input().split())) for _ in range(11)]
    visit = [False] * 11
    ans = 0
    back(0, 0)
    print(ans)