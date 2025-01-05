import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\Semester#07\Natural-Language-Programming\NLP-Labs\Lab#10\dataset\StudentsPerformance.csv')

numeric_columns = ['math score', 'reading score', 'writing score']

df_cleaned = df.dropna()

df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(0)

plt.scatter(df_cleaned['math score'], df_cleaned['reading score'])
plt.title('Scatter Plot of Math Score vs Reading Score')
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.show()
