import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('punkt') 
nltk.download('omw-1.4') 

import spacy
from textblob import TextBlob

# Create an instance of WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

text = "Hello everyone! Welcome to the course 123. We are studying Natural Language Processing."

# Tokenize the text into words 
tokenized_words = word_tokenize(text)

# Lemmatize each word 
lemmatized_text = ' '.join([lemmatizer.lemmatize(word) for word in tokenized_words])

print("Original Text:", text)
print("Lemmatized Text:", lemmatized_text)

#SPACY Lemmatization

for word in text:
    print(word.text,  word.lemma_)

#TEXTBLOB Lemmatization
text = TextBlob("Hello everyone! Welcome to the course 123. We are studying Natural Language Processing.")
for word in text.words.lemmatize():
    print(word)
