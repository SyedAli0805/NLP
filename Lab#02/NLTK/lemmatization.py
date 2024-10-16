import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

lemmatizer = WordNetLemmatizer()

text = "After several attempts, Sarah finally solved the puzzle. Exhausted yet relieved, she smiled. 'Was it luck or skill?' she pondered, unsure. Nevertheless, her determination paid off, proving that perseverance, rather than luck, often leads to success."

tokenizer = RegexpTokenizer(r'\w+')

words = tokenizer.tokenize(text)
lemma_words = []
for word in words:
    lemma_words.append(lemmatizer.lemmatize(word))
print("Original Words: ",words)
print("\nLemmatized Words:",lemma_words)