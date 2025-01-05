import pandas as pd

df = pd.read_csv(r'D:\Semester#07\Natural-Language-Programming\NLP-Labs\Lab#10\dataset\StudentsPerformance.csv')

numeric_columns = ['math score', 'reading score', 'writing score']

df_cleaned = df.dropna()

df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(0)

print(df_cleaned.head(n=10))
