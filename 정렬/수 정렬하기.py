import sys
sys.stdin = open("input.txt", "r")

n = int(input())
lst = [int(input()) for _ in range(n)]
for i in (sorted(lst)):
    print(i)