def x(n):
    if n <= 99:
        return print(n)
    else:
        count = 99
        for i in range(100,n+1):
            num = []
            l = list(map(int, str(i)))
            for j in range(len(l)-1):
                num.append(l[j+1] - l[j])
            if len(set(num)) == 1:
                count += 1
        return print(count)

n = int(input())
x(n)
