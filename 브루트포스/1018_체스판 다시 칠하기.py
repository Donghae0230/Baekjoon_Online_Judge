import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(input())

res = []
for i in range(n - 7):
    for j in range(m - 7):
        start_W, start_B = 0, 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):              
                if (k + l)%2 == 0:  
                    if lst[k][l] != 'W': start_W += 1  
                    if lst[k][l] != 'B': start_B += 1
                else :
                    if lst[k][l] != 'B': start_W += 1
                    if lst[k][l] != 'W': start_B += 1
        res.append(start_W)                         
        res.append(start_B)                         
print(min(res)) 