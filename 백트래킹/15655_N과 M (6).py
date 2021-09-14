import sys
sys.stdin = open("input.txt", "r")

def func(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return 
    for i in range(len(lst)):
        if not issued[i]:
            if lst[i] > arr[k-1]:
                arr[k] = lst[i]
                issued[i] = True
                func(k + 1)
                issued[i] = False

n, m = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))
arr = [0] * (m + 1)
issued = [False] * (n + 1)
func(0)