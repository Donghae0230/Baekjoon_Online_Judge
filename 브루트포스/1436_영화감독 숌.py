n = int(input())
num = 665
cnt = 0
while(cnt < n):
    num += 1
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        break;
print(num)