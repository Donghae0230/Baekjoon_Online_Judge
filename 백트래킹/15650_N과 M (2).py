import sys
sys.stdin = open("input.txt", "r")

def func(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(1, n + 1):
        if i > arr[k-1]:    #i가 arr 앞의 값보다 큰 경우
            arr[k] = i
            issued[i] = True
            func(k+1)
            issued[i] = False

n, m = map(int, sys.stdin.readline().split())
arr = [0] * (m + 1)
issued = [False] * (n + 1)
func(0)