"""
CP1404 Practical
Program to count word occurrences in a string
Estimated: 20 minutes
Actual: 40 minutes
"""
word_to_count = {}

user_string = input("Text: ")
words = user_string.split()

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

word_to_count = {word: word_to_count[word] for word in sorted(word_to_count)}
max_length = max(len(word) for word in words)
for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")
