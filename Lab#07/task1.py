import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import f1_score, classification_report
# Load the dataset
df = pd.read_csv('D:\\Semester#07\\Natural-Language-Programming\\NLP-Labs\\Lab#07\\dataset\\tripadvisor_hotel_reviews.csv')
# Separate negative and positive reviews
df_neg = df.loc[df['Rating'] < 3].reset_index(drop=True)
df_five = df.loc[df['Rating'] == 5].reset_index(drop=True)
# Match the number of positive reviews with the negative reviews
df_pos = df_five.loc[:len(df_neg) - 1]
# Combine positive and negative reviews
df_all = pd.concat([df_neg, df_pos], axis=0).reset_index(drop=True)
# Add a Sentiments column with binary labels
df_all['Sentiments'] = np.where(df_all['Rating'] == 5, 'Positive', 'Negative')
# Shuffle the dataset
df_all = df_all.sample(frac=1).reset_index(drop=True)
# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
df_all['Review'], df_all['Sentiments'], test_size=0.2, random_state=42)
# Convert text data to feature vectors
v = TfidfVectorizer()
x_train_vec = v.fit_transform(x_train)
x_test_vec = v.transform(x_test)
# Train the SVM classifier
clf_svm = svm.SVC(kernel='linear', probability=True)
clf_svm.fit(x_train_vec, y_train)
# Evaluate the classifier
accuracy = clf_svm.score(x_test_vec, y_test)
print(f"Accuracy of the SVM classifier: {accuracy:.2f}")
# F1 Score
fscore = f1_score(y_test, clf_svm.predict(x_test_vec), average='weighted')
print(f"Weighted F1 Score: {fscore:.2f}")
# Classification report
print("\nClassification Report:")
print(classification_report(y_test, clf_svm.predict(x_test_vec)))
# Test with custom reviews
rev_neg = ['Absolutely hate this place, horrible food']
rev_neg_vec = v.transform(rev_neg)
prediction_neg = clf_svm.predict(rev_neg_vec)
print(f"Prediction for negative review: {prediction_neg[0]}")

rev_pos = ['We loved the cozy ambiance and attention to detail in the hotel decor.']
rev_pos_vec = v.transform(rev_pos)
prediction_pos = clf_svm.predict(rev_pos_vec)
print(f"Prediction for positive review: {prediction_pos[0]}")
