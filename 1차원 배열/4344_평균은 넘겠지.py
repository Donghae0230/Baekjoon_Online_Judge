n = int(input())
while n:
    score = list(map(int, input().split()))
    avg = (sum(score) - score[0])/score[0]
    num = 0
    for i in range(score[0]):
        if score[i+1] > avg:
            num += 1
    print("{:.3f}%".format(num/score[0]*100))
    n -= 1



    
    
