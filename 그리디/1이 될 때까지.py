import sys
sys.stdin = open("input.txt","r")   

n, k = map(int, input().split())
cnt = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n = n // k
        cnt += 1
    else:
        n = n - 1
        cnt += 1
print(cnt)