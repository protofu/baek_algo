def solution(people, limit):
    answer = 0
    # 처음 참 고민했는데 2명씩이란 말을 늦게 봄
    # 무게 낮은 값부터 정렬
    people.sort()
    l = len(people)
    start = 0
    end = l-1
    # 모두 보트를 탈때까지
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
        
    return answer