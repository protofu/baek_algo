
def solve_sudoku(fill):
    # 다 채웠으면 출력하고 코드 종료
    if fill == len(zeros):
            for s in sudoku:
                print(*s)
            exit(0)
    y, x = zeros[fill]
    for number in range(1, 10):
        # 해당 숫자가 가로 세로 3x3에 없다면 백트래킹
        if not su_col[x][number] and not su_row[y][number] and not su_3x3[y//3][x//3][number]:
            sudoku[y][x] = number
            su_col[x][number] = su_row[y][number] = su_3x3[y//3][x//3][number] = True
            solve_sudoku(fill+1)
            su_col[x][number] = su_row[y][number] = su_3x3[y//3][x//3][number] = False
            sudoku[y][x] = 0

sudoku = [list(map(int, input().split())) for _ in range(9)]
# 후보 체크를 위한 2차원 가로세로 리스트
su_col = [[False] * 10 for _ in range(9)]
su_row = [[False] * 10 for _ in range(9)]
# 후보 체크를 위한 3차원 3x3 box 리스트
su_3x3 = [[[False] * 10 for _ in range(9)] for _ in range(3)]

zeros = []
for y in range(9):
    for x in range(9):
        num = sudoku[y][x]
        # 0이면 좌표 추가
        if num == 0:
            zeros.append((y, x))
        # 아니라면 방문 도장
        else:
            su_col[x][num] = su_row[y][num] = su_3x3[y//3][x//3][num] = True
solve_sudoku(0)

# ==========================================================================================
# # 가로세로 체크
# def check_col(y, x, nums):
#     for i in range(9):
#         num_col = sudoku[i][x]
#         if num_col != 0:
#             nums.discard(num_col)
#         num_row = sudoku[y][i]
#         if num_row != 0:
#             nums.discard(num_row)
#     return
#
# def check_3x3(y, x, nums):
#     # 3의 몫으로 나누고 3을 곱한 이유는 3x3 박스의 좌상단 부터 탐색하기 위함
#     # 예를들어 5라면 5//3 * 3= 3 -> 5의 좌상단은 3 (index 기준)
#     box_y, box_x = y//3 * 3, x//3 * 3
#     for i in range(box_y, box_y+3):
#         for j in range(box_x, box_x+3):
#             # 후보 리스트에서 해당 숫자 삭제
#             num = sudoku[i][j]
#             if num != 0:
#                 nums.discard(num)
#     return
#
# def solve_sudoku(fill):
#     # 모두 채웠으면 스도쿠 출력하고 코드 종료
#     if fill == len(zeros):
#         for s in sudoku:
#             print(*s)
#         exit(0)
#     # 0인 좌표를 받아오고
#     y, x = zeros[fill]
#     # 1~9 까지의 리스트 하나 만들고
#     nums = {i for i in range(1, 10)}
#     # 가로, 세로, 3x3 체크, 후보에서 제외하기
#     check_col(y, x, nums)
#     check_3x3(y, x, nums)
#     # 후보 없으면 그냥 return
#     if not nums:
#         return
#     # 남은 후보들을 넣으면서 백트래킹
#     for n in nums:
#         sudoku[y][x] = n
#         solve_sudoku(fill+1)
#         sudoku[y][x] = 0
#
# sudoku = [list(map(int, input().split())) for _ in range(9)]
# zeros = [(y, x) for x in range(9) for y in range(9) if sudoku[y][x] == 0]
# solve_sudoku(0)
#
