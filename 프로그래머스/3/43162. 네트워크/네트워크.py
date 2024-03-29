def solution(n, computers):
    answer = 0
    visit = [False] * n
    
    def dfs(node):
        visit[node] = True
        for i in range(n):
            if node != i and computers[node][i] and not visit[i]:
                dfs(i)
            
    for i in range(n):
        if not visit[i]:
            dfs(i)
            answer += 1
    return answer

