import sys
sys.stdin = open("input.txt","r")   

m, n = map(int, input().split())
comp = []
for _ in range(n):
    data = list(input().split())
    comp.append(min(data))
print(max(comp))
