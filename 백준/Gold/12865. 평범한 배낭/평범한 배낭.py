import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
lst = [[0,0]]
table = [[0]*(K+1) for _ in range(N+1)]
sub_ans = [0, 0]
for _ in range(N):
    W, V = map(int, input().split())
    sub_ans[0] += W
    sub_ans[1] += V
    lst.append([W, V])

for y in range(1, N+1):
    for x in range(1, K+1):
        w = lst[y][0]
        v = lst[y][1]
        if x < w:
            table[y][x] = table[y-1][x]
        else:
            table[y][x] = max(table[y-1][x], table[y-1][x-w] + v)
            
print(table[N][K])