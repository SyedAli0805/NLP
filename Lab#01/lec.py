import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
import re
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

text = "Hello everyone! Welcome to the course 123. We are studying Natural Language Processing."

#sentence tokenize

tokens_sent = nltk.sent_tokenize(text)
print(tokens_sent)