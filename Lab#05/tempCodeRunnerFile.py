from sklearn .feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

corpus = [
    'This is a positive sentence',
'I love Natural Language Processing.',
'Naive Bayes is a simple and effective algorithm.',
'Text classification is an important NLP task.',
'I dislike spam emails.',
'Machine Learning is a fascinating Field.'
]