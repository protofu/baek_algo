n, m, inven = map(int, input().split())
mine = sum([list(map(int, input().split())) for _ in range(n)], [])
mine_high = max(mine)
mine_low = min(mine)
time = float('inf')
lend = 0
# 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. -> 2초
# 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. -> 1초
# 대충 땅크기 250*250, 땅최대 0-256, 1610만회 -> 1초 안걸림 0.8초쯤?
for standard in range(mine_low, mine_high+1):
    dig = fill = tmp_time = 0
    for ground in mine:
        # 기준보다 낮은 땅이면
        if ground < standard:
            # 얼마나 채워야할지 측정
            fill += standard - ground
        # 기준보다 높은 땅이면
        elif ground > standard:
            # 얼마나 파야할지 측정
            dig += ground - standard

    # 기준에 대해 모두 측정 후 판단

    # 채워야 할 블록 갯수가 inven에 있는것 보다 많다면 그냥 통과
    # 땅을 파면 블록이 생기니까 fill - dig
    if inven >= fill - dig:
        # 해당 기준에 대한 시간 측정
        tmp_time = (fill + dig*2)
        # 원래 시간보다 덜 걸린다면 초기화
        if tmp_time <= time:
            time = tmp_time
            lend = standard

print(time, lend)
