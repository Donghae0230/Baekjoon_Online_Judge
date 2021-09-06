import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

arr = [0] 
tmp = 0
for i in range(n):
    tmp += data[i] 
    arr.append(tmp)
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(arr[j] - arr[i-1])