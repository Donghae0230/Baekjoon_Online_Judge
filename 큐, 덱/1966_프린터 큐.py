from collections import deque

case = int(input())
for _ in range(case):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    idx_que = deque(list(range(n))) #인덱스 값 담은 queue를 같이 계산
    cnt = 0 #출력 카운트
    while queue:
        if queue[0] == max(queue):
            cnt += 1
            queue.popleft()
            if idx_que.popleft() == m:
                print(cnt)
        else:
            queue.append(queue.popleft())
            idx_que.append(idx_que.popleft())