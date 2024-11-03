import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
#model training
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
# for Perfromance Evaluation
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_curve, auc
# Feature Selection
from sklearn.feature_selection import RFE
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest, mutual_info_classif

df = pd.read_csv(r'D:\Semester#07\Natural-Language-Programming\NLP-Labs\Lab#05\dataset\diabetes_dataset\diabetes1.csv',encoding='latin-1')
print(df.head())

print(df.isnull().sum())

# Handle missing values
df = df.replace('?', np.nan)
df = df.dropna()

# Plot Histogram
df.hist(figsize=(10, 8))
plt.show()

# Plot correlation heatmap
corr = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Task 3: Naïve Bayes Classifier Implementation
# Split data
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Naïve Bayes classifier
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Make predictions
y_pred = gnb.predict(X_test)

# Evaluate accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Task 4: Performance Evaluation
# Calculate metrics
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Plot confusion matrix
plt.imshow(confusion_matrix(y_test, y_pred), interpolation='nearest')
plt.title("Confusion Matrix")
plt.show()

# Plot ROC curve
fpr, tpr, _ = roc_curve(y_test, y_pred)
plt.plot(fpr, tpr, color='darkorange')
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")

plt.show()

# Task 5: Feature Selection
# Define selector
selector = SelectKBest(mutual_info_classif, k=5)

# Fit selector
selector.fit(X_train, y_train)

# Get selected features
support = selector.get_support()
print("Selected features:", X_train.columns[support])

# Train classifier with selected features
gnb.fit(X_train.iloc[:, support], y_train)

# Make predictions
y_pred = gnb.predict(X_test.iloc[:, support])

# Evaluate accuracy
print("Accuracy with selected features:", accuracy_score(y_test, y_pred))

# Task 6: Hyperparameter Tuning with Cross-Validation
param_grid = {'var_smoothing': [1e-9, 1e-8, 1e-7]}

grid_search = GridSearchCV(GaussianNB(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print("Optimal hyperparameters:", grid_search.best_params_)
print("Best score:", grid_search.best_score_)

# Train classifier with optimal hyperparameters
gnb = GaussianNB(**grid_search.best_params_)
gnb.fit(X_train, y_train)

# Make predictions
y_pred = gnb.predict(X_test)

# Evaluate accuracy
print("Accuracy with optimal hyperparameters:", accuracy_score(y_test, y_pred))