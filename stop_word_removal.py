import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer



import spacy
from textblob import TextBlob

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

text = "Hello everyone! Welcome to the course 123. We are studying Natural Language Processing."

#NLTK Stop Word Removal

nltk_stop_words = set(stopwords.words('english'))

nltk_tokens_word = nltk.word_tokenize(text)

nltk_filtered_words = [word for word in nltk_tokens_word if word.lower() not in nltk_stop_words]

print("\n NLTK Filtered Tokens (Stop Words Removed):")

print(nltk_filtered_words)

#SPACY Stop Word Removal

spacy_stop_words = nlp.Defaults.stop_words

spacy_doc = nlp(text)

# Filter out stop words from tokens
filtered_tokens = [token.text for token in spacy_doc if not token.is_stop]


# Filtered Tokens

print("\n SPACY Filtered Tokens (Stop Words Removed):")
print(filtered_tokens)