import sys
from collections import deque
input = sys.stdin.readline

W = list(input().rstrip())
S = deque(input().rstrip())
N = int(input())
LS = []
RS = []
cnt = 0
for _ in range(N):
    command = input().rstrip()
    if command == 'L':
        while S:
            LS.append(S.popleft())
            if len(LS) >= len(W) and LS[-len(W):] == W:
                cnt += 1
                for _ in range(len(W)):
                    LS.pop()
                break
    elif command == 'R':
        while S:
            RS.append(S.pop())
            if len(RS) >= len(W) and RS[-len(W):] == W[::-1]:
                cnt += 1
                for _ in range(len(W)):
                    RS.pop()
                break
    if not S:
        while LS:
            RS.append(LS.pop())
            if len(RS) >= len(W) and RS[-len(W):] == W[::-1]:
                cnt += 1
                for _ in range(len(W)):
                    RS.pop()
                break
if S:
    while S:
        RS.append(S.pop())
if LS:
    while LS:
        RS.append(LS.pop())

ans = "".join(RS[::-1])
print(cnt)
print(ans)
if "".join(W) in ans:
    print('You Lose!')
else:
    print('Perfect!')
