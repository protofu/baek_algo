N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
A_box = B_box = 0

def divide(x, y, N):
    global A_box
    global B_box
    A_cnt = B_cnt = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] == 1:
                A_cnt += 1
            else:
                B_cnt += 1
    if A_cnt == N**2:
        A_box += 1
    elif B_cnt == N**2:
        B_box += 1
    else:
        divide(x + N // 2, y + N // 2, N // 2)
        divide(x + N // 2, y, N // 2)
        divide(x, y + N // 2, N // 2)
        divide(x, y, N // 2)
        
divide(0, 0, N)
print(B_box)
print(A_box)

