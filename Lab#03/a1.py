import nltk
from nltk import word_tokenize

# Custom rule-based tagging
patterns = [
(r'.*ing$', 'VBG'), # gerunds
(r'.*ed$', 'VBD'), # simple past
(r'.*es$', 'VBZ'), # 3rd person singular present
(r'.*ould$', 'MD'), # modals
(r'.*\'s$', 'NN$'), # possessive nouns
(r'.*s$', 'NNS'), # plural nouns
(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
(r'.*', 'NN') # default to noun
]

# Input sentence
sentence = "The cat is chasing the mouse."

# Tokenize and apply rule-based POS tagging
regexp_tagger = nltk.RegexpTagger(patterns)
tokens = word_tokenize(sentence)
tagged = regexp_tagger.tag(tokens)

print(tagged)