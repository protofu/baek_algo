import sys
sys.setrecursionlimit(10**6)

def solution(n):
    answer = []
    def hanoi(start, tmp, target, n):
        if n == 1:
            answer.append([start, target])
            return
        hanoi(start, target, tmp, n-1)
        hanoi(start, tmp, target, 1)
        hanoi(tmp, start, target, n-1)
    
    hanoi(1, 2, 3, n)
    
    return answer