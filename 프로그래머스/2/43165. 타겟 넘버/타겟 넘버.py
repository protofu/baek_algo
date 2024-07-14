def solution(numbers, target):
    answer = 0
    # 재귀 dfs 탐색
    def dfs(idx, num):
        # 인덱스가 초과할때까지 ex) 4번인덱스 까지 있으면 5번에서 결과 도출할 수 있도록
        if idx == len(numbers):
            # 타겟 넘버와 같다면 +1
            if num == target:
                nonlocal answer 
                answer += 1
            return
        # 더하고 빼는 동작으로 재귀 2개 생성
        dfs(idx+1, num+numbers[idx])
        dfs(idx+1, num-numbers[idx])
    # 초기값으로 시작
    dfs(0, 0)
    return answer