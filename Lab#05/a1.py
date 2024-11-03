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

labels = ['positive','positive','positive','positive','negative','negative']

#split the data into train and test

x_train,x_test,y_train,y_test = train_test_split(corpus,labels,test_size=0.3,random_state=42)

#create countVectorizer to convert text data into numerical features
vectorizer = CountVectorizer()

# fit and transform the training data
x_train = vectorizer.fit_transform(x_train)

x_test = vectorizer.transform(x_test)

# create and train NB classifier
classifier = MultinomialNB()
classifier.fit(x_train, y_train)

#predict the labels for the test set
y_pred = classifier.predict(x_test)
print(x_test)
print(y_pred)
print(y_test)

#calculate the accuracy and display classification report
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f'Accuracy:{accuracy:2f}')
print('classification report: \n', classification_rep)

# prediction on new data
new_data =['I loved being with you', 'Haters will keep hating']
new_data_transformed = vectorizer.transform(new_data)

new_predictions = classifier.predict(new_data_transformed)

print('new data predictions:')
for text, prediction in zip(new_data, new_predictions):
    print(f'text: {text}, predicted label: {prediction}')