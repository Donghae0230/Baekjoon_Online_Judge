import sys
sys.stdin = open("input.txt", "r")

def cutIron(bar):
    lst = []
    res = 0
    for i in range(len(bar)):
        if bar[i] == '(':
            lst.append('(')
        elif bar[i] == ')':
            if bar[i-1] == '(':
                res += len(lst) - 1
                lst.pop()
            else:
                res += 1
                lst.pop()
    return res
bar = list(sys.stdin.readline())
print(cutIron(bar))

