import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def union(a, b, k):
    aroot = parent[a]
    broot = parent[b]
    if aroot != broot:
        parent[broot] = aroot
        wei[broot] = wei[a] + k - wei[b]

def find(x):
    if x == parent[x]:
        return x
    else:
        tmp = find(parent[x])
        wei[x] += wei[parent[x]]
        parent[x] = tmp
        return parent[x]

while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    parent = [i for i in range(N+1)]
    wei = [0] * (N+1)
    for _ in range(M):
        com, *lst = map(str, input().split())
        find(int(lst[0]))
        find(int(lst[1]))
        if com == '!':
            union(int(lst[0]), int(lst[1]), int(lst[2]))
        else:
            if parent[int(lst[0])] == parent[int(lst[1])]:
                print(wei[int(lst[1])] - wei[int(lst[0])])
            else:
                print('UNKNOWN')