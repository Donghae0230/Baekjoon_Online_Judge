import sys
sys.stdin = open("input.txt", "r")

n = int(input())
data = [0] * n
for i in range(n):
    data[i] = list(map(int, input().split()))
cnt = 0
rank = []
for i in range(n):
    for j in range(n):
        if j == i:
            continue
        elif data[j][0] > data[i][0] and data[j][1] > data[i][1]:
            cnt += 1
    rank.append(cnt+1)
    cnt = 0
print(*rank)
