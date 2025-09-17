def decimal(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
num = list(map(int, input().split()))

count = 0
for i in num:
    if decimal(i):
        count += 1
        
print(count)