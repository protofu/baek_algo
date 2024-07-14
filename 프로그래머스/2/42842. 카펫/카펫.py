def solution(brown, yellow):
    answer = []
    xy = []
    # 전체 블록 수
    blocks = brown + yellow
    # 가능한 x, y 조합 찾기
    for i in range(3, blocks//3+1):
        # 가능한 x, y 중 가로(x)가 큰것만
        if blocks%i == 0 and i >= blocks//i:
            # 조합 중 x-2 * y-2 가 yellow인것만 골라내기
            if (i-2)*(blocks//i-2) == yellow:
                answer.append(i)
                answer.append(blocks//i)
                break

    return answer
