import pandas as pd

df = pd.read_csv(r'D:\Semester#07\Natural-Language-Programming\NLP-Labs\Lab#10\dataset\StudentsPerformance.csv')

# Calculate basic statistics for numeric columns
numeric_columns = ['math score', 'reading score', 'writing score']
statistics = df[numeric_columns].agg(['mean', 'median', 'min', 'max'])

print(statistics)
