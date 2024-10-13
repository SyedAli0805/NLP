from textblob import TextBlob

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

word_tokenize = TextBlob(text).words
print("Printing Stem Words: ")
for word in word_tokenize:
    print(word," | ",word.stem())