# a 시간당 피로도 b 시간당 처리량 c 시간당 회복 m 최대 피로도
a, b, c, m = map(int, input().split())
works = 0
tired = m
# 일 자체가 피로도보다 높다면 바로 종료
if a > m:
    pass
else:
    # 24시간
    for _ in range(24):
        # 남은 피로도보다 일 피로도가 낮거나 같다면 일하기
        if tired >= a:
            works += b
            tired -= a
        # 남은 피로도보다 일 피로도가 높으면 휴식
        elif tired < a:
            # 휴식 후 피로도가 최대보다 낮거나 같다면 그대로
            if tired + c <= m:
                tired += c
            # 휴식 후 피로도가 최대보다 높으면 m으로 고정
            else:
                tired = m
print(works)
