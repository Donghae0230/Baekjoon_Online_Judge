import sys
sys.stdin = open("input.txt","r")   

def cnt(n, room):
    temp = room[:n + 1]
    for i in range(1, n + 1):
        room[i] = sum(temp[:i + 1])
    return room
case = int(input())
for _ in range(case):
    room = list(range(15))
    k = int(input())
    n = int(input())
    for i in range(k):
        room = cnt(n, room)
    print(room[n])