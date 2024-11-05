import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Creating the TfidfVectorizer Object
tfidf_vect = TfidfVectorizer()

# Defining the Corpus
corpus = [

'This is first sentence',
'This is second sentence',
'This is third sentence'
]

# Fitting the Model to the Corpus
x = tfidf_vect.fit(corpus)
print('learned vocabulary')
print(x.vocabulary_)
print('feature names (words)')
print(tfidf_vect.get_feature_names_out())

# Transforming the Corpus
x = tfidf_vect.transform(corpus)

print('dimensions of sparse matrix : docs*unique words:')
print(x.shape)
print('Sparse Matrix: ')
print(x)
print('visualize in array form:')
print(x.toarray())

# Creating a DataFrame
df = pd.DataFrame(x.toarray(), columns=tfidf_vect.get_feature_names_out())
print(df)