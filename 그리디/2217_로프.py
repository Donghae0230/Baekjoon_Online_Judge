# k개의 로프로 중량이 w인 물체를 들어올릴 때, 각 로프에는 w/k만큼의 중량이 걸린다.
# 들어올릴 수 있는 물체의 최대 중량은?(모든 로프 사용할 필요x) 

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
rope = [int(sys.stdin.readline()) for _ in range(n)]
rope.sort() # 오름차순으로 정렬
# 최대 중량 = 사용하는 로프의 가장 작은 중량 * 로프 개수
w = rope[-1]    # 가장 큰 로프 1개만 쓰는 경우
for i in range(1, n):
    rope.pop()
    temp = rope[-1] * (i + 1)
    if temp > w:
        w = temp
print(w)



