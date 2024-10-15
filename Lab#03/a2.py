import nltk
from nltk.corpus import treebank
nltk.download('treebank')
# Load treebank tagged corpus
train_sents = treebank.tagged_sents()[:3000]

# Train an HMM tagger
hmm_tagger = nltk.HiddenMarkovModelTagger.train(train_sents)

# Input sentence
sentence = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(sentence)

# POS tagging using HMM tagger
tagged_sentence = hmm_tagger.tag(tokens)
print(tagged_sentence)