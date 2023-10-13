"""
20 minutes, 40 minutes
"""
words_to_counts = {}


user_string = input("Text: ")
words = user_string.split()

for word in words:
    words_to_counts[word] = words_to_counts.get(word, 0) + 1

words_to_counts = {word: words_to_counts[word] for word in sorted(words_to_counts)}
max_length = max(len(word) for word in words)
for word, count in words_to_counts.items():
    print(f"{word:{max_length}} : {count}")

print(words_to_counts)
