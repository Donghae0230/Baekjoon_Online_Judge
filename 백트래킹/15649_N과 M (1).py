import sys
sys.stdin = open("input.txt", "r")

def func(k):
    if k == m:  #arr 길이가 m일 때 출력 
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(1, n + 1):
        if not issued[i]:
            arr[k] = i
            issued[i] = True
            func(k+1)
            issued[i] = False

n, m = map(int, input().split())
arr = [0] * (m + 1)
issued = [False] * (n + 1)
func(0)
