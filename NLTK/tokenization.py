import nltk

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

nltk_tokens_sent = nltk.sent_tokenize(text)
print("NLTK Sent Tokenization:")
for sent in nltk.sent_tokenize(text):
    print(sent)

nltk_tokens_word = nltk.word_tokenize(text)
print("\nNLTK Word Tokenization:", nltk_tokens_word)