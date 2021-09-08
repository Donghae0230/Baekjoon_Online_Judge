import sys
sys.stdin = open("input.txt", "r")

def func(k):
    if k == m:
        for i in range(m):
            print(arr[i], end = ' ')
        print()
        return
    for i in range(1, n + 1):
        if arr[k-1] <= i:
            arr[k] = i
            func(k+1)

n, m = map(int, sys.stdin.readline().split())
arr = [0] * (m + 1)
func(0)