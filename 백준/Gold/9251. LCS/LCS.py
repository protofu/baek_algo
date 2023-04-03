S = input()
W = input()

s, w = len(S), len(W)
visited = [0]*w

for i in range(s):
    cnt = 0
    for j in range(w):
        if cnt < visited[j]:
            cnt = visited[j]
        else:
            if S[i] == W[j]:
                visited[j] = cnt + 1
print(max(visited))
