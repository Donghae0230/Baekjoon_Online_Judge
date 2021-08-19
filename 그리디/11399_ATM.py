import sys
sys.stdin = open("input.txt","r")

n = int(input())
data = sorted(list(map(int, input().split())))
res = 0
temp = 0
for  i in data:
    res += temp + i
    temp += i 
print(res)
