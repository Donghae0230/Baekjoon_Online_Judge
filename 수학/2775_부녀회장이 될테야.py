case = int(input())
for _ in range(case):
    room = list(range(15))
    k = int(input())
    n = int(input())
    for i in range(k):
        for i in range(1, n + 1):
            room[i] += room[i-1]
    print(room[n])