import sys
sys.setrecursionlimit(10**6)

def solution(n):
    answer = []
    # 재귀 구현
    def hanoi(start, tmp, target, n):
        # 남은 원판이 하나라면 그 원판의 경로 저장
        if n == 1:
            answer.append([start, target])
            return
        # 1번 기둥을 시작(start)으로 잡고, 2번 기둥을 목표(target)로 설정 후 1개씩 이동
        hanoi(start, target, tmp, n-1)
        # 마지막 원판은 3번 기둥으로(target) 설정
        hanoi(start, tmp, target, 1)
        # 남은 2번기둥(tmp)를 시작으로 두고 목표인 3번기둥(target)으로 이동시키기
        hanoi(tmp, start, target, n-1)
    
    hanoi(1, 2, 3, n)
    return answer
