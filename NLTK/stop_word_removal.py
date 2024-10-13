from nltk.corpus import stopwords
from nltk import word_tokenize

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

nltk_stop_words = set(stopwords.words('english'))

words = word_tokenize(text)

filtered_text = []
stopwords = []
for word in words:
    if word not in nltk_stop_words:
        filtered_text.append(word)
    else:
        stopwords.append(word)
print("Text after stop words removal:",filtered_text)
print("\n Removed Stopwords: ",stopwords)
