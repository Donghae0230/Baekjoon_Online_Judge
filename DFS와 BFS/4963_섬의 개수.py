import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(start, visited): 
    queue = deque()
    queue.append(start)
    dx = [-1, 1, 0, 0, 1, 1, -1, -1, 0]
    dy = [0, 0, 1, -1, 1, -1, 1, -1, 0]  
    while queue:
        x, y = queue.popleft()
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if island[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return visited

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    visited = [[0] * w for _ in range(h)]
    island = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0 
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and island[i][j] == 1:
                cnt += 1
                bfs([i,j], visited)   
    print(cnt)
