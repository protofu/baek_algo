import sys
input = sys.stdin.readline
k, n = map(int,input().split())

lan_list =[int(input()) for i in range(k)]
sear = 1
end = max(lan_list)
while sear <= end:
    half = (sear + end) // 2
    cnt = 0
    for one_lan in lan_list:
        cnt += one_lan // half
    if cnt>=n:
        sear = half + 1
    else:
        end = half - 1
print(end)


