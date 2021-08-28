import sys
sys.stdin = open("input.txt", "r")

n = int(input())
target = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
res = []
for i in range(1, n+1):
    stack.append(i)
    res.append('+')
    while stack and target:
        if stack[-1] == target[0]:
            stack.pop()
            res.append('-')
            del target[0]
        else:
            break
if target:
    print('NO')
else:
    for i in range(len(res)):
        print(res[i])

