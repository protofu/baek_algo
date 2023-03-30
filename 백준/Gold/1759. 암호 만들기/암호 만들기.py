import sys
input=sys.stdin.readline

def back_tracking(cnt, idx):
    if cnt == N:
        v, c = 0, 0

        for i in range(N):
            if rlt[i] in a:
                v += 1
            else:
                c += 1
        if v >= 1 and c >= 2:
            print("".join(rlt))
        return
    for i in range(idx, M):
        rlt.append(password[i])
        back_tracking(cnt+1, i+1)
        rlt.pop()


N, M = map(int, input().split())
password = sorted(list(input().split()))
rlt = []
a = ['a', 'e', 'i', 'o', 'u']
back_tracking(0, 0)