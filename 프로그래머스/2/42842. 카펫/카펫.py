def solution(brown, yellow):
    answer = []
    xy = []
    blocks = brown + yellow
    for i in range(3, blocks//3+1):
        if blocks%i == 0 and i >= blocks//i:
            xy.append([i, blocks//i])
    
    for x, y in xy:
        if (x-2)*(y-2) == yellow:
            answer.append(x)
            answer.append(y)
    
    print(answer)
    return answer