from nltk import word_tokenize
from nltk.util import ngrams

#input text
text = "Natural Language Processing enables computers to understand human languages."

#Tokenization
tokens = word_tokenize(text)
print(tokens)

#Generate N-grams
print("\nPrinting Unigrams: \n")
unigrams = list(ngrams(tokens, 1))
print(unigrams)
print("\nPrinting Bigrams: \n")
bigrams = list(ngrams(tokens, 2))
print(bigrams)
print("\nPrinting Trigrams: \n")
trigrams = list(ngrams(tokens, 3))
print(trigrams)