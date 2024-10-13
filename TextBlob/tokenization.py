from textblob import TextBlob

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

sentence_tokenize = TextBlob(text).sentences

print("TextBlob Sentence Tokenization: ",sentence_tokenize)

word_tokenize = TextBlob(text).words

print("\n\nTextBlob Word Tokenization:",word_tokenize)

#TextBlob does not provide built-in method to tokenize at character level