import sys
sys.stdin = open("input.txt", "r")

def calPlus(s):
    res = 0
    for i in s.split('+'):
        res += int(i)
    return res

s = list(input().split('-'))    # '-'를 기준으로 나누기
for i in range(len(s)): #식에 있는 '+'제거 
    if '+' in s[i]: 
        s[i] = calPlus(s[i])
        
res = int(s[0]) 
for i in range(1,len(s)):
     res -= int(s[i])
print(res)