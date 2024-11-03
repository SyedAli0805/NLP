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

# Load dataset
df_train = pd.read_csv(r'D:\Semester#07\Natural-Language-Programming\NLP-Labs\Lab#05\dataset\irrigation_dataset\train_data.csv', encoding='latin-1')
df_test = pd.read_csv(r'D:\Semester#07\Natural-Language-Programming\NLP-Labs\Lab#05\dataset\irrigation_dataset\test_data.csv',encoding='latin-1')
print(df_train.head())
print(df_test.head())

# Check for missing values
print("Missing Values of Training Data:\n", df_train.isnull().sum())
print("Missing Values of Training Data:\n", df_train.isnull().sum())

# # Handle missing values
df_train = df_train.replace('?', np.nan)
df_train = df_train.dropna()

df_test = df_test.replace('?', np.nan)
df_test = df_test.dropna()

# Plot Histogram
df_train.hist(figsize=(10, 8))
plt.show()

# Plot correlation heatmap
corr = df_train.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Features")
plt.show()

# # Task 3: Naïve Bayes Classifier Implementation
# Load training data
X_train = df_train.drop(['pump'],axis=1)  # Feature
y_train = df_train['pump']         # Target label

# Load test data
X_test = df_test.drop(['pump'],axis=1)   # Feature
y_test = df_test['pump']  # Actual Label


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
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
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
selector = SelectKBest(mutual_info_classif, k=2)

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