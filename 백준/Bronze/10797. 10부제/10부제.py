t=int(input())
cnt = 0
lst = list(map(int, input().split()))
for i in lst:
    if t == i:
        cnt += 1
print(cnt)