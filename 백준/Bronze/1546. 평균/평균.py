subNum = int(input())
score = list(map(int, input().split()))
M = max(score)

new_score = [(i / M) * 100 for i in score]
print(sum(new_score) / subNum)