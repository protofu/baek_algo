import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
TRU = set(input().rstrip().split()[1:])

p_pers = []
rlt = []

for _ in range(m):
    p_pers.append(set(input().rstrip().split()[1:]))
    rlt.append(1)

for _ in range(m):
    for i, party in enumerate(p_pers):
        if TRU.intersection(party):
            rlt[i] = 0
            TRU = TRU.union(party)

print(sum(rlt))