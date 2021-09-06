import sys
sys.stdin = open("input.txt", "r")

def func(k):
    if k == m:  #arr 길이가 m일 때 출력 
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(1, n + 1):   #1부터 n까지 오름차순
        if not issued[i]:
            arr[k] = i
            issued[i] = True
            func(k+1)
            issued[i] = False

# 문제: 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 모든 수열
n, m = map(int, input().split())
arr = [0] * (m + 1)
issued = [False] * (n + 1)  #수가 쓰였는지 나타냄
func(0)
