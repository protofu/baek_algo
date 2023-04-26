def dfs(score, cnt):
    global flag, ans
    if cnt == 11:
        ans = max(ans, score)
        return

    for i in range(11):
        if pos[cnt][i] and not visited[i]:
            visited[i] = True
            dfs(score+pos[cnt][i], cnt+1)
            visited[i] = False


for _ in range(int(input())):
    pos = [[0]*11 for _ in range(11)]
    visited = [0] * 11
    flag = ans = 0
    for i in range(11):
        pos[i] = list(map(int, input().split()))
    dfs(0, 0)
    print(ans)
