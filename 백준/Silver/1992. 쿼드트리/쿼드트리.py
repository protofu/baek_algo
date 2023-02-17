N = int(input())
paper = [list(input()) for _ in range(N)]
box = []

def divide(x, y, N):
    A_cnt = B_cnt = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] == '1':
                A_cnt += 1
            else:
                B_cnt += 1
    if A_cnt == N**2:
        box.append(1)
    elif B_cnt == N**2:
        box.append(0)
    else:
        box.append('(')
        divide(x, y, N // 2)
        divide(x, y + N // 2, N // 2)
        divide(x + N // 2, y, N // 2)
        divide(x + N // 2, y + N // 2, N // 2)
        box.append(')')


divide(0, 0, N)
print(*box, sep='')


