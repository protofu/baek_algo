from collections import Counter as Cou
import sys

rlt = []
cnt = 0
n, m = map(int, input().split())
lst = [input() for _ in range(n+m)]
n_lst = Cou(lst).most_common()
for i in n_lst:
    if i[1] == 2:
        rlt.append(i[0])
        cnt += 1
    else:
        break
rlt.sort()
print(cnt)
for i in rlt:
    print(i)