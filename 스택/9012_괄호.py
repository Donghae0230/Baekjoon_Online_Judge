import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    while "()" in s:
        s = s.replace("()","")
    if "(" in s or ")" in s:
        print("NO")
    else:
        print("YES")