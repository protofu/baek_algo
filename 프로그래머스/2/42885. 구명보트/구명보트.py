def solution(people, limit):
    answer = 0
    # 처음 참 고민했는데 2명씩이란 말을 늦게 봄
    # 무게 낮은 값부터 정렬
    people.sort()
    l = len(people)
    start = 0       # 시작 포인트
    end = l-1       # 끝 포인트
    # 모두 보트를 탈때까지 투포인터를 돌려보겠쉼다
    # 2명 탄것만 셀거라서 = 은 안붙임
    while start < end:
        # 처음과 끝 2명이 된다면
        if people[start] + people[end] <= limit:
            start += 1
            answer += 1
        # 어찌되든 끝점은 줄어야함 혼자 타거나 같이 타거나
        end -= 1
    # 같이 탄 보트만 answer에 넣었으니 총 인원에서 빼주면 된다.
    return l - answer