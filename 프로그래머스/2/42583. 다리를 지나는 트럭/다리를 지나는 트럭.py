from collections import deque

def solution(bl, w, tw):
    answer = 0
    # 앞뒤로 작업할거라 deque
    bridge = deque([0]*bl)
    tw = deque(tw)
    wei = 0
    # 언제 끝날지 몰라서 while
    while tw:
        # 1초 +
        answer += 1
        # 먼저 공간을 만들어주고
        wei -= bridge.popleft()
        # 남은 트럭이 있으면서, 다리트럭 무게 + 지나갈 트럭 무게가 초과가 아니면 지나가기
        if wei+tw[0] <= w:
            wei += tw[0]
            bridge.append(tw.popleft())
        # 초과라면 다리 위 트럭 움직이기, 공간 다시 넣기
        else:
            bridge.append(0)
    answer += len(bridge)        
    return answer