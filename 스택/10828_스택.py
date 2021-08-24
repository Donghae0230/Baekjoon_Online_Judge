import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    print(cmd)
    if 'push' in cmd:
        stack.append(cmd[5:])
    elif cmd == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
