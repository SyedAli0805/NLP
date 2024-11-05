import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
corpus = [
    'This is first sentence',
    'This is second sentence',
    'This is third sentence'
]

x = cv.fit(corpus)
print(x.vocabulary_)
print(cv.get_feature_names_out())

x = cv.transform(corpus)
x = cv.fit_transform(corpus)

print(x.shape)
print(x.toarray())
df = pd.DataFrame(x.toarray(),columns=cv.get_feature_names_out())
print(df)