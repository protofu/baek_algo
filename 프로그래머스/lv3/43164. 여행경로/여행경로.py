def solution(tickets):
    answer = []
    routes = {}
    for ticket in tickets:
        if ticket[0] not in routes:
            routes[ticket[0]] = []
        routes[ticket[0]].append(ticket[1])
        routes[ticket[0]].sort()

    stack = ["ICN"]
    while stack:
        top = stack[-1]
        if top not in routes or not routes[top]:
            answer.append(stack.pop())
        else:
            stack.append(routes[top].pop(0))

    return answer[::-1]
