def solution(n):
    answer = 0
    a, b = 1, 2
    for _ in range(n-1):
        a, b = b, a+b
    
    
    return a%1234567