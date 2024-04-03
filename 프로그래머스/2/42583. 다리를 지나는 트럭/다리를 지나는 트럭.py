from collections import deque

def solution(bridge_length, weight, truck_weights):
    # bridge_length 최대 다리위 트럭 수, weight 하중, truck_weights 트럭별 무게
    answer = 0
    truck_weights = deque(truck_weights)
    queue = deque([0]*bridge_length)
    wei = 0
    while truck_weights:
        answer += 1
        wei -= queue.popleft()
        if wei + truck_weights[0] <= weight:
            wei += truck_weights[0]
            queue.append(truck_weights.popleft())
        else:
            queue.append(0)
        
    answer += len(queue)
        
    return answer