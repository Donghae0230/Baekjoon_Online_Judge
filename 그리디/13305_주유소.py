import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
n = int(input())
length = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
res = 0
for i in range(n-1):  
    if cost[i] >= min_cost:
        # min_cost값 * 거리로 계산  
        res += min_cost * length[i]
    else:
        # 더 작은 값을 찾으면 min_cost 갱신
        min_cost = cost[i]
        res += min_cost * length[i]
print(res)