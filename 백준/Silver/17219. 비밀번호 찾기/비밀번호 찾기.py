import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    a, b = list(map(str, input().split()))
    dic[a] = b
for _ in range(M):
    print(dic[input().strip()])
