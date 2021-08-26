import sys
sys.stdin = open("input.txt", "r")

stack = []
while True:
    s = input()
    if s == '.':
        break
    for i in s:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':  
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
    print('yes') if len(stack) == 0 else print('no')
    stack = []