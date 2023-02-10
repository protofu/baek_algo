import sys
input = sys.stdin.readline

n = list(input().strip())
n.sort()
for i in range(len(n)-1, -1, -1):
    print(n[i], end='')