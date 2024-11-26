import nltk
nltk.download('stopwords')

stopwords = set(nltk.corpus.stopwords.words('english'))  # Use set for faster lookups

# Sample corpus
corpus = ['Ibrahim is a lazy boy. His friend is also lazy.', 
          'Umar is not a lazy person']

# Removing stopwords
filtered_corpus = []
for sentence in corpus:
    filtered_sentence = ' '.join([word for word in sentence.split() if word.lower() not in stopwords])
    filtered_corpus.append(filtered_sentence)

print(filtered_corpus)
