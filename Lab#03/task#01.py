import nltk
from nltk import word_tokenize

patterns = [
    (r'.*ing$', 'VBG'),  # gerunds (verb ending in -ing)
    (r'.*ed$', 'VBD'),   # simple past (verb ending in -ed)
    (r'.*es$', 'VBZ'),   # 3rd person singular present (verb ending in -es)
    (r'.*ould$', 'MD'),  # modals (like could, would)
    (r'.*\'s$', 'NN$'),  # possessive nouns (noun's)
    (r'.*s$', 'NNS'),    # plural nouns (nouns ending in -s)
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*ly$', 'RB'),    # adverbs (ending in -ly)
    (r'.*ous$', 'JJ'),   # adjectives (ending in -ous)
    (r'.*ive$', 'JJ'),   # adjectives (ending in -ive)
    (r'.*able$', 'JJ'),  # adjectives (ending in -able)
    (r'.*ful$', 'JJ'),   # adjectives (ending in -ful)
    (r'(The|the|A|a|An|an)$', 'DT'),  # determiners (articles)
    (r'(is|are|was|were|be|being|been|am)$', 'VB'),  # verb "to be"
    (r'(has|have|had)$', 'VB'),  # verb "to have"
    (r'[.,\'"?!]', 'PUNCT'),  # punctuation marks
    (r'.*', 'NN')        # default to noun
]


sentence = "The cat is chasing the small, elusive mouse happily."


regexp_tagger = nltk.RegexpTagger(patterns)
tokens = word_tokenize(sentence)
tagged = regexp_tagger.tag(tokens)

print(tagged)
