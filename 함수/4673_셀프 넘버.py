def d(n):
    return n + sum(map(int, str(n)))

N = [i for i in range(1, 10001)]

ctor_num = []
for n in N:
    ctor_num.append(d(n))

self_num = [i for i in N if i not in ctor_num]
for n in self_num:
    print(n)