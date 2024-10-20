import nltk
from nltk.corpus import treebank
nltk.download('treebank')

# Load treebank tagged corpus
train_sents = treebank.tagged_sents()

# Train an HMM tagger
hmm_tagger = nltk.HiddenMarkovModelTagger.train(train_sents)

sentence = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(sentence)

tagged_sentence = hmm_tagger.tag(tokens)

print(tagged_sentence)