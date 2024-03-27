import sys
sys.setrecursionlimit(10**6)

def solution(n):
    answer = []
    def hanoi(start, target, mid, n):
        if n == 1:
            answer.append([start, target])
            return
        hanoi(start, mid, target, n-1)
        hanoi(start, target, mid, 1)
        hanoi(mid, target, start, n-1)

    hanoi(1, 3, 2, n)
    return answer