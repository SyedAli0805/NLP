from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample corpus
corpus = ["I love this movie",
          "This movie is terrible",
          "The plot is confusing"]

vectorizer = CountVectorizer(binary=True)
one_hot_encoded = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())  # Use get_feature_names_out() in recent versions of sklearn
print(one_hot_encoded.toarray())

# Bag of Words
vectorizer = CountVectorizer()
bow_encoded = vectorizer.fit_transform(corpus)

# Print feature names and BoW vectors
print(vectorizer.get_feature_names_out())
print(bow_encoded.toarray())

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf_encoded = vectorizer.fit_transform(corpus)

# Print feature names and TF-IDF vectors
print(vectorizer.get_feature_names_out())
print(tfidf_encoded.toarray())
