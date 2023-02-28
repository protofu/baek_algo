N = int(input())
paper = [[0]*101 for _ in range(101)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):            # 도화지 채우기
        paper[i][x:x + 10] = [1] * 10   # 리스트 슬라이싱으로 채우기

for y in range(101):
    for x in range(101):
        if paper[y][x]:                 # 1이라면
            cnt = 0
            for i in range(4):          # 델타탐색
                ny, nx = y + dy[i], x + dx[i]
                if 101 > ny >= 0 and 101 > nx >= 0 and paper[ny][nx]:   #범위안에서 1이면
                    cnt += 1                                # 카운트
            if cnt == 3:    # 3이라면 선
                ans += 1
            elif cnt == 2:  # 2라면 꼭지점
                ans += 2    # 꼭지점은 2번 세어줘야함 방향이 바뀌며 2번 세어주기 때문

print(ans)