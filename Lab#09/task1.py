from collections import Counter
from nltk import word_tokenize

#input text
text = "Pakistan Love Me I Love Me I Love Pakistan"
tokens = word_tokenize(text)

#Generate bigrams
bigrams = list(zip(tokens[:-1], tokens[1:]))
print(bigrams)

#Generate trigrams
trigrams = list(zip(tokens[:-2],tokens[1:],tokens[2:]))
print(trigrams)


#Count unigrams and bigrams
unigram_counts = Counter(tokens)
print(unigram_counts)
bigram_counts = Counter(bigrams)
print(bigram_counts)
trigram_counts = Counter(trigrams)
print(trigram_counts)

#Calculate bigram probabilitites
bigram_probabilities = {trigram: count / bigram_counts[trigram[0],trigram[1]] for trigram, count in trigram_counts.items()}
print(bigram_probabilities)
