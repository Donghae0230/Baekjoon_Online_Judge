import sys
sys.stdin = open("input.txt", "r")

s = sys.stdin.readline().strip()
bomb = list(sys.stdin.readline().strip())

stack = []
for i in range(len(s)):
    stack.append(s[i])
    if stack[-len(bomb):] == bomb:
        del stack[-len(bomb):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')


