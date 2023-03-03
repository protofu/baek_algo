from collections import Counter as cou
import sys
input = sys.stdin.readline
N = int(input())
num_lst = [int(input()) for _ in range(N)]
num_lst.sort()
dic = cou(num_lst).most_common(2)
if sum(num_lst)/N < 0:
    a = -round(abs(sum(num_lst))/N)
else:
    a = round(abs(sum(num_lst)) / N)
print(a)
b = num_lst[N//2]
print(b)
if len(dic) == 1:
    print(dic[0][0])
else:
    if dic[0][1] > dic[1][1]:
        print(dic[0][0])
    else:
        print(dic[1][0])
d = abs(num_lst[0] - num_lst[-1])
print(d)