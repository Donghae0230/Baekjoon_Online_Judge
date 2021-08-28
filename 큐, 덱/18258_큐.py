import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
queue = deque()
for _ in range(n):
    cmd = sys.stdin.readline().split()
    # print('cmd: ' + cmd[0])
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(0) if queue else print(1)
    elif cmd[0] == 'front':
        print(queue[0]) if queue else print(-1)
    elif cmd[0] == 'back':
        print(queue[-1]) if queue else print(-1)
        
