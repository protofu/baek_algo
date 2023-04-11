n, s = map(int, input().split())
data = list(map(int, input().split()))
tmp_sum = end = start = 0
ans = 1e9

while True:
    if tmp_sum >= s:

        ans = min(ans, end - start)  # 매 순간 최소 길이로 초기화
        tmp_sum -= data[start]  # 현재 수열의 시작 위치 값을 빼주고
        start += 1  # 현재 수열의 시작 위치를 한 계단 앞으로 이동

    # left부터 right까지 수열의 합이 s를 넘지 않는다면
    else:
        # 맨 끝 위치가 n과 같다면 반복을 멈춰준다. s를 넘는 수열을 만들 수 없기 때문
        if end == n:
            break

        tmp_sum += data[end]  # 현재 수열의 마지막 위치 값을 더해주고
        end += 1  # 수열의 마지막 위치를 한 계단 앞으로 이동

print(0) if ans == 1e9 else print(ans)