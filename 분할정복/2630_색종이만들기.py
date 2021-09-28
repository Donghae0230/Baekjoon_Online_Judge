import sys
sys.stdin = open("input.txt", "r")

def cutPaper(x, y, n):  # x,y좌표와 색종이 크기 
    global cnt_white, cnt_blue
    print(x, y, n)
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:
                cutPaper(x, y, n//2)
                cutPaper(x, y+n//2, n//2)
                cutPaper(x+n//2, y, n//2)
                cutPaper(x+n//2, y+n//2, n//2)
                return # 호출한 함수는 중복되지 않도록 종료시킴

    if paper[x][y] == 1:
        cnt_blue += 1
    else:
        cnt_white += 1

n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt_white, cnt_blue = 0, 0
cutPaper(0,0,n)
print(cnt_white)
print(cnt_blue)
