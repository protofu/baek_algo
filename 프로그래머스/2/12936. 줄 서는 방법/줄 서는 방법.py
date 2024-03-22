import math

def solution(n, k):
    answer = []
    num_lst = [i for i in range(1, n+1)]
    
    while n != 0:
        idx = (k-1)//math.factorial(n-1)
        answer.append(num_lst.pop(idx))
        k = k % math.factorial(n-1)
        n -= 1

    return answer