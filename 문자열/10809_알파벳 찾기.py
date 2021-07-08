s = input()
a = list(range(97,123))

for i in range(len(a)):
    print(s.find(chr(a[i])),end=' ')