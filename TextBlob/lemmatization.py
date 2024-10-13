from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('wordnet')

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

word_tokenize = TextBlob(text).words
lemma_words = []
print("Printing TextBlob Lemma: ")
for word in word_tokenize:
    lemma_words.append(word.lemmatize())
print("Original Words: ",word_tokenize)
print("Lemmatize Words: ",lemma_words)