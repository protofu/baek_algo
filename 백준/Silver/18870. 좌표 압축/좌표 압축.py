import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
lst = list(map(int, input().split()))
sort_lst = sorted(set(lst))
dic = {i : v for v, i in enumerate(sort_lst)}
for i in lst:
    print(f'{dic[i]} ')
