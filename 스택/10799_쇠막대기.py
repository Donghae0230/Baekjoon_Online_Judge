import sys
sys.stdin = open("input.txt", "r")

def cutIron(bar):
    stack = []
    cnt = 0
    for i in range(len(bar)):
        if bar[i] == '(':
            stack.append('(')
        elif bar[i] == ')':
            if bar[i-1] == '(':
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1
    return cnt
bar = list(sys.stdin.readline())
print(cutIron(bar))