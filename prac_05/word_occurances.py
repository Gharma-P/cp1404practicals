"""
Write a program to count the occurrences of words in a string.
Estimate: 45mins
Actual: 75mins
"""

#sentence: this is a collection of words of nice words this is a fun thing it is
get_sentence = input("Enter a sentence: ").lower()

sentence_words = get_sentence.split()
repeated_words = {}
for word in sentence_words:
    count = repeated_words.get(word, 0)
    repeated_words[word] = count + 1

sorted_words = list(repeated_words.keys())
sorted_words.sort()

max_length = max(len(word) for word in sorted_words)

for word in sorted_words:
    print(f"{word:{max_length}} : {repeated_words[word]}")





