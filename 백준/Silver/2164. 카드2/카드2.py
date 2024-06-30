from collections import deque

n = int(input())
# 앞뒤로 입출력 위해 deque로 생성
q = deque([i for i in range(n, 0, -1)])
# 반복문 카드가 1개 남을때 까지
while len(q) != 1:
    # 맨위 첫장 빼고
    q.pop()
    # 그 다음장 뺀걸 가장 밑으로
    q.appendleft(q.pop())
print(q[0])