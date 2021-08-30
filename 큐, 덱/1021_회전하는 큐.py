import sys
sys.stdin = open("input.txt", "r")

from collections import deque

n, m = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
idx = list(map(int, input().split()))
cnt = 0
while idx:
    if idx[0] == queue[0]:
        queue.popleft()
        del idx[0]
    elif queue.index(idx[0]) >= len(queue)/2:
        queue.rotate(1)
        cnt += 1
    elif queue.index(idx[0]) < len(queue)/2:
        queue.rotate(-1)
        cnt += 1
print(cnt)
