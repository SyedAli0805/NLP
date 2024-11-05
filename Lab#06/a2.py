import pandas as pd
import re
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer

#Downloading Stopwords
nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()

#Reading CSV File
df = pd.read_csv(r'D:\Semester#07\Natural-Language-Programming\NLP-Labs\Lab#06\datasets\spam.csv',encoding='latin-1')
print(df.head())

def clean_text(txt):
    # remove punctuation
    txt = ''.join([c for c in txt if c not in string.punctuation])
    # split into tokens
    tokens = re.split(r'\W+', txt)
    # Filter out stopwords, empty tokens, and non-alphabetic tokens, then apply stemming
    txt = [ps.stem(word) for word in tokens if word and word.isalpha() and word not in stopwords]
    return txt
#vectorizing the Text Data
cv1 = CountVectorizer(analyzer=clean_text)

x = cv1.fit_transform(df['SMS'])
print('Show shape of data, number of rows (total instances) and columns (unique tokens).')
print(x.shape)
print('unique tokens found in SMS:')
print(cv1.get_feature_names_out())


# Creating a DataFrame for the Vectorized Data
pd.set_option('display.max_colwidth', 100)
df1 = pd.DataFrame(x.toarray(), columns=cv1.get_feature_names_out())
print(df1.head(10))

# Sample data Vectorization
data_sample = df[1:10]
cv2 = CountVectorizer(analyzer=clean_text)

x=cv2.fit_transform(data_sample['SMS'])
print('displaying shape of only small sample data')
print(x.shape)
print('unique tokens found in sample SMS:')
print(cv2.get_feature_names_out())

# Creating a DataFrame for the Vectorized Data
pd.set_option('display.max_colwidth', 100)
df2 = pd.DataFrame(x.toarray(), columns=cv2.get_feature_names_out())
print(df2.head(10))