import pandas as pd
import re
import string
import nltk
from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Downloading Stopwords
nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()

# Reading CSV File
df = pd.read_csv(r'D:\Semester#07\Natural-Language-Programming\NLP-Labs\Lab#06\datasets\spam.csv', encoding='latin-1')
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
print(df.head())

def clean_text(txt):
    # remove punctuation
    txt = ''.join([c for c in txt if c not in string.punctuation])
    # split into tokens
    tokens = re.split(r'\W+', txt)
    # Filter out stopwords, empty tokens, and non-alphabetic tokens, then apply stemming
    txt = [ps.stem(word) for word in tokens if word and word.isalpha() and word not in stopwords]
    return ' '.join(txt)  # Join tokens back into a single string


# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer(analyzer=clean_text)

# Fit and transform the cleaned SMS data
x = tfidf.fit_transform(df['SMS'])
print('Dimensions of sparse matrix (docs*unique words):')
print(x.shape)
print('Sparse Matrix:')
print(x)

# Visualize in array form
print('Visualize in array form:')
print(x.toarray())

# Creating a DataFrame for the Vectorized Data
df_vectorized = pd.DataFrame(x.toarray(), columns=tfidf.get_feature_names_out())
print(df_vectorized)

# Sample data vectorization (taking rows 1 to 10 from the original cleaned SMS text)
data_sample = df['SMS'][1:10]

# Re-initialize TF-IDF Vectorizer for the sample
tfidf_sample = TfidfVectorizer()
x_sample = tfidf_sample.fit_transform(data_sample)

print('Displaying shape of only small sample data:')
print(x_sample.shape)
print('Unique tokens found in sample SMS:')
print(tfidf_sample.get_feature_names_out())

# Creating a DataFrame for the Vectorized Sample Data
df_sample_vectorized = pd.DataFrame(x_sample.toarray(), columns=tfidf_sample.get_feature_names_out())
print(df_sample_vectorized.head(10))


