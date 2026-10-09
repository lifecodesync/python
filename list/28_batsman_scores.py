# 28. Scores of a batsman in 10 matches
scores = [45, 102, 67, 8, 120, 55, 33, 99, 0, 74]
total = sum(scores)
centuries = 0
half_centuries = 0
for s in scores:
    if s >= 100:
        centuries += 1
    elif s >= 50:
        half_centuries += 1
print("Scores:", scores)
print("Highest score:", max(scores))
print("Lowest score:", min(scores))
print("Total runs:", total)
print("Average runs:", total / len(scores))
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)
