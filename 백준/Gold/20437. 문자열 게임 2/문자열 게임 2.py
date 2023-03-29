import sys
input=sys.stdin.readline

for _ in range(int(input())):
    alpha = list(input().strip())
    history = [[] for _ in range((ord('z') - ord('a') + 1))] # 알파벳 배열

    for i in range(len(alpha)):
        history[ord(alpha[i]) - ord('a')].append(i) #index저장

    K = int(input())
    short, long = 10000, 0

    for i in range(len(history)):
        if len(history[i]) >= K:
            for j in range(len(history[i]) - K + 1):
                tmp = history[i][j+K-1] - history[i][j] + 1
                short = min(short, tmp)
                long = max(long, tmp)

    if short == 10000 and long == 0:
        print(-1)
    else:
        print(short, long)