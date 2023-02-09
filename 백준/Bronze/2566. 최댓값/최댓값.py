num_list = [list(map(int, input().split())) for _ in range(9)]
pix = [0, 0, 0]
for i in range(9):
    for j in range(9):
        if pix[0] < num_list[i][j]:
            pix = [num_list[i][j], i, j]
                    
print(pix[0])
print(pix[1]+1, pix[2]+1)
    
