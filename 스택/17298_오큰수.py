import sys
sys.stdin = open("input.txt", "r")
      
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = [0]     #인덱스에 대한 stack
res  = [-1] * n
for i in range(1, n):
    while stack and arr[i] > arr[stack[-1]]:
        res[stack.pop()] = arr[i]
    stack.append(i)
print(*res)


