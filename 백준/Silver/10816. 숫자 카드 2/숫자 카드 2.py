N = int(input())
cards = list(map(int, input().split()))
M = int(input())
sel_cards = list(map(int, input().split()))
rlt_d = {i : 0 for i in sel_cards}

for i in cards:
    if i in rlt_d.keys():
        rlt_d[i] += 1

for i in sel_cards:
    print(rlt_d[i], end=' ')