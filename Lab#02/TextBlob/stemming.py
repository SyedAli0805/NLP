from textblob import TextBlob

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

word_tokenize = TextBlob(text).words
stem_words = []
print("Printing Stem Words: ")
for word in word_tokenize:
    stem_words.append(word.stem())

print("Original Words:",word_tokenize)
print("\nStem Words:",stem_words)