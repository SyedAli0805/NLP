import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

import spacy
from textblob import TextBlob

#loading english model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

text = "Hello everyone! Welcome to the course 123. We are studying Natural Language Processing."

#sentence tokenize
nltk_tokens_sent = nltk.sent_tokenize(text)
print("NLTK Sentence Tokenization:",nltk_tokens_sent)

spacy_tokens_sent = list(nlp(text).sents)
print("SPACY Sentence Tokenization")
for sent in spacy_tokens_sent:
    print(sent.text)

textblob_tokens_sent = TextBlob(text)
print("TextBLOB Sentence Tokenization:",textblob_tokens_sent.sentences)

# Word tokenize
nltk_tokens_word = nltk.word_tokenize(text)
print("NLTK Word Tokenization:", nltk_tokens_word)

spacy_doc = nlp(text)
print("SpaCy Word Tokenization:")
for token in spacy_doc:
    print(token.text)


textblob_tokens_word = TextBlob(text)
print("TextBlob Word Tokenization:")
for word in textblob_tokens_word.words:
    print(word)

# Character-level tokenization
nltk_tokens_char = [list(word) for word in nltk_tokens_word]
print("NLTK Character Tokenization:", nltk_tokens_char)


print("SPACY Character-level Tokenization:")
for token in spacy_doc:
    print(f"Word: {token.text}")
    for char in token.text:
        print(f"  {char}")


print("TextBLOB Character-level Tokenization:")
for word in textblob_tokens_word.words:
    print(f"Word: {word}")
    for char in word:
        print(f"  {char}")