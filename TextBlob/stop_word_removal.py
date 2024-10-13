from textblob import TextBlob
from nltk.corpus import stopwords

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

word_tokenize = TextBlob(text).words

stopwords = set(stopwords.words('english'))

filtered_text = []

removed_stop_words = []

for word in word_tokenize:
    if word not in stopwords:
        filtered_text.append(word)
    else:
        removed_stop_words.append(word)

print("\n Text After Stopwords Removal: ",filtered_text)

print("\n Removed Stop Words: ", removed_stop_words)