# n 학생수 / lost 잃어버린 / re 여분이 있는
def solution(n, lost, reserve):
    answer = 0
    visited = [0] + [1]*(n) + [0]
    
    # 체육복 챙겨넣기
    for i in range(1, n+1):
        if i in reserve:
            visited[i] +=1
        if i in lost:
            visited[i] -= 1
        
    print(visited)  
    # 1번 학생부터 순차로
    for i in range(1, n+1):
        if visited[i] == 0:
            if visited[i-1] == 2:
                visited[i] += 1
                visited[i-1] -= 1
            elif visited[i+1] ==2:
                visited[i] += 1
                visited[i+1] -= 1
        if visited[i] > 0:
            answer+= 1
            
            
            
    return answer