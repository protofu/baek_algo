def isPromising(cnt):
    if cnt == len(zero):
        for i in sudoku:
            print(*i, sep="")
        exit()
    else:
        y, x = zero[cnt]
        posiY, posiX = y//3, x//3
        sandNum = num[:]
        for i in range(3*posiY, (posiY+1)*3):
            for j in range(3*posiX, (posiX+1)*3):
                if sudoku[i][j] in sandNum:
                    sandNum.remove(sudoku[i][j])

        for i in range(9):
            if sudoku[y][i] in sandNum:
                sandNum.remove(sudoku[y][i])
            if sudoku[i][x] in sandNum:
                sandNum.remove(sudoku[i][x])
        for i in sandNum:
            sudoku[y][x] = i
            isPromising(cnt+1)
        sudoku[y][x] = 0


sudoku = [list(map(int, list(input()))) for _ in range(9)]
num = [i for i in range(1, 10)]
zero = [(j, i) for j in range(9) for i in range(9) if not sudoku[j][i]]

isPromising(0)
