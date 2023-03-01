n = int(input())
lst = list(map(int, input().split()))
cnt = 1
cnt_max = 0
if n > 1:
    for i in range(1, n):
        if lst[i] >= lst[i-1]:
            cnt += 1
        else:
            cnt = 1
        if cnt_max < cnt:
            cnt_max = cnt
    cnt = 1
    for i in range(1, n):
        if lst[i] <= lst[i-1]:
            cnt += 1
        else:
            cnt = 1
        if cnt_max < cnt:
            cnt_max = cnt
else:
    cnt_max = 1
print(cnt_max)