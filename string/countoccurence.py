s = input("Enter a sentence: ")
word = input("Enter word: ")

words = s.split()
count = 0

for x in words:
    if x == word:
        count += 1

print("Occurrences:", count)