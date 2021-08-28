import sys
sys.stdin = open("input.txt", "r")

from collections import deque

n, k = map(int, input().split())
queue = deque()
res = [0] * n
for i in range(1, n+1):
    queue.append(i)
for i in range(n):
    queue.rotate(-(k-1))
    res[i] = str(queue.popleft())
print('<' + ', '.join(res) + '>')

