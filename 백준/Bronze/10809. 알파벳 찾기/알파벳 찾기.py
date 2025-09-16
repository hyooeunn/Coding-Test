s = list(input())
p = 'abcdefghijklmnopqrstuvwxyz'

for i in p:
    if i in s:
        print(s.index(i), end= ' ')
    else:
        print(-1, end= ' ')