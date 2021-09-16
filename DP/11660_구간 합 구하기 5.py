# PyPY3에서 통과
import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
lst = [0] * n
arr = [[0] * n for _ in range(n)]
# arr = [[0] * n] * n 처럼 선언하면 바라보는 객체가 동일
# = 값 변경시 다른 원소까지 변경

for i in range(n):
    lst[i] = list(map(int, sys.stdin.readline().split()))
    tmp = 0 
    for j in range(len(lst[i])):
        tmp += lst[i][j]
        arr[i][j] = tmp
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = 0
    for i in range(x1-1, x2):
        if y1 != 1:
            ans += arr[i][y2-1] - arr[i][y1-2]
        else:
            ans += arr[i][y2-1]
    print(ans)