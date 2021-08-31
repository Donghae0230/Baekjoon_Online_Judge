import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    func = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    queue = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if n == 0:  
        queue = deque()

    error = False
    cnt_R = 0
    for i in range(len(func)):
        if func[i] == 'D':
            if queue:
                if cnt_R % 2 == 1:
                    queue.pop() #매번 뒤집을 수 없으니까
                else:
                    queue.popleft()
            else:
                error = True
                break
        else:
            cnt_R += 1
    if error:
        print('error')
    else:
        if cnt_R % 2 == 1:
            queue.reverse()
        print('[' + ','.join(queue) + ']')

