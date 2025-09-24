n , m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= m:
                result = max(result, sum)
                

print(result)

# i + 1, j + 1 이런 식으로 적은 이유
# 전부 range(n) 형식으로 쓴다면 같은 카드를 여러 번 뽑는 중복이 발생하기 떄문이다.

# 따라서 그렇게 적은 이유는
# → 같은 카드를 두 번 뽑는 걸 막기 위해서
# → (0, 1, 2) / (1, 0, 2) 같은 중복된 경우를 제거하기 위해서
# → 그리고 i < j < k가 되도록 만들어서 서로 다른 3장의 조합만 탐색하게 하려고!
