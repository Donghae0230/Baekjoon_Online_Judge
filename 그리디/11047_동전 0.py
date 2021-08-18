import sys
sys.stdin = open("input.txt","r")

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
cnt = 0
for i in reversed(data):
    if i <= k:
        cnt += k // i
        k %= i
print(cnt)

