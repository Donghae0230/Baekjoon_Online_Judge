import sys
sys.stdin = open("input.txt","r") 

trans = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for i in trans:
    s = s.replace(i, '*')
print(len(s))