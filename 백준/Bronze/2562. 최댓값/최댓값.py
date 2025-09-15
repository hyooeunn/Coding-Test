max = 0
position = 0

for i in range(9):
    num = int(input())
    if num > max:
        max = num
        position = i + 1

print(max)
print(position)