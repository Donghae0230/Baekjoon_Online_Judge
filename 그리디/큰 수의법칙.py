n, m ,k = map(int, input().split())
data = list(map(int,input().split()))
data.sort()
first, second = data[-1], data[-2]

count = (m // (k + 1)) * k + (m % (k + 1))
res = first * count
res += second * (m - count)
print(res)