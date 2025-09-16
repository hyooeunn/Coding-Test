t = int(input())

for _ in range(t):
    quiz = input()
    score = 0
    streak = 0
    
    for i in quiz:
        if i == 'O':
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)