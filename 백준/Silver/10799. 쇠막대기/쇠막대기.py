laser = input()
laser = list(laser.replace('()', '#'))
cnt_list = []
cnt = 0

for ori in laser:
    if ori == '(':
        cnt_list.append(1)
    if ori == ')':
        cnt_list.pop()
    if ori == '#':
        cnt += len(cnt_list)

print(cnt + laser.count("("))