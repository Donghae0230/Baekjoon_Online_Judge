import sys
sys.stdin = open("input.txt","r")   

a, b, v = map(int, input().split())
days = (v-b)/(a-b)
print(int(days) if days == int(days) else int(days)+1)