from collections import Counter
from nltk import word_tokenize

#input text
text = "Pakistan Love Me I Love Me I Love Pakistan"
tokens = word_tokenize(text)

#Generate bigrams
bigrams = list(zip(tokens[:-1], tokens[1:]))
print(bigrams)

#Count unigrams and bigrams
unigram_counts = Counter(tokens)
print(unigram_counts)
bigram_counts = Counter(bigrams)
print(bigram_counts)

#Calculate bigram probabilitites
bigram_probabilities = {bigram: count / unigram_counts[bigram[0]] for bigram, count in bigram_counts.items()}
print(bigram_probabilities)
