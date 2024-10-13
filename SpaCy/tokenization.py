import spacy

#loading english model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

text = "Hello, world! This is NLP. SpaCy handles punctuation differently; special characters like @, #, and $ are also tokens."

spacy_tokens_sent = list(nlp(text).sents)
print("SPACY Sentence Tokenization")
for sent in spacy_tokens_sent:
    print(sent.text)

spacy_tokens_word = nlp(text)
print("SpaCy Word Tokenization:")
for token in spacy_tokens_word:
    print(token.text)
