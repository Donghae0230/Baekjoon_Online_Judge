import sys
sys.stdin = open("input.txt", "r")

def cutIron(bar):
    bar = bar.replace('()','-')
    tmp = 0
    res = 0
    for i in bar:
        if i == '(':
            tmp += 1
            res += 1
        elif i == '-':
            res += tmp
        else:
            tmp -= 1
    return res
bar = sys.stdin.readline()
print(cutIron(bar))