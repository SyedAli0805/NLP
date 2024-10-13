import nltk

text = "Hello, world! This is NLP. SpaCy handles punctuation differently; special characters like @, #, and $ are also tokens."

nltk_tokens_word = nltk.word_tokenize(text)


print("\n NLTK Part of Speech Tagging: ")
for word in nltk.pos_tag(nltk_tokens_word):
    print(word)