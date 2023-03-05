	
14

#####################################################################################
# 오목인지 아닌지 판별하는 함수
def checK(y, x, n):
    cnt = 1
    global win
    global po
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if checkerboard[ny][nx] == n and checkerboard[y-dy[i]][x-dx[i]] != n:
            while checkerboard[ny][nx] == n:
                cnt += 1
                ny, nx = ny + dy[i], nx + dx[i]
    #########################################
        if cnt == 5: # 오목 이라면 그 돌을 저장
            win = n
            if x > nx: # 오목이 된 돌에서 양끝 돌의 가로값 비교 후 작은 값을 넣기
                po = (ny-dy[i], nx-dx[i])
            else:
                po = (y, x)
            return
    ##########################################
        else:
            cnt = 1

##########################################################################################
# 메인 함수, 체크보드는 범위지정이 귀찮아 좌우양옆 한칸씩 더 줬습니다.
checkerboard = [[0]*21] + [[0] + list(map(int, input().split()))+ [0] for _ in range(19)] + [[0]*21]
win = flag = 0
po = ()
for y in range(1, 20):
    for x in range(1, 20):
        if checkerboard[y][x]:
            n = checkerboard[y][x]
            checK(y, x, n)
        if win and po:
            flag = 1
            print(win)
            print(*po)
            break
    if flag:
        break
if not flag: # flag를 통해 반복문이 깨진다는 소리는 값이 있다는것, 즉 flag가 0 이면 무조건 무승부
    print(0)

#############################################################################################