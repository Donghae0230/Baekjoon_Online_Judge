import sys

k = int(sys.stdin.readline())
data = []
for _ in range(k):
    num = int(sys.stdin.readline().rstrip())
    data.pop() if num == 0 else data.append(num)
print(sum(data))
