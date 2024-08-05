def solution(tickets):
    answer = []
    routes = {}
    # 경로 딕셔너리로 정리
    # 키 : 출발 || 요소 : 도착
    for ticket in tickets:
        if ticket[0] not in routes:
            routes[ticket[0]] = []
        routes[ticket[0]].append(ticket[1])
        # 사전순 정렬
        routes[ticket[0]].sort()
    # 시작을 ICN으로
    stack = ["ICN"]
    # stack이 비었단건 다 탐색하고 끝낸것
    while stack:
        # stack의 top은 무조건 도착점이니까 도착점을 시작으로 잡고
        top = stack[-1]
        # top에서부터 갈 수 있는 곳이 없으면 answer에 넣기
        if top not in routes or not routes[top]:
            answer.append(stack.pop())
        # 그게 아니라면 stack에 경로 추가
        else: 
            stack.append(routes[top].pop(0))
    # 역순으로 저장했으니 역순으로 출력
    return answer[::-1]