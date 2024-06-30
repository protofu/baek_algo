n, k = map(int, input().split())
# if 7 --> 0 1 2 3 4 5 6 7
era_list = [False, False] + ([True] * (n-1))
cnt = 1
# 소수를 찾아보자!
for i in range(2, n+1):  
    for m in range(i, n+1 ,i):
        if era_list[m] == 1:
            if cnt == k:
                print(m)
            cnt += 1
                
        era_list[m] = 0