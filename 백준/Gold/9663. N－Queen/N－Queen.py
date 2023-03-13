import sys
input = sys.stdin.readline

def is_promising(S):
    for i in range(S):
        if l[S] == l[i] or abs(l[S]-l[i]) == S-i:
            return False
    return True

def Queen(S):
    global ans
    if S == N: # 끝줄까지 탐색 했으면
        ans += 1
    else:
        for i in range(N):
            l[S] = i
            if is_promising(S):
                Queen(S+1)
N = int(input())

ans = 0
l = [0]*N

Queen(0)
print(ans)