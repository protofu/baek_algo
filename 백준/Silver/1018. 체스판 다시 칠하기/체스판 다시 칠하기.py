y, x = map(int, input().split())
board = [input() for _ in range(y)]
Min = 64
for i in range(y-7):
    for j in range(x-7):
        cnt1 = cnt2 = 0
        for r in range(i, i+8):
            for c in range(j, j+8):
                if (r+c)%2 == 0:
                    if board[r][c] != 'W':
                        cnt1 += 1
                    if board[r][c] != 'B':
                        cnt2 += 1
                else:
                    if board[r][c] != 'B':
                        cnt1 += 1
                    if board[r][c] != 'W':
                        cnt2 += 1
        if Min > min(cnt1, cnt2):
            Min = min(cnt1, cnt2)
print(Min)