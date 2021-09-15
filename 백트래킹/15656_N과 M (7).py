import sys
sys.stdin = open("input.txt", "r")

def func(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(n):
        arr[k] = lst[i]
        func(k+1)

n, m = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))
arr = [0] * n
func(0)
