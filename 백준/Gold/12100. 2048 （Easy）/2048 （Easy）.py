import copy

def left(sgame):
    for i in range(N):
        cnt = 0
        for j in range(1, N):
            if sgame[i][j]:
                tmp = sgame[i][j]
                sgame[i][j] = 0

                if not sgame[i][cnt]:
                    sgame[i][cnt] = tmp
                elif sgame[i][cnt] == tmp:
                    sgame[i][cnt] *= 2
                    cnt += 1
                else:
                    cnt += 1
                    sgame[i][cnt] = tmp
    return sgame

def right(sgame):
    for i in range(N):
        cnt = N - 1
        for j in range(N - 1, -1, -1):
            if sgame[i][j]:
                tmp = sgame[i][j]
                sgame[i][j] = 0

                if not sgame[i][cnt]:
                    sgame[i][cnt] = tmp
                elif sgame[i][cnt] == tmp:
                    sgame[i][cnt] *= 2
                    cnt -= 1
                else:
                    cnt -= 1
                    sgame[i][cnt] = tmp
    return sgame

def up(sgame):
    for j in range(N):
        cnt = 0
        for i in range(N):
            if sgame[i][j]:
                tmp = sgame[i][j]
                sgame[i][j] = 0

                if not sgame[cnt][j]:
                    sgame[cnt][j] = tmp
                elif sgame[cnt][j] == tmp:
                    sgame[cnt][j] *= 2
                    cnt += 1
                else:
                    cnt += 1
                    sgame[cnt][j] = tmp
    return sgame

def down(sgame):
    for j in range(N):
        cnt = N - 1
        for i in range(N - 1, -1, -1):
            if sgame[i][j]:
                tmp = sgame[i][j]
                sgame[i][j] = 0

                if not sgame[cnt][j]:
                    sgame[cnt][j] = tmp
                elif sgame[cnt][j] == tmp:
                    sgame[cnt][j] *= 2
                    cnt -= 1
                else:
                    cnt -= 1
                    sgame[cnt][j] = tmp
    return sgame

def back(cnt, game):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                if game[i][j] > ans:
                    ans = game[i][j]
        return

    for i in range(4):
        sandGame = copy.deepcopy(game)
        if not i:
            back(cnt+1, left(sandGame))
        elif i == 1:
            back(cnt+1, right(sandGame))
        elif i == 2:
            back(cnt+1, up(sandGame))
        else:
            back(cnt+1, down(sandGame))

N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
ans = 0

back(0, game)
print(ans)
