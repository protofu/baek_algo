import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    check, a, b = map(int, input().split())
    if not check:
        union(a, b)
    else:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')